# -*- coding: utf-8 -*-
{
    'name': "estudio",

    'summary': """
        Este es un modulo de aprendizaje""",

    'description': """
        Este es el mejor modulo para realizar pruebas de concepto
    """,

    'author': "Jonathan",
    'website': "http://www.todoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/vista_estudio.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    
    ],
}
