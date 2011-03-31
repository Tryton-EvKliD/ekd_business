# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Business',
    'name_ru_RU': 'Направление деятельности',
    'version': '1.8.0',
    'author': 'Dmitry Klimanov',
    'email': 'k-dmitry2@narod.ru',
    'website': 'http://www.delfi2000.ru/',
    'description': '''Add accounting second business
''',
    'description_ru_RU': '''Добавляет возможность ведения управленчесского учета в разрезе вида деятельности
''',
    'depends': [
        'ekd_company',
        'ekd_documents',
        'ekd_account',
        'ekd_budget',
        'ekd_project',
    ],
    'xml': [
         'xml/ekd_business.xml',
#         'xml/company.xml',
#         'xml/employee.xml',
#         'xml/user.xml',
         'xml/move_ru.xml',
#         'xml/balance.xml',
         'xml/ekd_documents.xml',
         'xml/ekd_system.xml',
         'xml/ekd_doc_cash_view.xml',
         'xml/ekd_doc_advance_view.xml',
         'xml/ekd_doc_request_view.xml',
    ],
    'translation': [
        'ru_RU.csv',
    ],
}
