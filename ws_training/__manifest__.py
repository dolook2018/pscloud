# -*- coding: utf-8 -*-
{
    'name': 'PS Cloud 培训',
    'version': '12.0.1.0',
    'summary': 'PS Cloud 培训',
    'author': "www.mypscloud.com",
    'website': 'https://www.mypscloud.com/',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'wizard/student_regiester_views.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/training_lesson_views.xml',
        'views/training_subject_views.xml',
        'reports/training_report.xml',
        'reports/training_sale_template.xml',
        'views/training_classroom_views.xml',
        'views/training_views.xml',
    ],
    'demo': ['demo/pscloud_demo.xml',
    ],
    'qweb': [],
    'js': [],
    'css': [],
    'auto_install': False,
    'application': True,
}
