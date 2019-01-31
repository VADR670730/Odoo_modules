# -*- coding: utf-8 -*-
{
    'name': "event_update",

    'summary': """
        Updating events module""",

    'description': """
        updating events module
    """,

    'author': "Omar-sekouti",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Events',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','event'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/view_event_update.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}