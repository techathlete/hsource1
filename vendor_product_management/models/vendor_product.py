#coding: utf-8

from odoo import _, api, fields, models


class vendor_product(models.Model):
    """
    The model to keep supplier products' list
    """
    _name = "vendor.product"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Vendor product"
    _rec_name = "product_name"

    @api.depends("quant_ids.active", "quant_ids", "quant_ids.supplier_quantity", "quant_ids.product_quantity",
                 "quant_ids.uom_error",)
    def _compute_vendor_quantity(self):
        """
        Compute method for vendor_quantity, uom_notes, zero_qty
        """
        for product in self:
            product.vendor_quantity = sum(product.quant_ids.mapped('product_quantity'))
            supplier_qty = sum(product.quant_ids.mapped('supplier_quantity'))
            product.zero_qty = not supplier_qty
            uom_notes = False
            if any(product.quant_ids.mapped('uom_error')):
                uom_notes = _("UoM issue preventing calculation of Quantity")
            product.uom_notes = uom_notes

    def _inverse_partner_id(self):
        """
        Inverse method for partner_id, product_name, product_code, product_id, product_tmpl_id, delay

        Extra info:
         * sudo() is required since portal users do not have rights for products
        """
        self = self.sudo()
        for product in self:
            if product.product_id and (not product.product_tmpl_id \
                    or product.product_tmpl_id != product.product_id.product_tmpl_id):
                product.product_tmpl_id = product.product_id.product_tmpl_id
            product.price_ids.write({
                "name": product.partner_id.id,
                "product_name": product.product_name,
                "product_code": product.product_code,
                "product_id": product.product_id.id,
                "product_tmpl_id": product.product_tmpl_id.id,
                "delay": product.delay,
            })

    def _inverse_active(self):
        """
        Inverse method for active
        If product is deactivated, we deactivated prices and quants
        If it activated back, we do nothing, since have no idea which were inversed deactivated, which were deactivated
        manually
        """
        for product in self:
            if not product.active:
                product.price_ids.sudo().write({"active": False})
                product.quant_ids.sudo().write({"active": False})

    @api.onchange("product_id")
    def _onchange_product_id(self):
        """
        Onchange method for product_id
        """
        for product in self:
            if product.product_id:
                product.product_tmpl_id = product.product_id.product_tmpl_id

    partner_id = fields.Many2one(
        "res.partner",
        string="Vendor",
        inverse=_inverse_partner_id,
        required=True,
    )
    labeler = fields.Char(
        string="Labeler/Manufacturer",
    )
    mfg_product_code = fields.Char(
        string="Mfg. Product Code",
    )
    lot_number = fields.Char(
        string="Lot/Serial Number",
    )
    expiration_date = fields.Char(
        string="Expiration/Available Date",
    )
    strength = fields.Char(
        string="Strength",
    )
    dosage_form = fields.Char(
        string="Dosage Form",
    )
    package_description = fields.Char(
        string="Package Description",
    )
    sell_quantity = fields.Integer(
        string="Sell Quantity",
    )
    uom = fields.Char(
        string="Unit of Measure",
    )
    total_box_in_case = fields.Char(
        string="Boxes in a Case",
    )
    total_each_in_box = fields.Char(
        string="Eaches in a Box",
    )
    location = fields.Char(
        string="Location",
    )
    cost_center = fields.Char(
        string="Facility / Cost Center",
    )
    product_name = fields.Char(
        string="Product Description",
        inverse=_inverse_partner_id,
    )
    product_code = fields.Char(
        string="Product Code",
        inverse=_inverse_partner_id,
    )
    product_id = fields.Many2one(
        'product.product',
        'Linked Product',
        inverse=_inverse_partner_id,
    )
    product_tmpl_id = fields.Many2one(
        'product.template',
        'Linked Template',
        inverse=_inverse_partner_id,
    )
    delay = fields.Integer(
        string="Additional Lead Time",
        inverse=_inverse_partner_id,
    )
    quant_ids = fields.One2many(
        "vendor.quant",
        "vendor_product_id",
        string="Inventory",
    )
    vendor_quantity = fields.Float(
        string="Quantity",
        compute=_compute_vendor_quantity,
        compute_sudo=True,
        store=True,
    )
    uom_notes = fields.Char(
        string="Notes",
        compute=_compute_vendor_quantity,
        compute_sudo=True,
        store=True,
    )
    zero_qty = fields.Float(
        string="Out of Stocks",
        compute=_compute_vendor_quantity,
        store=True,
        compute_sudo=True,
    )
    uom_name = fields.Char(
        related="product_tmpl_id.uom_name",
        compute_sudo=True,
    )
    price_ids = fields.One2many(
        "product.supplierinfo",
        "vendor_product_id",
        string="Pricing",
    )
    description = fields.Text(
        string="Additional Information",
    )
    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env.user.company_id.id,
        index=1,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        inverse=_inverse_active,
    )
    # to let portal users update products
    activity_date_deadline = fields.Date(compute_sudo=True)

    _order = "product_tmpl_id, product_id, partner_id, id"


    def name_get(self):
        """
        Overloading the method, to reflect parent's name recursively
        """
        result = []
        for product in self:
            name = u"[{}] {} - {}".format(
                product.product_code and product.product_code or '',
                product.product_name and product.product_name or '',
                product.partner_id and product.partner_id.name or '',
            )
            result.append((product.id, name))
        return result

    @api.model
    def _find_vendor_product(self, partner_id, product_code, product_name):
        """
        The method to find vendor product by code and name

        Args:
         * partner_id - res.partner object
         * product_code - char
         * product_name - char

        Returns:
         * int - vendor.product id
         * False if any not found
        """
        products = False
        if product_code:
            products = self._search([
                ("partner_id", "=", partner_id.id),
                ("product_code", "=", product_code),
                "|",
                    ("active", "=", True),
                    ("active", "=", False),
            ], limit=1)
            if not products and product_name:
                products = self._search([
                    ("partner_id", "=", partner_id.id),
                    ("product_code", "=", product_code),
                    ("product_name", "=", product_name),
                    "|",
                        ("active", "=", True),
                        ("active", "=", False),
                ], limit=1)
        return products and products[0] or False
