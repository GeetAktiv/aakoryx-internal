# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _link_products_to_tasks(self, order):
        """Link all products from sale order lines to each related task.

        :param order: Sale order being confirmed.
        :type order: recordset (sale.order)
        :return: None
        :rtype: None
        :warning: Requires `tasks_ids` (on sale.order) and
                  `product_ids` (on project.task) to exist.
        """
        if not order.tasks_ids or not order.order_line:
            return

        # Get all unique products from sale order lines
        products = order.order_line.mapped('product_id')

        # Link those products to all tasks connected to this order
        order.tasks_ids.write({
            'product_ids': [(6, 0, products.ids)],
        })

    def action_confirm(self):
        """Extend Sale Order confirmation to link products to tasks.

        :return: Standard action_confirm result
        :rtype: bool
        """
        res = super().action_confirm()
        self._link_products_to_tasks(self)
        return res
