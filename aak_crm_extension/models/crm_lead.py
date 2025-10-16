# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    lead_uid = fields.Char(
        string="Lead ID",
        required=True,
        readonly=False,
        copy=False,
        index='trigram',
        help="Auto-generated unique identifier for the lead (e.g. LEAD-2025-001).",
        default=lambda self: self.env['ir.sequence'].next_by_code('crm.lead.lead_uid')
    )
    service_type = fields.Selection(
        selection=[
            ("security", "Security"),
            ("two_way_radio", "2-Way Radio"),
            ("wan_tower", "WAN / Tower"),
        ],
        string="Service Type",
        required=True,
        help="Category of service the customer is interested in.",
    )
    initial_request = fields.Text(
        string="Initial Request",
        required=True,
        help="Brief description of the customer's needs or project request.",
    )

    @api.constrains("email_from", "phone", "mobile", "street")
    def _check_contact_information(self):
        """Ensure at least one contact method is provided.

        :raises ValidationError: If all contact fields are empty.
        :warning: At least one of email, phone, mobile, or address must be filled.
        """
        for lead in self:
            if not any([lead.email_from, lead.phone, lead.mobile, lead.street]):
                raise ValidationError(
                    _(
                        "Please provide at least one contact detail: "
                        "Email, Phone, Mobile, or Address."
                    )
                )
