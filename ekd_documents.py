# -*- coding: utf-8 -*-
from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pyson import In, If, Get, Eval, Not, Equal, Bool, Or, And

class DocumentTemplate(ModelSQL, ModelView):
    _name='ekd.document.template'

    business = fields.Property(fields.Many2One('ekd.business',
        'Business', domain=[('id','in', Eval('businesses'))]))

    def default_business(self):
        return Transaction().context.get('business') or False

DocumentTemplate()


class Document(ModelSQL, ModelView):
    _name='ekd.document'

    business = fields.Many2One('ekd.business', 'Business', domain=[('id','in', Eval('businesses'))])

    def default_business(self):
        return Transaction().context.get('business') or False


Document()
