# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def action_fsm_validate(self, stop_running_timers=False):
        """
        Validate the FSM task and send an invitation to the customer to complete
        a survey based on the service type related to the task's sale order.

        This method first checks if a survey email template is available. Then,
        depending on the service type ('security' or 'two_way_radio'), it selects
        the corresponding survey. If a valid survey is found and the task has an
        associated partner with an email, it generates a survey link and sends
        an email to the customer with the survey invitation.

        Args:
            stop_running_timers (bool): Flag to stop running timers. Defaults to False.

        Returns:
            res: The result of the original action_fsm_validate method.
        """
        res = super().action_fsm_validate(stop_running_timers)

        template = self.env.ref(
            'aak_crm_customer_feedback.mail_template_tower_install_survey_invite'
        )
        if not template:
            return res

        service_type = self.sale_order_id.team_id.service_type
        if service_type not in ['security', 'two_way_radio']:
            return res

        survey_mapping = {
            'security': 'aak_crm_customer_feedback.customer_satisfaction_survey',
            'two_way_radio': 'aak_crm_customer_feedback.two_way_radio_and_communications_feedback_survey'
        }
        survey = self.env.ref(survey_mapping.get(service_type))
        if not survey:
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
