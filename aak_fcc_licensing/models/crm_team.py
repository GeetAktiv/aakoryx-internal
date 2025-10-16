# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    fcc_licence_required = fields.Boolean(
        string="FCC Licence Required?",
        help="Check if this sales team requires FCC licensing."
    )
