# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SaleComponents(models.TransientModel):
    _name = "sale.component"
    _description = "BOM Inventory"

    product_id = fields.Many2one('product.product', string="Product")
    component_id = fields.Many2one('component.list', string="BOM Inventory")
    quantity = fields.Float(string="Quantity", default="1.0")
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company, readonly=True)

    def action_add_component(self):
        """Entry point for adding product + components to Sale Order"""
        self.ensure_one()

        sale_order = self._get_sale_order()
        product = self._get_product_variant()

        # create main product line first (must be record, not dict)
        main_product_vals = self._prepare_main_product_line(sale_order, product)
        main_product = self.env["sale.order.line"].create(main_product_vals)
        lines_to_create = []

        # add section line
        lines_to_create.append(self._prepare_section_line(sale_order, main_product))

        # add component lines
        lines_to_create += self._prepare_component_lines(sale_order, main_product)

        # batch create for performance
        if lines_to_create:
            self.env["sale.order.line"].create(lines_to_create)

        return True

    # -----------------------------
    # Helpers
    # -----------------------------

    def _get_sale_order(self):
        order_id = self.env.context.get("active_id")
        sale_order = self.env["sale.order"].browse(order_id)
        if not sale_order:
            raise ValidationError(_("No active Sale Order found."))
        return sale_order

    def _get_product_variant(self):
        product = self.product_id
        if not product:
            raise ValidationError(_("Product must have at least one variant."))
        return product

    def _prepare_main_product_line(self, sale_order, product):
        return {
            "order_id": sale_order.id,
            "product_id": product.id,
            "product_uom_qty": self.quantity,
        }

    def _prepare_section_line(self, sale_order, main_product):
        return {
            "order_id": sale_order.id,
            "name": f"{self.product_id.name} - Components",
            "display_type": "line_section",
            "comp_parent_line_id": main_product.id
        }

    def _prepare_component_lines(self, sale_order, main_product):
        return [
            {
                "order_id": sale_order.id,
                "product_id": component.product_id.id,
                "product_uom_qty": component.quantity * self.quantity,
                "comp_parent_line_id": main_product.id,
                "component_factor": component.quantity
            }
            for component in self.component_id.product_components_ids
            if component.product_id
        ]
