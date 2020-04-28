# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json
import logging
from datetime import datetime
from werkzeug.exceptions import Forbidden, NotFound

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.exceptions import ValidationError
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class WebsiteSaleSource(WebsiteSale):
     def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        domains = super(WebsiteSaleSource, self)._get_search_domain( search, category, attrib_values, search_in_description)
        domains = [domains]
        pricelist_context, pricelist = self._get_pricelist_context()

        product_temp_ids = []

        categ_ids=[]
        for prod in pricelist.item_ids:
            if prod.product_tmpl_id:
                product_temp_ids.append(prod.product_tmpl_id.id)
            elif prod.product_id:
                product_temp_ids.append(prod.product_id.product_tmpl_id.id)
            elif prod.categ_id:
                categ_ids.append(prod.categ_id.id)

        subdomains = [[('id','in', product_temp_ids)]]

        if categ_ids:
            subdomains.append([('categ_id', 'child_of', categ_ids)])
        
        domains.append(expression.OR(subdomains))
        domains.append(expression.AND([[('list_price', '>', 0)]]))
        return expression.AND(domains)