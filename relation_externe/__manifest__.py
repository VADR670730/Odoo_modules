# -*- coding: utf-8 -*-
{
    'name': "Post_grad",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "ESI",
    'website': "http://www.ESI.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human.Ressources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/view_demande_charge.xml',
        'views/view_bon_commande.xml',
        'views/templates.xml',
        'views/view_bon_commande_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}