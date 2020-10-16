# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_type_reference(self):
        for move in self:
            if move.sale_line_id:
                move.type_reference = move.sale_line_id.type_reference

    type_reference = fields.Char('Type Reference', compute='_get_type_reference')

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _get_type_reference(self):
        for line in self:
            if line.move_id and line.move_id.sale_line_id:
                line.type_reference = line.move_id.sale_line_id.type_reference

    type_reference = fields.Char('Type Reference', compute='_get_type_reference')