# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(
        selection_add=[
            ('draft', "Quotation"),
            ('sent', "Quotation Sent"),
            ('reviewed', 'Reviewed'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('sale', "Sales Order"),
            ('cancel', "Cancelled"),
        ],
        ondelete={
            'reviewed': 'set default',
            'approved': 'set default',
            'rejected': 'set default',
        }
    )

    def copy(self, default=None):
        """Preserve component hierarchy of order lines when duplicating."""
        self.ensure_one()
        default = dict(default or {})

        # Step 1: Copy the order
        new_order = super().copy(default=default)

        # Step 2: Build mapping { old_line_id: new_line_id }
        line_mapping = {
            old_line.id: new_line.id
            for old_line, new_line in zip(self.order_line, new_order.order_line)
        }

        # Step 3: Re-link parent-child hierarchy
        for old_line in self.order_line:
            if old_line.comp_parent_line_id:
                new_child = new_order.order_line.filtered(
                    lambda l: l.id == line_mapping.get(old_line.id)
                )
                new_parent_id = line_mapping.get(old_line.comp_parent_line_id.id)
                if new_child and new_parent_id:
                    new_child.comp_parent_line_id = new_parent_id

        return new_order

    def action_confirm(self):
        """Override sale order confirmation to mark pickings as generated from SO"""
        res = super().action_confirm()
        # All pickings generated from this order
        pickings = self.picking_ids.filtered(lambda p: not p.is_so_generated)
        for picking in pickings:
            # Update picking context and field
            picking.with_context(from_sale_order=True).write({'is_so_generated': True})
        return res

    def action_check_availability(self):
        """
            Check stock availability for all products in the sales order.

            This method validates whether sufficient quantities are available in stock
            for each product line in the order. It performs the following steps:
              - Prefetches the available quantity (`qty_available`) for all products in the order.
              - Iterates through each order line and compares the available stock with the required quantity.
              - If any product has insufficient stock, it raises a `UserError` listing all affected products
                along with their required and available quantities.
              - If all products have sufficient stock, the order state is updated to `'reviewed'`.

            Raises:
                UserError: If one or more products have insufficient available quantity.

            Returns:
                None
        """
        for order in self:
            insufficient_lines = []
            products = order.order_line.mapped('product_id')
            products.read(['qty_available'])  # prefetch quantities

            for line in order.order_line:
                if line.product_id.type == 'consu' and line.product_id.qty_available < line.product_uom_qty:
                    insufficient_lines.append(
                        f"{line.product_id.display_name} (Required: {line.product_uom_qty}, Available: {line.product_id.qty_available})"
                    )

            if insufficient_lines:
                message = _("Insufficient stock for:\n") + "\n".join(insufficient_lines)
                raise UserError(message)
            else:
                order.state = 'reviewed'
