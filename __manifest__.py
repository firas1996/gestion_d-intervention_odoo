# -*- coding: utf-8 -*-
{
    'name': "Gestion Des Interventions",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Firas Hamila",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'template.xml',
        'views/index.xml',
        'views/project.xml',
        'views/rapport.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    "auto_install": False,
    "installable": True,
}

