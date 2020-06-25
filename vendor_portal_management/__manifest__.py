# -*- coding: utf-8 -*-
{
    "name": "Vendor Products Portal",
    "version": "13.0.1.0.1",
    "category": "Purchases",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/13.0/vendor-products-portal-447",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "vendor_product_management",
        "website"
    ],
    "data": [
        "data/data.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/view.xml",
        "views/res_config_settings.xml",
        "views/core_templates.xml",
        "views/vendor_product_template.xml",
        "views/vendor_location_template.xml"
    ],
    "qweb": [
        "static/src/xml/*.xml"
    ],
    "js": [

    ],
    "demo": [

    ],
    "external_dependencies": {},
    "summary": "The tool to motivate vendors to prepare product catalogue in your Odoo",
    "description": """
    This tool aims to force suppliers to administrate their products in your Odoo portal. The app let vendor contacts to create, update, and import products they sell, related prices and stock levels by their locations.

    Vendor products catalog in portal
    Vendor stocks control without effort
    Supplier prices management and self-management
    Comfortable importing of vendor product data
    # How vendor stocks work
    <div class="alert alert-danger">
<span style="font-size:18px"> 
<i class="fa fa-exclamation-triangle"></i> Our warehouses' stocks are not linked to vendor stocks. Vendor stocks are absolutely independent since we can't control all supplier moves, and, hence, can't support double-entry system
</span> 
</div>
<ul>
<li>Each stock level is provided per definite vendor location. Vendors might easily create, edit, and archive own warehouses</li>
<li>Each vendor might have an unlimited number of locations. Locations are distinguished by name, address, and average delivery time</li>
<li>Stock levels are manageed in vendor units of measure, but purchase managers should make sure it has the same category as our linked product. The idea is to support conversion in order internal users work with habitual figures.  For example, dozens and units are fine, while dozens and hours might lead to mistakes</li>
<li>Vendor stocks and locations might be switched off for portal users on the configuration page</li>
<li>Stock levels are not used in our moves, but they are provided for general information. Stock levels are updated either manually or through the import process. It might be done by both portal and purchase users</li>
</ul>
    # How to import vendor products and stocks
    The tool let portal and purchase users import vendor products and prices as an Excel table of the <strong>predefined format</strong>
<ul>
<li>The table format is supplied with this tool source code and would be available in the portal under the section 'Help'</li>
<li>You may change the table content to provide users with more specific examples and labels. However do no not change columns' order and do not remove those: it would lead to inevitable mistakes</li>
<li>The wizard offers useful tips to make a correct import. You may edit those recommendations on the configuration page, but make sure you do not remove critical advice</li>
<li>Each import finishes with the special results' and errors' pop-up. It let users control of what has been actually done</li>
<li>In the wizard users may select which table lines should be imported. It is useful in case the number of lines is too big to import them all</li>
<li>In the wizard portal users can select whether their previous products' list should be archived. It let fully replace the product catalogue with a new one</li>
<li>In the wizard it is possible to make previous prices outdated. It let users remove misleading data</li>
<li>In case import can't be fully finished until Odoo stops it, contact your system administrator to increase configured time-outs</li>
</ul>
    # How to import vendor product and prices
    The tool let portal and purchase users import products and stock levels as an Excel table of the <strong>predefined format</strong>
<ul>
<li>The table format is supplied with this tool source code and would be available in the portal under the section 'Help'</li>
<li>You may change the table content to provide users with more specific examples and labels. However do no not change columns' order and do not remove those: it would lead to inevitable mistakes</li>
<li>The wizard offers useful tips to make a correct import. You may edit those recommendations on the configuration page, but make sure you do not remove critical advice</li>
<li>Each import finishes with the special results' and errors' pop-up. It let users control of what has been actually done</li>
<li>In the wizard users might select which table lines should be imported. It is useful in case the number of lines is too big to import them all</li>
<li>In the wizard portal users can select whether their previous products' list should be archived. It let fully replace the product catalogue with a new one</li>
<li>In the wizard it is possible to mark previous stocks as not any more topical</li>
<li>In case import can't be fully finished until Odoo stops it, contact your system administrator to increase configured time-outs</li>
</ul>
    Vendor portal: main page
    List of vendor products in portal for self-administration
    Suppliers edit product info by themselves
    Vendor may easy change important product details
    Vendors notify you about available stocks
    Suppliers keep up-to-dated prices in portal
    Vendors are notified about results of their actions
    Vendors import products and stocks through portal
    The template for vendor stock levels table (backend)
    Vendors might import products and update prices
    The template for vendor products' table (backend)
    Import results' and errors' pop-up in portal
    Grant vendor contacts an access to portal
    Grant vendor contacts an access to portal (2)
    List of locations of a vendor currently logged in
    Supplier location (warehouse) in portal
    Vendors might create / update their locations
    Vendor products interface (backend)
    Control vendor inventories per each product (backend)
    Vendor product form (backend)
    Vendor stocks on a product form (backend)
    Import of vendor products and stocks (backend)
    Stocks import wizard' recommendations (backend)
    Import of vendor products and prices (backend)
    Prices import wizard goes with detailed recommendations (backend)
    Configure your own configurations for import (backend)
    Vendor stock level form per each product (backend)
    Vendor locations list (not linked to our locations!)
    Check results and errors of import (backend)
    Vendor stocks by product templates (backend)
    Access stocks of this supplier from a partner form (backend)
    I faced the error: QWeb2: Template 'X' not found
    <div class="knowsystem_block_title_text">
            <div class="knowsystem_snippet_general" style="margin:0px auto 0px auto;width:100%;">
                <table align="center" cellspacing="0" cellpadding="0" border="0" class="knowsystem_table_styles" style="width:100%;background-color:transparent;border-collapse:separate;">
                    <tbody>
                        <tr>
                            <td width="100%" class="knowsystem_h_padding knowsystem_v_padding o_knowsystem_no_colorpicker" style="padding:20px;vertical-align:top;text-align:inherit;">
                                
                                <ol style="margin:0px 0 10px 0;list-style-type:decimal;"><li><p class="" style="margin:0px;">Restart your Odoo server and update the module</p></li><li><p class="" style="margin:0px;">Clean your browser cache (Ctrl + Shift + R) or open Odoo in a private window.</p></li></ol></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    What are update policies of your tools?
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 115% }
	</style>


</p><p lang="en-US" style="margin:0px 0px 0.25cm 0px;line-height:120%;">According to the current Odoo Apps Store policies:</p><ul style="margin:0px 0 10px 0;list-style-type:disc;"><li><p lang="en-US" style="margin:0px;line-height:120%;"> every module bought for the version 12.0 and prior gives you an access to the all versions up to 12.0. </p></li><li><p lang="en-US" style="margin:0px;line-height:120%;">starting from the version 13.0, every version of the module should be purchased separately.</p></li><li><p lang="en-US" style="margin:0px;line-height:120%;">disregarding the version, purchasing a tool grants you a right for all updates and bug fixes within a major version.<br></p></li></ul><p lang="en-US" style="margin:0px 0px 0.25cm 0px;line-height:120%;">Take into account that Odoo Tools team does not control those policies. By all questions please contact the Odoo Apps Store representatives <a href="https://www.odoo.com/contactus" style="text-decoration:none;color:rgb(13, 103, 89);background-color:transparent;">directly</a>.</p>
    May I buy your app from your company directly?
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="margin:0px 0px 10px 0px;">Sorry, but no. We distribute the
tools only through the <a href="https://apps.odoo.com/apps" style="text-decoration:none;color:rgb(13, 103, 89);background-color:transparent;">official Odoo apps store</a></p>
    How should I install your app?
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="line-height:120%;margin:0px 0px 10px 0px;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><ol style="margin:0px 0 10px 0;list-style-type:decimal;">
	<li><p style="margin:0px;line-height:120%;">Unzip source code of purchased tools in one of your Odoo
	add-ons directory</p>
	</li><li><p style="margin:0px;line-height:120%;">Re-start the Odoo server</p>
	</li><li><p style="margin:0px;line-height:120%;">Turn on the developer mode (technical settings)</p>
	</li><li><p style="margin:0px;line-height:120%;">Update the apps' list (the apps' menu)</p>
	</li><li><p style="margin:0px;line-height:120%;">Find the app and push the button 'Install'</p>
	</li><li><p style="margin:0px;line-height:120%;">Follow the guidelines on the app's page if those exist.</p>
</li></ol>
    Your tool has dependencies on other app(s). Should I purchase those?
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="margin:0px 0px 0.25cm 0px;line-height:120%;">Yes, all modules marked in dependencies are absolutely required for a correct work of our tool. Take into account that price marked on the app page already includes all necessary dependencies.&nbsp;&nbsp;</p>
    I noticed that your app has extra add-ons. May I purchase them afterwards?
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><p style="margin:0px 0px 0.25cm 0px;line-height:120%;">Yes, sure. Take into account that Odoo
automatically adds all dependencies to a cart. You should exclude
previously purchased tools.</p>
    I would like to get a discount
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><p style="margin:0px 0px 0.25cm 0px;line-height:120%;">
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


</p><p style="margin:0px 0px 0.25cm 0px;line-height:120%;">Regretfully, we do not have a
technical possibility to provide individual prices.</p>
    How can I install your app on Odoo.sh?
    
	
	
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		a:link { so-language: zxx }
	-->
	</style>


<p style="margin:0px 0px 10px 0px;">As soon as you purchased the
app, the button 'Deploy on Odoo.sh' will appear on the app's page in
the Odoo store. Push this button and follow the instructions.</p>
<p style="margin:0px 0px 10px 0px;">Take into account that for paid
tools you need to have a private GIT repository linked to your
Odoo.sh projects</p>
    May I install the app on my Odoo Online (SaaS) database?
    <p style="margin:0px 0px 10px 0px;">No, third party apps can not be used on Odoo Online.</p>
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "100.0",
    "currency": "EUR",
}
