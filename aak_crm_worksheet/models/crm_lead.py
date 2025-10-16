# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from ast import literal_eval

from odoo import models, _
from odoo.osv import expression

class CrmLead(models.Model):
    _inherit = "crm.lead"

    def action_crm_lead_worksheet(self, stage_id, vals):
        self.ensure_one()
        stage_id = self.env['crm.stage'].browse(stage_id)
        action = stage_id.worksheet_template_id.action_id.sudo().read()[0]
        worksheet = self.env[stage_id.worksheet_template_id.model_id.sudo().model].search(
            [('x_crm_lead_id', '=', self.id)])
        context = literal_eval(action.get('context', '{}'))
        action_name = "Worksheet"
        wizard_id = self.env['crm.check.wizard'].create({
            'lead_id': self.id,
        })
        action.update({
            'name': action_name,
            'res_id': worksheet.id if worksheet else False,
            'views': [(False, 'form')],
            'target': 'new',
            'context': {
                **context,
                'edit': True,
                'default_x_crm_lead_id': self.id,
                'stage_id': stage_id.id,
                'vals': vals,
                'wizard_id': wizard_id.id,
            },
        })
        return action

    def action_worksheet_check(self):
        self.ensure_one()
        is_passed = False
        stage_id = self.env['crm.stage'].browse(self.env.context.get('stage_id'))
        domain = literal_eval(stage_id.worksheet_success_conditions or '[]')
        model = self.env[stage_id.worksheet_template_id.model_id.sudo().model]
        if model.search_count(expression.AND([domain, [('x_crm_lead_id', '=', self.id)]]), limit=1):
            is_passed = True
            self.write(self.env.context.get('vals'))
        return {'type': 'ir.actions.client', 'tag': 'soft_reload'}, is_passed

    def action_worksheet_discard(self):
        return {'type': 'ir.actions.act_window_close'}

    def action_set_won_rainbowman(self):
        """
        Override the default 'Set Won' behavior to add custom worksheet logic.

        Instead of immediately setting the lead as won, this method opens the
        worksheet wizard first (if the stage has a worksheet). Once the worksheet
        is validated, the stage is officially updated to 'Won'. If the wizard is
        discarded, the stage remains unchanged.
        """
        self.ensure_one()
        stage = self.stage_id
        won_stage = self.env['crm.stage'].search([('is_won', '=', True)], limit=1)

        # If no worksheet template or no won stage, fallback to default behavior
        if not won_stage or not stage or not won_stage.worksheet_template_id:
            return super(CrmLead, self).action_set_won_rainbowman()

        # Prepare values (simulate what will be written when validated)
        vals = {'stage_id': won_stage.id}

        # Open the worksheet popup before actually setting the stage
        action = self.action_crm_lead_worksheet(won_stage.id, vals)

        if isinstance(action, dict) and action.get("type", "").startswith("ir.actions"):
            return action

        # If somehow no worksheet action, fallback to normal Odoo behavior
        return super(CrmLead, self).action_set_won_rainbowman()