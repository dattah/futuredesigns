# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fd_type_reference(models.Model):
#     _name = 'fd_type_reference.fd_type_reference'
#     _description = 'fd_type_reference.fd_type_reference'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
