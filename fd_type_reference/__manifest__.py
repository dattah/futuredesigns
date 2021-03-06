# -*- coding: utf-8 -*-
{
    'name': "Future Designs Type Reference",

    'summary': """
        Add type reference field to sale order lines, invoice lines and deliveries.
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Bizanova",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale',
        'account'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/account_views.xml',
        'views/stock_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
