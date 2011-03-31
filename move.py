# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction

class MoveRU(ModelSQL, ModelView):
    _name = 'ekd.account.move'

    business = fields.Many2One('ekd.business', 'Business')

    def default_business(self):
        return Transaction().context.get('business') or False

MoveRU()
