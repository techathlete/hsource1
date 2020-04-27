# -*- coding: utf-8 -*-

from odoo import  api, fields, models


PARAMS = [
#    ("vendor_product_help", str, ""),
#    ("vendor_stocks_help", str, ""),
    ("vendor_pharma_help", str, ""),
    ("vendor_medical_help", str, ""),
    ("vendor_capital_help", str, ""),
]


class res_config_settings(models.TransientModel):
    _inherit = "res.config.settings"

#    vendor_product_import_id = fields.Many2one(
#        "ir.attachment",
#        string="Product Template",
#    )
#    vendor_product_help = fields.Html(
#        string="Help for Products"
#    )
#    vendor_stocks_import_id = fields.Many2one(
#        "ir.attachment",
#        string="Inventory Template",
#    )
#    vendor_stocks_help = fields.Html(
#        string="Help for Inventory"
#    )

    vendor_pharma_import_id = fields.Many2one(
        "ir.attachment",
        string="Pharma Template",
    )
    vendor_pharma_help = fields.Html(
        string="Help for Pharma"
    )

    vendor_medical_import_id = fields.Many2one(
        "ir.attachment",
        string="Medical Template",
    )
    vendor_medical_help = fields.Html(
        string="Help for Medical"
    )

    vendor_capital_import_id = fields.Many2one(
        "ir.attachment",
        string="Capital Template",
    )
    vendor_capital_help = fields.Html(
        string="Help for Capital"
    )

    @api.model
    def get_values(self):
        """
        Overwrite to add new system params
        """
        Config = self.env['ir.config_parameter'].sudo()
        res = super(res_config_settings, self).get_values()
        values = {}
        for field_name, getter, default in PARAMS:
            values[field_name] = getter(str(Config.get_param(field_name, default)))
#        vendor_stocks_import_id = int(Config.get_param('vendor_stocks_import_id', 0))
#        vendor_product_import_id = int(Config.get_param('vendor_product_import_id', 0))
        vendor_pharma_import_id = int(Config.get_param('vendor_pharma_import_id', 0))
        vendor_medical_import_id = int(Config.get_param('vendor_medical_import_id', 0))
        vendor_capital_import_id = int(Config.get_param('vendor_capital_import_id', 0))
        values.update({
#            "vendor_stocks_import_id": vendor_stocks_import_id,
#            "vendor_product_import_id": vendor_product_import_id,
            "vendor_pharma_import_id": vendor_pharma_import_id,
            "vendor_medical_import_id": vendor_medical_import_id,
            "vendor_capital_import_id": vendor_capital_import_id,
        })
        res.update(**values)
        return res

    def set_values(self):
        """
        Overwrite to add new system params
        """
        Config = self.env['ir.config_parameter'].sudo()
        super(res_config_settings, self).set_values()
        for field_name, getter, default in PARAMS:
            value = getattr(self, field_name, default)
            Config.set_param(field_name, value)

#        vendor_product_import_id = self.vendor_product_import_id and self.vendor_product_import_id.id or 0
#        if self.vendor_product_import_id and not self.vendor_product_import_id.public:
#            self.vendor_product_import_id.public = True
#        Config.set_param("vendor_product_import_id", vendor_product_import_id)
#        vendor_stocks_import_id = self.vendor_stocks_import_id and self.vendor_stocks_import_id.id or 0
#        if self.vendor_stocks_import_id and not self.vendor_stocks_import_id.public:
#            self.vendor_stocks_import_id.public = True
#        Config.set_param("vendor_stocks_import_id", vendor_stocks_import_id)

        vendor_pharma_import_id = self.vendor_pharma_import_id and self.vendor_pharma_import_id.id or 0
        if self.vendor_pharma_import_id and not self.vendor_pharma_import_id.public:
            self.vendor_pharma_import_id.public = True
        Config.set_param("vendor_pharma_import_id", vendor_pharma_import_id)

        vendor_medical_import_id = self.vendor_medical_import_id and self.vendor_medical_import_id.id or 0
        if self.vendor_medical_import_id and not self.vendor_medical_import_id.public:
            self.vendor_medical_import_id.public = True
        Config.set_param("vendor_medical_import_id", vendor_medical_import_id)

        vendor_capital_import_id = self.vendor_capital_import_id and self.vendor_capital_import_id.id or 0
        if self.vendor_capital_import_id and not self.vendor_capital_import_id.public:
            self.vendor_capital_import_id.public = True
        Config.set_param("vendor_capital_import_id", vendor_capital_import_id)

