# -*- coding: utf-8 -*-
{
    'name': "S of T (School of IT)",

    'summary': """
        We are startup company based on technology education""",

    'description': """
        This is school management system software supported in Odoo 10

        by A sryn
    """,

    'author': "A SRYN",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'New Module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    "report"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/school_category_view.xml',
        'views/school_L_view.xml',
        'views/res_partner.xml',
        'views/school_session_view.xml',
        'report/report_session.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "demo"          : [],
    "test"          : [],
    "images"        : [],
    "qweb"          : [],
    "css"           : [],
    "application"   : True,
    "installable"   : True,
    "auto_install"  : False,
}