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

    'sequence': 1,

    'author': "Assane DOUMBOUYA, Amy KANE, Cheikhouna NDIAYE, Hayib TOURE",
    'category': 'Industries',
    'version': '1.0',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/film_views.xml',
        'views/lieu_views.xml',
        'views/societe_production_views.xml',
        'views/tournage_views.xml',
        'views/realisateur_views.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}