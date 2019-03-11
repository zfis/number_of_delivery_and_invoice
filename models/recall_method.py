# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Call_method_save_stock_picking(models.Model):
    _inherit = 'stock.picking'
    number_of_pact = fields.Char(string="Number of Pact")
    @api.model
    def create(self, vals):
        vals['number_of_pact'] = vals['name'][-5:]
        res = super(Call_method_save_stock_picking, self).create(vals)
        return res

class Call_method_save_account_invoice(models.Model):
    _inherit = 'account.invoice'
    number_of_pact = fields.Char(string="Number of Pact")
    @api.model
    def create(self, vals):
        vals['number_of_pact'] = vals['number'][-4:]
        res = super(Call_method_save_account_invoice, self).create(vals)
        return res