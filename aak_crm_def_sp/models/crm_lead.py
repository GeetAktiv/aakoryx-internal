# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        IrConfigParameter = self.env['ir.config_parameter'].sudo()
        param_key = 'aak_crm_def_sp.default_crm_lead_user_id'
        if IrConfigParameter.get_param(param_key):
            defaults['user_id'] = int(IrConfigParameter.get_param(param_key))
        return defaults
