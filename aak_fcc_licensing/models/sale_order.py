# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fcc_licence_required = fields.Boolean(
        string="FCC Licence Required?",
        related='team_id.fcc_licence_required',
        help="Check if this sales team requires FCC licensing."
    )
