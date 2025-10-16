# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def action_fsm_validate(self, stop_running_timers=False):
        res = super().action_fsm_validate(stop_running_timers)
        template = self.env.ref(
            'aak_crm_customer_feedback.mail_template_tower_install_survey_invite'
        )
        survey = self.env.ref(
            'aak_crm_customer_feedback.survey_customer_feedback'
        )
        if not template or not survey:
            return res

        for task in self:
            if task.partner_id and task.partner_id.email:
                # Create user input record for the survey
                user_input = self.env['survey.user_input'].create({
                    'survey_id': survey.id,
                    'partner_id': task.partner_id.id,
                    'email': task.partner_id.email,
                })

                # Build the survey link and send the email
                survey_url = f"{task.get_base_url()}/survey/{survey.access_token}/{user_input.access_token}"
                template.sudo().with_context(survey_url=survey_url).send_mail(task.id, force_send=True)
        return res
