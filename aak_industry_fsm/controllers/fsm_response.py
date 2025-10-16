# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import http
from odoo.http import request


class FSMResponseController(http.Controller):
    """HTTP endpoints to collect simple YES/NO responses from customers."""

    @http.route(
        ['/aak/fsm/respond/<int:task_id>/<string:answer>'],
        type='http', auth='public', methods=['GET'], csrf=False, sitemap=False
    )
    def aak_fsm_respond(self, task_id, answer, **kwargs):
        """
        Handle YES/NO button clicks from customers.

        - Validates task existence
        - Logs a chatter message on the task
        - Notifies task assignees via email template
        - Renders a small thank-you page

        The output (messages, emails, template rendering) is unchanged.
        """
        answer = (answer or '').strip().lower()
        Task = request.env['project.task'].sudo()
        task = Task.browse(task_id).exists()
        if not task:
            return request.render('portal.http_error', {'status_code': 404})

        if answer not in ('yes', 'no'):
            answer = 'unknown'

        # 1. Log chatter message
        task.message_post(
            body=f"Customer responded: {answer.upper()} via email buttons.",
            message_type="comment",
            subtype_xmlid="mail.mt_comment",
        )

        # 2. Notify task assignees with email template
        try:
            template = request.env.ref("aak_industry_fsm.mail_template_field_service_response")
        except Exception:
            # Template may be removed or not installed; keep behavior silent.
            template = False

        if template:
            template.with_context(response=answer).send_mail(
                task.id,
                force_send=True,
            )

        # 3. Render simplified thank-you page (no task context needed)
        return request.render(
            "aak_industry_fsm.template_fsm_response_thankyou",
            {'answer': answer.upper()}
        )
