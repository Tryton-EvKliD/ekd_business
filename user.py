# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
"Human Resource"
import copy
from trytond.model import ModelView, ModelSQL, fields
from trytond.wizard import Wizard
from trytond.report import Report
from trytond.pyson import In, If, Get, Eval, Not, Equal, Bool, Or, And


class UserBusinessMulty(ModelSQL):
    'User Business Multy'
    _name = 'res.user.business'
    _description = __doc__

    user = fields.Many2One('res.user', 'User',
                        ondelete='CASCADE', required=True, select=1)
    business = fields.Many2One('ekd.business', 'Business',
                        ondelete='RESTRICT', required=True, select=1)

UserBusinessMulty()

class User(ModelSQL, ModelView):
    _name = 'res.user'

    business = fields.Many2One('ekd.business', 'Business', domain=[('id','in', Eval('businesses'))])
    businesses = fields.Many2Many('res.user.business', 'user', 'business', 'Business')

    def __init__(self):
        super(User, self).__init__()
        self._context_fields.insert(0, 'business')
        self._context_fields.insert(0, 'businesses')
        self._preferences_fields.insert(0, 'business')

User()
