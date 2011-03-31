# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
"Human Resource"
import copy
from trytond.model import ModelView, ModelSQL, fields
from trytond.wizard import Wizard
from trytond.report import Report

class EmployeeBusinessMulty(ModelSQL):
    'Employee Business Multy'
    _name = 'company.employee.business'
    _description = __doc__

    employee = fields.Many2One('company.employee',
                                'Company', ondelete='CASCADE', required=True, select=1)
    business = fields.Many2One('ekd.business', 'Business',
                            ondelete='RESTRICT', required=True, select=1)

EmployeeBusinessMulty()

class Employee(ModelSQL, ModelView):
    _name = 'company.employee'

    business = fields.Many2Many('company.employee.business', 'employee', 'business', 'Business')

Employee()
