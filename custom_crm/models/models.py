# -*- coding: utf-8 -*-
from odoo import models, fields, api

class custom_crm(models.Model):
    _name = 'custom_crm.visit'
    _description = 'visit'

    name = fields.Char(string = 'Descripción')
    customer = fields.Char(string = 'Cliente')
    date = fields.Datetime(string = 'Fecha')
    type = fields.Selection([('P','Presencial'), ('W','WhatsApp'), ('T','Telefono')], string = 'Tipo visita', required=True )
    done = fields.Boolean(string = 'Realizado', readonly = True)

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
