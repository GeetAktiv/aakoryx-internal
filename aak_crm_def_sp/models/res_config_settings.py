# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _get_crm_lead_user_domain(self):
        return [('id', 'in', self.env['res.users'].search([]).filtered(lambda u: u.has_group('sales_team.group_sale_salesman')).ids)]

    crm_lead_user_id = fields.Many2one(comodel_name='res.users', string='User',
                                       config_parameter='aak_crm_def_sp.default_crm_lead_user_id',
                                       domain=_get_crm_lead_user_domain)
