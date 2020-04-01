# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    grecaptcha_enabled = fields.Boolean('Recaptcha Enabled', related='website_id.grecaptcha_enabled', readonly=False)
    grecaptcha_site_key = fields.Char('Recaptcha Site Key', related='website_id.grecaptcha_site_key', readonly=False)
    grecaptcha_secret_key = fields.Char('Recaptcha Secret Key', related='website_id.grecaptcha_secret_key', readonly=False)
    grecaptcha_threshold = fields.Float('Recaptcha Threshold', related='website_id.grecaptcha_threshold', readonly=False)
    grecaptcha_snippet = fields.Text('Recaptcha Snippet', related='website_id.grecaptcha_snippet', readonly=True)
