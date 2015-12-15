# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'customers',
    'version' : '1.0',
   
    'description': """
I     This module is adding customer ID,purchase Orer in partner module
      picking Operation and delivery slip custom module.
      
    """,
    'depends' : ['base', 'mail','sale','stock','base_setup','report','account','purchase'],
    'data': ['views/res_partner_view.xml',
             'views/sale_order_view.xml',
             'views/stock_view.xml',
             'views/stock_picking_view.xml',
             'views/account_invoice_view.xml',
             'views/product_template_view.xml'
             ,'views/report_stock_picking.xml',
             'views/report_picking_slip.xml','views/purchase_order_view.xml'],
    'demo': [ ],
    'qweb': [ ],   
     'installable': True,
    'application': True,
    'auto_install': True,
    
}
