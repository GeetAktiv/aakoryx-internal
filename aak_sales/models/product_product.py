# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    """
    Extension of `product.product` to introduce equipment classification.

    Features:
    - Adds a boolean field `is_equipment` to distinguish equipment from salable products.
    - Ensures that a product cannot be both `salable` (`sale_ok=True`) and `equipment`.
    - Automatically disables `sale_ok` if `is_equipment` is enabled, both on create and write.
    """
    _inherit = "product.product"

    # is_equipment = fields.Boolean(string='Equipment')

    @api.constrains("is_equipment", "sale_ok", "rent_ok")
    def _check_equipment_and_sale_ok(self):
        """
        Constraint: prevent a product from being both salable and equipment.

        Raises:
            ValidationError: if both `is_equipment=True` and `sale_ok=True`
            are set for the same product.
        """
        for rec in self:
            if rec.is_equipment and rec.sale_ok:
                raise ValidationError(
                    _("A product cannot be both 'Salable' and 'Equipment'. "
                      "Please choose one option.")
                )
            if rec.is_equipment and rec.rent_ok:
                raise ValidationError(
                    _("A product cannot be both 'Rentable' and 'Equipment'. "
                      "Please choose one option.")
                )

    def write(self, vals):
        """
        Override write() to enforce mutual exclusivity of `is_equipment` and `sale_ok`.

        Logic:
        - If `is_equipment=True` is set during an update, automatically force
          `sale_ok=False` before saving.
        """
        if vals.get("is_equipment"):
            vals["sale_ok"] = False
            vals["rent_ok"] = False
        return super().write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        """
        Override create() to enforce mutual exclusivity of `is_equipment` and `sale_ok`.

        Logic:
        - For each new product being created, if `is_equipment=True` is set,
          automatically force `sale_ok=False`.
        """
        for vals in vals_list:
            if vals.get("is_equipment"):
                vals["sale_ok"] = False
                vals["rent_ok"] = False
        return super().create(vals_list)
