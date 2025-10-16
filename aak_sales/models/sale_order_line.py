# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    """
    Extension of sale.order.line to support product component hierarchy.

    Features:
    - Parent/Child relationship between sale order lines for components.
    - Each child line quantity is computed based on parent quantity * component factor.
    - Custom deletion logic to remove child/component lines and linked section lines
      when a parent line is deleted.
    """
    _inherit = 'sale.order.line'

    component_id = fields.Many2one('component.list', string="Component")
    comp_parent_line_id = fields.Many2one(
        "sale.order.line",
        string="Parent Line",
        index=True,
        copy=True
    )
    child_line_ids = fields.One2many(
        "sale.order.line",
        "comp_parent_line_id",
        string="Component Lines"
    )
    component_factor = fields.Float(string="Component Factor")

    def write(self, vals):
        """
        Override write() to update child line quantities when parent quantity changes.

        Logic:
        - If a parent line's `product_uom_qty` is updated,
          update each child line's `product_uom_qty`
          as: parent_qty * child.component_factor.
        """
        res = super().write(vals)
        for line in self:
            if not line.comp_parent_line_id and 'product_uom_qty' in vals:
                for child in line.child_line_ids:
                    child.product_uom_qty = line.product_uom_qty * child.component_factor
        return res

    @api.model_create_multi
    def create(self, vals_list):
        """
        Override create() to initialize child line quantities
        when a parent line is created.

        Logic:
        - For each newly created parent line,
          set its child line `product_uom_qty`
          as: parent_qty * child.component_factor.
        """
        lines = super().create(vals_list)
        for line in lines:
            if not line.comp_parent_line_id:
                for child in line.child_line_ids:
                    child.product_uom_qty = line.product_uom_qty * child.component_factor
        return lines

    def unlink(self):
        """
        Override unlink() to ensure component hierarchy is cleaned up.

        Logic:
        - Identify parent lines in the recordset.
        - Delete child lines linked to these parent lines via SQL for performance.
        - Delete section lines (`display_type = 'line_section'`) linked to parents.
        - Finally, delete the parent lines themselves.
        """
        if not self:
            return super().unlink()

        # Get IDs of all parent lines in the recordset
        parent_ids = self.filtered(lambda l: not l.comp_parent_line_id).ids

        if parent_ids:
            # Delete all child component lines linked to these parents
            self.env.cr.execute("""
                DELETE FROM sale_order_line
                WHERE comp_parent_line_id = ANY(%s)
            """, [parent_ids])

            # Delete all linked section lines
            self.env.cr.execute("""
                DELETE FROM sale_order_line
                WHERE comp_parent_line_id = ANY(%s)
                AND display_type = 'line_section'
            """, [parent_ids])

        # Finally, delete the parent lines themselves
        return super().unlink()
