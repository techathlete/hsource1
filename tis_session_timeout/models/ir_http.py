# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _authenticate(cls, auth_method='user'):
        res = super(IrHttp, cls)._authenticate(auth_method=auth_method)
        if request and request.env and request.env.user:
            request.env.user._auth_timeout_check()
        return res
