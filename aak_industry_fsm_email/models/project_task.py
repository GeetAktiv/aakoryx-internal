# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def action_fsm_validate(self, stop_running_timers=False):
        res = super().action_fsm_validate(stop_running_timers)
        template = self.env.ref('aak_industry_fsm_email.task_warranty_email_template')  # XML ID of template

        for task in self:
            # Make sure the task is linked to a sale order
            if task.sale_order_id:
                # Get sale order lines with products that have warranty_date
                warranty_lines = task.sale_order_id.order_line.filtered(lambda l: l.product_id.warranty_date)
                if warranty_lines and template and task.partner_id.email:
                    # Pass the warranty_lines to the template using context
                    template.with_context(warranty_lines=warranty_lines).send_mail(task.id, force_send=True)

        return res
