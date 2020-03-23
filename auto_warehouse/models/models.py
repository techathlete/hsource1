# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    country_ids = fields.One2many(string='Countries Served', comodel_name='res.country',  inverse_name='warehouse_id')
    state_ids = fields.One2many(string='States Served', comodel_name='res.country.state', inverse_name='warehouse_id')

class Country(models.Model):
    _inherit = 'res.country'

    warehouse_id = fields.Many2one(string='Closest Warehouse', comodel_name='stock.warehouse', ondelete='cascade')

class CountryState(models.Model):
    _inherit = 'res.country.state'

    warehouse_id = fields.Many2one(string='Closest Warehouse', comodel_name='stock.warehouse', ondelete='cascade')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_shipping_id')
    def _change_partner_shipping_id(self):
        for s in self:
            if s['partner_shipping_id'] and s['partner_shipping_id']['country_id']:
                Warehouse = self.env['res.country']
                wids = Warehouse.search(['country_ids.id', '=', s['partner_shipping_id']['country_id']])
                if wids and len(wids.ids) > 0:
                    s['warehouse_id'] = wids[0]
