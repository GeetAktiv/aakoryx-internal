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
        """
        Extend the standard Sale Order confirmation process to:
          1. Link all products from sale order lines to the related tasks.
          2. Automatically assign a suitable vehicle to each task based on
             the number of sale order lines (component count).

        Vehicle assignment logic:
            - <10 components → Light truck (F-150 class)
            - 10–20 components → Medium truck (F-250 class)
            - >20 components → Heavy truck (F-350 class)

        :return: Result of the standard `action_confirm` method.
        :rtype: bool
        :warning: Requires `tasks_ids` on sale.order and
                  `vehicle_assignment_id` on project.task.
        """
        res = super().action_confirm()
        self._link_products_to_tasks(self)

        if self.tasks_ids:
            line_count = len(self.order_line.mapped("product_id"))

            if line_count < 10:
                vehicle_type = "light_truck"
            elif 10 <= line_count <= 20:
                vehicle_type = "medium_truck"
            elif line_count > 20:
                vehicle_type = "heavy_truck"
            else:
                vehicle_type = None

            if vehicle_type:
                vehicle = self.env["fleet.vehicle"].search(
                    [("vehicle_capacity_type", "=", vehicle_type)],
                    order="id desc",
                    limit=1,
                )
                if vehicle:
                    self.tasks_ids.write({"vehicle_assignment_id": vehicle.id})
        return res
