# -*- coding: utf-8 -*-
from odoo import models, fields, api

class custom_crm(models.Model):
    _name = 'custom_crm.visit'
    _description = 'visit'

    name = fields.Char(string = 'Descripción')
    customer = fields.Many2one(string = 'Cliente', comodel_name = 'res.partner')
    date = fields.Datetime(string = 'Fecha')
    type = fields.Selection([('P','Presencial'), ('W','WhatsApp'), ('T','Telefono')], string = 'Tipo visita', required=True )
    done = fields.Boolean(string = 'Realizado', readonly = True)
    image = fields.Binary(string = 'Imagen')

    def toggle_state(self):
        self.done = not self.done