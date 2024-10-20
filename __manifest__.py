# -*- coding: utf-8 -*-
{
    'name': "Gestion de tournage de films",

    'summary': 'Module pour gérer les tournages de films',

    'description': """
        Ce module permet de gérer les tournages de films, incluant :
        - Films
        - Lieux de tournage
        - Sociétés de production
        - Tournages
        - Réalisateurs
    """,

    'author': "HTTECH",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Industries',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}