# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models


class CRMCheckWizard(models.TransientModel):
    _name = 'crm.check.wizard'
    _description = 'Wizard on which worksheet loads'

    lead_id = fields.Many2one(comodel_name='crm.lead', string='Lead')
