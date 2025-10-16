# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, _


class CrmStage(models.Model):
    _inherit = "crm.stage"

    worksheet_template_id = fields.Many2one(
        comodel_name="worksheet.template",
        string="Worksheet Template",domain="[('res_model', '=', 'crm.lead')]",
        help="Worksheet to show when records move into this stage."
    )
    worksheet_model_name = fields.Char(
        string='Model Name', related='worksheet_template_id.model_id.model', readonly=True, store=True)
    worksheet_success_conditions = fields.Char(string='Success Conditions')
