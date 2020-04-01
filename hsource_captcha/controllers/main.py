# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from odoo import _,http
import requests, logging, json
_logger = logging.getLogger(__name__)


class WebsiteForm(WebsiteForm):
                    
    # Check and insert values from the form on the model <model>
    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        website = request.env['website'].get_current_website()
        success = website and website.grecaptcha_verify(**kwargs)
        if not success:
            return json.dumps(False)
        return super(WebsiteForm, self).website_form(model_name, **kwargs) 


class AuthSignupHome(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        if kw and kw.get('grecaptcha'):
            qcontext = self.get_auth_signup_qcontext()
            website = request.env['website'].get_current_website()
            success = website and website.grecaptcha_verify(**kw)
            if not success:
                qcontext['error'] = _('Google ReCaptcha Failed.')
                qcontext['invalid_token'] = True
                response = request.render('auth_signup.signup', qcontext)
                response.headers['X-Frame-Options'] = 'DENY'
                return response
        return super(AuthSignupHome, self).web_auth_signup()
