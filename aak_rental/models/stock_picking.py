# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _should_create_auto_return(self, linked_sales):
        """
        Override hook:
        Create return only if the sale order is rental,
        fallback to normal sales logic for non-rental orders.
        """
        if linked_sales.filtered(lambda so: so.is_rental_order):
            return True
        # fallback to sales logic
        return super()._should_create_auto_return(linked_sales)
