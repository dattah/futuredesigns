# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _get_type_reference(self):
        for line in self:
            if line.sale_line_ids:
                line.type_reference = line.sale_line_ids[0].type_reference

    type_reference = fields.Char('Type Reference', compute='_get_type_reference')