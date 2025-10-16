# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CRMLeadAutoActivity(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def action_create_daily_activities(self):
        """Create a 'Call' activity for leads created today."""

        today = fields.Date.context_today(self)
        start_of_day = fields.Datetime.to_datetime(today)
        end_of_day = fields.Datetime.add(start_of_day, days=1, seconds=-1)

        # stage_id = self.env['crm.stage'].search([()])

        leads = self.search([
            ('create_date', '>=', start_of_day),
            ('create_date', '<=', end_of_day),
            ('active', '=', True),
        ])
        if not leads:
            _logger.info("No leads created today — skipping.")
            return

        activity_type = self.env['mail.activity.type'].search([
            ('category', '=', 'phonecall')
        ], limit=1)

        if not activity_type:
            skipped_leads = ", ".join(leads.mapped('name'))
            _logger.warning(
                "No 'Phone Call' activity type found — skipping activity creation for leads: %s",
                skipped_leads or "None"
            )
            return

        for lead in leads:
            user_id = lead.user_id.id or self.env.user.id
            lead.activity_schedule(
                activity_type_id=activity_type.id,
                summary='Initial customer contact activity',
                user_id=user_id,
                date_deadline=today,
            )

        _logger.info("Scheduled 'Call' activities for %d leads.", len(leads))
