# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields

class CompanyBusinessMulty(ModelSQL):
    'Company Business Multy'
    _name = 'ekd.business.company'
    _description = __doc__

    company = fields.Many2One('company.company',
                                'Company', ondelete='CASCADE', required=True, select=1)
    business = fields.Many2One('ekd.business', 'Business',
                                                ondelete='RESTRICT', required=True, select=1)

CompanyBusinessMulty()

class Company(ModelSQL, ModelView):
    _name = 'company.company'

    businesses = fields.Many2Many('ekd.business.company', 'company', 'business', 'Business')

Company()
