# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
"Business"
from trytond.model import ModelView, ModelSQL, fields
#from trytond.wizard import Wizard
#from trytond.report import Report
import copy


class Business(ModelSQL, ModelView):
    'Business'
    _name = 'ekd.business'
    _description = __doc__

    name = fields.Char('Name', size=None, required=True, translate=True)
    shortname = fields.Char('Short Name', size=None, required=True, translate=True)
    code = fields.Char('Internal Code')
    code_legal = fields.Char('Code Legal')
    parent = fields.Many2One('ekd.business', 'Parent')
    system_tax = fields.Many2One('ekd.account.tax.group', 'System Tax')
    childs = fields.One2Many('ekd.business', 'parent', 'Children')
    companies = fields.One2Many('ekd.business.company', 'business', 'Child Company')
    employees = fields.One2Many('ekd.business.employee', 'business', 'Child Employee')
    users = fields.One2Many('ekd.business.user', 'business', 'Child Employee')
    start_date = fields.Date('Start date')
    end_date = fields.Date('End date')
    active = fields.Boolean('Active')

Business()
