# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import requests, logging, json
_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'

    grecaptcha_enabled = fields.Boolean('Recaptcha Enabled')
    grecaptcha_site_key = fields.Char('Recaptcha Site Key')
    grecaptcha_secret_key = fields.Char('Recaptcha Secret Key')
    grecaptcha_threshold = fields.Float('Recaptcha Threshold', default=0.5, help='Setting the threshold for what is considered a non-suspicious user. Default to 0.5. 1.0 is very likely a good interaction, 0.0 is very likely a bot.')
    grecaptcha_snippet = fields.Text('Recaptcha Code Snippet', 
                                     readonly=True, 
                                     help="Place this code inside of your website template's form element.",
                                     default=
"""
<div class="form-group row form-field" t-if="website.grecaptcha_enabled and website.grecaptcha_site_key">
    <t t-set="grecaptcha_site_key" t-value="website.grecaptcha_site_key"/>
    <input id="site_key" t-att-value="grecaptcha_site_key" type="hidden"/>
    <script t-att-src="'https://www.google.com/recaptcha/api.js?render=' + grecaptcha_site_key"></script>
    <script>
        grecaptcha.ready(function() {
           grecaptcha.execute(document.getElementById('site_key').value).then(function(token) {
           let input = document.getElementById('grecaptcha');
           input.value = token;
           });
        });
    </script>
    <input class="form-control o_website_form_input" id="grecaptcha" name="grecaptcha" type="hidden"/>
</div>
"""
    )

    def grecaptcha_verify(self, **kw):
        self.ensure_one()
        if self and self.grecaptcha_enabled:
            url = "https://www.google.com/recaptcha/api/siteverify"
            secret_key = self.grecaptcha_secret_key
            captcha_response = kw.get('grecaptcha')
            payload = {
                'secret': secret_key,
                'response': captcha_response,
            }
            gg_response = requests.get(url, params=payload, verify=True).json()
            _logger.info(str(gg_response))
            if not gg_response.get('success') or gg_response.get('score') < self.grecaptcha_threshold:
                return False
        return True
