# -*- coding: utf-8 -*-
{
    'name': "H-Source: products hidden",
    'summary': """
       Hide products if <0 on pricelist
    """,

    'description': """
        Task ID: 2230401 - AAL
        
Products are assigned to one of three Pricelists: Consumer, Hosptial, Government. 
 Customers with portal access to eCommerce are assigned to one of three Pricelists: 
 Consumer, Hospital, Government.  When a Customer visits the Products on the Shop page,
  they should see only the Products they can buy.
    """,

    'author': "Odoo PS-US",
    'website': "http://www.odoo.com",
    'license': 'OEEL-1',

    'category': 'Custom Development',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        'views/inherit_products_template.xml'
    ],
}