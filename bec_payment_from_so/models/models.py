# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class bec_payment_from_so(models.Model):
#     _name = 'bec_payment_from_so.bec_payment_from_so'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100