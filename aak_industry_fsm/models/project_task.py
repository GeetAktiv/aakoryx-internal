# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, models


class ProjectTask(models.Model):
    """Extend project.task to email customers about planned date windows."""
    _inherit = "project.task"

    def _get_schedule_template(self):
        """Return the schedule-date mail template or False."""
        try:
            return self.env.ref("aak_industry_fsm.mail_template_field_service_schedule_date")
        except Exception:
            return False

    @api.model_create_multi
    def create(self, vals_list):
        """
        On creation, if a task has a planned end (date_deadline),
        send schedule window email to the customer.

        Output/behavior kept identical.
        """
        records = super().create(vals_list)
        template = self._get_schedule_template()
        if template:
            for rec in records:
                if rec.date_deadline:
                    template.send_mail(rec.id, force_send=True)
        return records

    def write(self, vals):
        """
        On update, when the planned end (date_deadline) changes,
        send schedule window email to the customer.

        Output/behavior kept identical.
        """
        res = super().write(vals)
        if "date_deadline" in vals:
            template = self._get_schedule_template()
            if template:
                for rec in self:
                    if rec.date_deadline:
                        template.send_mail(rec.id, force_send=True)
        return res
