# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class vendor_capital_import(models.TransientModel):
    """
    The model to reflect low sold product variants
    """
    _name = "vendor.capital.import"
    _inherit = "vendor.import.wizard"
    _description = 'Import vendor products'

    @api.model
    def _default_template_table_id(self):
        """
        Default method for template_table_id
        """
        attach_id = int(self.env['ir.config_parameter'].sudo().get_param('vendor_capital_import_id', 0))
        attach_obj = self.env["ir.attachment"]
        return attach_id and attach_obj.browse(attach_id) or attach_obj

    @api.model
    def _default_help_text(self):
        """
        Default method for help_text
        """
        return self.env['ir.config_parameter'].sudo().get_param('vendor_capital_help', "")

    @api.depends("template_table_id")
    def _compute_url(self):
        """
        Compute method for url
        """
        for wiz in self:
            url = '/web/content/{}?download=true'.format(wiz.template_table_id.id,)
            wiz.url = url

    archive_products = fields.Boolean(
        string="Replace existing Products",
    )
    template_table_id = fields.Many2one(
        "ir.attachment",
        string="Template",
        default=_default_template_table_id,
        readonly=True,
    )
    help_text = fields.Html(
        string="Help",
        default=_default_help_text,
        readonly=True,
    )
    url = fields.Char(
        string="Download template",
        compute=_compute_url,
        readonly=True,
    )

    def _process_import(self):
        """
        The method to create vendor products & prices
         1. Archive previous products / prices if asked to
         2. Prepare values from the table
         3. Adapt each value format of fields, check for errors
         4. Update / create vendor product
         5. Update / create supplier info (price)

        Methods:
         * _prepare_values of vendor.import.wizard
         * _find_vendor_product of vendor.product
         * _find_exactly_the_same_price of product.supplierinfo
         * _parse_float
         * _parse_date

        Returns:
         * list (results - updated vendor.products), list (errors)

        Extra info:
         * Expected singleton
        """
        self.ensure_one()
        vendor_product = self.env["vendor.product"]
        vendor_quant = self.env["vendor.quant"]
        vendor_location = self.env["vendor.location"]
        supplier_info = self.env["product.supplierinfo"]
        errors = []
        results = []
        #1
        if not self.import_chosen_lines:
            if self.archive_products:
                to_archive = vendor_product.search([("partner_id", "=", self.partner_id.id)])
                to_archive.write({"active": False})
        # 2
        fields = [
                  "id","labeler","product_code","mfg_product_code","product_name","description","lot_number","expiration_date",
                  "sell_quantity","uom","price","currency","min_qty","date_start","date_end","location","delay", "cost_center"
                 ]
        values = self._prepare_values(fields, "vendor.product")
        line_num = 1
        for val in values:
            # 3
            line_num += 1
            labeler = val[1]
            product_code = val[2]
            mfg_product_code = val[3]
            product_name = val[4]
            description = val[5]
            lot_number = val[6]
            expiration_date = val[7]
            sell_quantity = val[8]
            uom = val[9]
            price, price_error = self._parse_float(val[10])
            currency, currency_error = self._parse_currency(val[11])
            min_qty, min_qty_error = self._parse_float(val[12])
            date_start, date_start_error = self._parse_date(val[13])
            date_end, date_end_error = self._parse_date(val[14])
            location = val[15]
            delay = val[16]
            cost_center = val[17]
            if not product_code or not product_name:
                errors.append(
                    _(u"There is no UDC/GTIN Code or Product Description defined on line {}. Line is skipped;".format(line_num))
                )
                continue
            if not location:
                errors.append(
                    _(u"There is no location defined on line {}. The line is skipped;".format(line_num))
                )
                continue
            if price_error or min_qty_error or date_start_error or date_end_error or currency_error:
                errors.append(
                    _(u"Not all columns of the line {} are parsed. Errors: {} {} {} {} {}".format(
                        line_num,
                        price_error and price_error or "",
                        min_qty_error and min_qty_error or "",
                        date_start_error and date_start_error or "",
                        date_end_error and date_end_error or "",
                        currency_error and currency_error or "",
                    ))
                )
                continue
            supplier_product_uom_id = False
            if uom:
                uom_ids = self.env["uom.uom"]._search([("name", "=", uom)], limit=1)
                if uom_ids:
                    supplier_product_uom_id = uom_ids[0]
                else:
                    errors.append(
                        _(u"Unit of measure name {} on line {} is not found".format(
                            uom,
                            line_num,
                        ))
                    )

            # 4
            product = vendor_product._find_vendor_product(self.partner_id, product_code, product_name)

            pr_values = {
                "partner_id": self.partner_id.id,
                "active": True,
                "product_code": product_code,
                "mfg_product_code": mfg_product_code,
                "product_name": product_name,
                "labeler": labeler,
                "description": description, "lot_number": lot_number, "expiration_date": expiration_date,
                "sell_quantity": sell_quantity,
                "uom": uom, "total_box_in_case": total_box_in_case, "total_each_in_box": total_each_in_box,
                "cost_center": cost_center,
            }
            if not product:
                product = vendor_product.create(pr_values).id
                _logger.debug(u"Vendor product {} is created".format(product))
            else:
                vendor_product.browse(product).write(pr_values)
                _logger.debug(u"Vendor product {} is updated".format(product))
            if product not in results:
                results.append(product)
            # 5
            supplier_info_id = supplier_info._find_exactly_the_same_price(product, min_qty, date_start, date_end,
                                                                          currency)
            supplier_info_vals = {
                "vendor_product_id": product,
                "price": price,
                "min_qty": min_qty,
                "date_start": date_start,
                "date_end": date_end,
                "currency_id": currency or self.env.user.sudo().company_id.currency_id.id,
                "active": True,
            }
            if not supplier_info_id:
                supplier_info_id = supplier_info.create(supplier_info_vals).id
                _logger.debug(u"Price {} of vendor product is created".format(supplier_info_id, product))
            else:
                supplier_info.browse(supplier_info_id).write(supplier_info_vals)
                _logger.debug(u"Price {} of vendor product is updated".format(supplier_info_id, product))

            # 6
            if location:
              location_id = vendor_location._find_or_create_location(location, self.partner_id, delay)

            # 7
            quant_id = vendor_quant._find_quant(product, location_id)
            vendor_quant_vals = {
                "vendor_product_id": product,
                "vendor_location_id": location_id,
                "supplier_quantity": sell_quantity,
                "active": True,
            }
            if supplier_product_uom_id:
                vendor_quant_vals.update({"supplier_product_uom_id": supplier_product_uom_id})
            if not quant_id:
                quant_id = vendor_quant.create(vendor_quant_vals).id
                _logger.debug(u"Vendor quant {} for product {} is created".format(quant_id, product))
            else:
                vendor_quant.browse(quant_id).write(vendor_quant_vals)
                _logger.debug(u"Vendor quant {} for product {} is created".format(quant_id, product))

            if quant_id not in results:
                results.append(quant_id)

            self.env.cr.commit()

        return results, errors
