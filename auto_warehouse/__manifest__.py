# -*- coding: utf-8 -*-
{
    'name': "auto_warehouse",

    'summary': """Auto populate the closets warehouse in SO form.""",

    'description': """
        https://www.odoo.com/web#id=2220590&action=333&active_id=360&model=project.task&view_type=form&cids=3&menu_id=4720
    """,

    'author': "Odoo, Inc.",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'account', 'sale_management', 'account_accountant', 'mrp', 'contacts', 'sale_stock', 'sale'],

    # only loaded in demonstration mode
    'demo': [],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
