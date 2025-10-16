# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    service_type = fields.Selection(
        selection=[
            ("security", "Security"),
            ("two_way_radio", "2-Way Radio"),
            ("wan_tower", "WAN / Tower"),
        ],
        string="Service Type",
        help="Category of service the sales team is handling.",
    )
