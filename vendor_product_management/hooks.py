# -*- coding: utf-8 -*-


def pre_init_hook(cr):
    """Loaded before installing the module.

    None of this module's DB modifications will be available yet.

    If you plan to raise an exception to abort install, put all code inside a
    ``with cr.savepoint():`` block to avoid broken databases.

    :param openerp.sql_db.Cursor cr:
        Database cursor.
    """
    pass


def post_init_hook(cr, registry):
    """
    Loaded after installing the module.
    The goal is create default help and templates for imports

    This module's DB modifications will be available.

    :param openerp.sql_db.Cursor cr:
        Database cursor.

    :param openerp.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    from odoo import _, api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    attachment_obj = env["ir.attachment"]
    Config = env['ir.config_parameter']
    supplier_info = env["product.supplierinfo"]
    vendor_product = env["vendor.product"]

#    product_path = "vendor_product_management/static/xls/vendor_products.xlsx"
#    stocks_path = "vendor_product_management/static/xls/vendor_quants.xlsx"
    pharma_path = "vendor_product_management/static/xls/pharma_product_template.xlsx"
    medical_path = "vendor_product_management/static/xls/medical_product_template.xlsx"
    capital_path = "vendor_product_management/static/xls/capital_product_template.xlsx"
#    product_table_id = attachment_obj.create({
#        "name": _("Vendor Products Template"),
#        "url": product_path,
#        "type": "url",
#        "public": True,
#    }).id
#    stocks_table_id = attachment_obj.create({
#        "name": _("Vendor Stocks Template"),
#        "url": stocks_path,
#        "type": "url",
#        "public": True,
#    }).id
    pharma_table_id = attachment_obj.create({
        "name": _("Pharma Template"),
        "url": pharma_path,
        "type": "url",
        "public": True,
    }).id
    medical_table_id = attachment_obj.create({
        "name": _("Medical Template"),
        "url": medical_path,
        "type": "url",
        "public": True,
    }).id
    capital_table_id = attachment_obj.create({
        "name": _("Capital Template"),
        "url": capital_path,
        "type": "url",
        "public": True,
    }).id

#    product_help = """<h4>While preparing the table for import take into account:</h4>
#    <ul>
#        <li>The columns in the template are strictly defined. Do not re-arrange and do not remove them</li>
#        <li>One of the columns 'Product name' or 'Product code' must be filled up. Other columns are optional</li>
#        <li>There should be no empty lines</li>
#        <li>The first line is always a line with headers. Lines with real data should start from the line 2</li>
#        <li>If you have different prices for the same product, create a line for each for each price</li>
#        <li>Currency should be chosen among the list of available currencies</li>
#        <li>Dates should have proper date cell format</li>
#        <li>Numbers should have proper number format in all cells</li>
#        <li>The option 'archive products' if chosen would lead to archivation of previous products</li>
#        <li>The option 'mark previous prices as outdated' if chosen would lead to archivation of previous products' prices</li>
#    </ul>"""
#    stocks_help = """<h4> While preparing the table for import take into account:</h4>
#    <ul>
#        <li>The columns in the template are strictly defined. Do not re-arrange and do not remove them</li>
#        <li>The column 'Location name' should be filled up as well as one of the columns 'Product name' or 'Product
#        code'. Other columns are optional</li>
#        <li>There should be a single line for each combination product - location</li>
#        <li>The first line is always a line with headers. Lines with real data should start from the line 2</li>
#        <li>There should be no empty lines</li>
#        <li>Numbers should have proper number format in all cells</li>
#        <li>Units of measure should be chosen among the list of available UoMs</li>
#        <li>The option 'archive products' if chosen would lead to archivation of previous products</li>
#        <li>The option 'archive previous stocks' if chosen would lead to archivation of previous products' stock
#        levels</li>
#    </ul>"""

    pharma_help = """<h4> While preparing the Pharmaceuticals table for import take into account:</h4>
    <ul>
    </ul>"""
    medical_help = """<h4> While preparing the Medical/Surgical Supplies table for import take into account:</h4>
    <ul>
    </ul>"""
    capital_help = """<h4> While preparing the Capital Equipment table for import take into account:</h4>
    <ul>
    </ul>"""

#    Config.set_param("vendor_product_help", product_help)
#    Config.set_param("vendor_stocks_help", stocks_help)
    Config.set_param("vendor_pharma_help", pharma_help)
    Config.set_param("vendor_medical_help", medical_help)
    Config.set_param("vendor_capital_help", capital_help)
#    Config.set_param("vendor_product_import_id", product_table_id)
#    Config.set_param("vendor_stocks_import_id", stocks_table_id)
    Config.set_param("vendor_pharma_import_id", pharma_table_id)
    Config.set_param("vendor_medical_import_id", medical_table_id)
    Config.set_param("vendor_capital_import_id", capital_table_id)

    existing_supplier_info_ids = supplier_info.search([])
    for info in existing_supplier_info_ids:
        ex_ven_product = vendor_product.search([
            ("partner_id", "=", info.name.id),
            ("product_id", "=", info.product_id.id),
            ("product_tmpl_id", "=", info.product_tmpl_id.id),
        ],limit=1)
        if not ex_ven_product:
            values = {
                "partner_id": info.name.id,
                "product_tmpl_id": info.product_tmpl_id.id,
                "delay": info.delay,
            }
            values_list = []
            if info.product_id:
                new_vals = values.copy()
                new_vals.update({
                    "product_id": info.product_id.id,
                    "product_code": info.product_code or info.product_id.default_code,
                    "product_name": info.product_name or info.product_id.name,
                })
                values_list = [new_vals]
            else:
                for pr_variant in info.product_tmpl_id.product_variant_ids:
                    new_vals = values.copy()
                    new_vals.update({
                        "product_id": pr_variant.id,
                        "product_code": info.product_code or pr_variant.default_code,
                        "product_name": info.product_name or pr_variant.name,
                    })
                    values_list += [new_vals]
            for val in values_list:
                ex_ven_product = vendor_product.create(val)
        info.vendor_product_id = ex_ven_product

def uninstall_hook(cr, registry):
    """Loaded before uninstalling the module.

    This module's DB modifications will still be available. Raise an exception
    to abort uninstallation.

    :param openerp.sql_db.Cursor cr:
        Database cursor.

    :param openerp.modules.registry.RegistryManager registry:
        Database registry, using v7 api.
    """
    pass


def post_load():
    """Loaded before any model or data has been initialized.

    This is ok as the post-load hook is for server-wide
    (instead of registry-specific) functionalities.
    """
    pass
