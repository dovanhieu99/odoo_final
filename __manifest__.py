# -*- coding: utf-8 -*-
{
    'name': 'Quản lí Sinh Viên alo',
    'version': '12.0',
    'summary': 'Demo Module Relation',
    'sequence': 1,
    'description': """""",
    'category': '',
    'website': '',
    'depends': ['base'],
    'data': [
        'data/sequence.xml',
        'views/students.xml',
        'views/khoa_hoc.xml',
        'views/chuyen_nganh.xml',
        'views/mon_hoc.xml',
        'views/point.xml',
        'views/class_class.xml',
        'views/menu.xml',
        'security/group.xml',
        'security/ir.model.access.csv',
        # 'wizard/point_point.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}