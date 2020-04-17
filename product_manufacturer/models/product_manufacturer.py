# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    manufacturer = fields.Many2one(comodel_name="res.partner", string="Manufacturer")
    manufacturer_pname = fields.Char(string="UDC Number (GTIN)")
    manufacturer_pref = fields.Char(string="Catalog/Mfg. #")
    manufacturer_purl = fields.Char(string="Mfg. Product URL")
