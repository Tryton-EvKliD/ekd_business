# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
import gettext
_ = gettext.gettext

class BalanceAccount(ModelSQL, ModelView):
    _name = "ekd.balances.account"

    business = fields.Many2One('ekd.business', 'Business')

    def default_business(self):
        return Transaction().context.get('business') or False

BalanceAccount()

class BalancePartner(ModelSQL, ModelView):
    _name = "ekd.balances.party"

    business = fields.Many2One('ekd.business', 'Business')

    def default_business(self):
        return Transaction().context.get('business') or False

BalancePartner()

class BalanceProduct(ModelSQL, ModelView):
    _name = "ekd.balances.product"

    business = fields.Many2One('ekd.business', 'Business')

    def default_business(self):
        return Transaction().context.get('business') or False

BalanceProduct()

class BalanceAnalytic(ModelSQL, ModelView):
    _name = "ekd.balances.analytic"

    business = fields.Many2One('ekd.business', 'Business')

    def default_business(self):
        return Transaction().context.get('business') or False

BalanceAnalytic()

class BalanceFinance(ModelSQL, ModelView):
    _name = "ekd.balances.finance"

    business = fields.Many2One('ekd.business', 'Business')

    def default_business(self):
        return Transaction().context.get('business') or False

BalanceFinance()
