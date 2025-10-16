# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, api


class SetVisitDate(models.TransientModel):
    """Wizard to select a concrete visit date and notify the customer."""
    _name = 'set.visit.date'
    _description = 'Set Visit Date Wizard'

    visit_date = fields.Date(string="Visit Date", required=True)
    show_alert = fields.Boolean(string="Show Alert", compute="_compute_show_alert")

    @api.depends('visit_date')
    def _compute_show_alert(self):
        """Show warning if selected visit date is outside the planned window."""
        for wizard in self:
            task = self.env['project.task'].browse(self.env.context.get('active_id'))
            wizard.show_alert = False

            if not (wizard.visit_date and task and task.planned_date_start and task.date_deadline):
                continue

            # Convert datetime fields to date (user timezone aware)
            start_date = fields.Datetime.context_timestamp(wizard, task.planned_date_start).date()
            end_date = fields.Datetime.context_timestamp(wizard, task.date_deadline).date()
            visit_date = wizard.visit_date

            # Show alert if visit date is outside planned range
            if not (start_date <= visit_date <= end_date):
                wizard.show_alert = True

    def action_confirm(self):
        """
        Send the visit date email to the customer (does not update task dates).
        """
        self.ensure_one()
        task = self.env['project.task'].browse(self._context.get('active_id'))
        if not task:
            return {'type': 'ir.actions.act_window_close'}

        try:
            template = self.env.ref('aak_industry_fsm.mail_template_field_service_visit_date')
        except Exception:
            template = False

        if template:
            template.with_context(visit_date=self.visit_date).send_mail(task.id, force_send=True)

        return {'type': 'ir.actions.act_window_close'}
