# -*- coding: utf-8 -*-

from odoo import models, fields


class estudio(models.Model):
     _name = 'estudio.estudio'
     _description = 'estudio.estudio'
    
     name = fields.Char()
     Cedula = fields.Integer()
     Edad = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

#     @api.depends('value')
 #    def _value_pc(self):
  #       for record in self:
#             record.value2 = float(record.value) / 100
