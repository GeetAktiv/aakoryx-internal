# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # Flag to identify if picking was generated from a Sale Order
    is_so_generated = fields.Boolean("Is SO Generated", default=False)
    auto_return_created = fields.Boolean(default=False)

    @api.model_create_multi
    def create(self, vals_list):
        """
        Override to automatically mark pickings created from Sale Orders.

        If the picking is created in a context containing `from_sale_order=True`,
        it sets the `is_so_generated` flag to True for all created pickings.

        :param list vals_list: List of dictionaries containing field values for new records.
        :return: Newly created stock.picking records.
        :rtype: recordset
        """
        from_so = bool(self.env.context.get("from_sale_order"))
        for vals in vals_list:
            vals["is_so_generated"] = from_so
        return super().create(vals_list)

    def copy(self, default=None):
        """
        Override to reset `is_so_generated` flag when duplicating a picking.

        Ensures that the duplicate picking is not treated as originating
        from a sale order.

        :param dict default: Optional dictionary of default values to override.
        :return: Duplicated stock.picking record.
        :rtype: record
        """
        default = dict(default or {})
        default['is_so_generated'] = False  # Reset SO flag on duplicate
        return super().copy(default)

    def button_validate(self):
        """
        Override the standard validation behavior to trigger automatic return creation.

        Automatically generates a return picking for equipment products when:
          - The picking is an outgoing delivery (`picking_type_code == 'outgoing'`), and
          - It originates from a sale order (`is_so_generated=True`) that is not a rental, OR
          - It is a backorder picking that contains equipment products.

        The method also prevents duplicate return creation unless it's a valid backorder case.

        :return: Result of the parent `button_validate` method.
        :rtype: any
        """
        res = super().button_validate()

        if self.env.context.get("skip_auto_return"):
            return res

        for picking in self.filtered(lambda p: p.picking_type_code == "outgoing"):
            linked_sales = picking.sale_id or self.env['sale.order']

            # Filter to identify if any move in the picking belongs to equipment product
            has_equipment = any(picking.move_ids.filtered(lambda m: m.product_id.is_equipment))

            # CASE 1: Backorder picking → allow auto return only if it contains equipment products
            if picking.backorder_id and has_equipment and picking._should_create_auto_return(linked_sales):
                picking._auto_create_return_for_equipment()
                picking.auto_return_created = True
                continue  # move to next picking

            # CASE 2: Normal case → only if not already processed
            if (
                    not picking.auto_return_created
                    and picking.is_so_generated
                    and picking._should_create_auto_return(linked_sales)
                    and has_equipment
            ):
                picking._auto_create_return_for_equipment()
                picking.auto_return_created = True

        return res

    def _should_create_auto_return(self, linked_sales):
        """
        Determine whether an automatic return should be created.

        Default behavior: returns True for all sale orders that are not rental orders.

        :param recordset linked_sales: sale.order recordset linked to the picking.
        :return: True if auto-return should be created, else False.
        :rtype: bool
        """
        return bool(linked_sales.filtered(lambda so: not so.is_rental_order))

    def _auto_create_return_for_equipment(self):
        """
        Automatically create a return picking for equipment products.
        Works safely with backorders without resetting previous return quantities.
        """
        self.ensure_one()

        # Filter only equipment moves
        equipment_moves = self.move_ids.filtered("product_id.is_equipment")
        if not equipment_moves:
            return

        # Explicitly detach from original move chain to avoid quantity recalculation
        return_wizard = self.env["stock.return.picking"].create({
            "picking_id": self.id,
            "product_return_moves": [
                (0, 0, {
                    "product_id": move.product_id.id,
                    "quantity": move.quantity,
                    "move_id": move.id,
                }) for move in equipment_moves
            ],
        })

        # Create the return picking without relinking old moves
        new_return = return_wizard.with_context(skip_auto_return=True)._create_return()

        # Fix: Clear `move_orig_ids` to prevent chain updates affecting old returns
        for new_move in new_return.move_ids:
            new_move.move_orig_ids = False

        # Post a message for traceability
        self.message_post(body=_(
            "New Return Order has been created: %(picking_link)s",
            picking_link=new_return._get_html_link()
        ))
