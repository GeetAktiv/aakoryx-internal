# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

import pytz
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ComponentList(models.Model):
    """
    Model to define reusable component lists for service type products.

    Features:
    - Assign a `product.product` as the base service product.
    - Add multiple component lines through `product.components`.
    - Maintain a unique name per list, automatically generated based on
      product name and creation datetime.
    - Track versioning: every modification (except direct version updates)
      automatically increments the version number.
    """
    _name = "component.list"
    _description = "Component List"

    name = fields.Char(string='Name', readonly=True, copy=False)
    product_id = fields.Many2one(
        'product.product',
        string='Service Product',
        help="Main service/product associated with this component list."
    )
    quantity = fields.Float(string="Quantity", default="1")
    product_components_ids = fields.One2many(
        'product.components',
        'component_id',
        string='Components',
        help="List of components linked to this configuration."
    )
    version = fields.Float(string="Version", readonly=True, default=0.0)
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company, readonly=True)

    @api.constrains('name')
    def _check_unique_name(self):
        """
        Constraint to ensure uniqueness of component list names.

        Raises:
            ValidationError: if another component list with the same `name`
            already exists in the database.
        """
        for record in self:
            if record.name:
                existing = self.search([
                    ('name', '=', record.name),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing:
                    raise ValidationError(_(
                        "A component list with the name '%s' already exists. "
                        "Please use a different name."
                    ) % record.name)

    @api.model_create_multi
    def create(self, vals_list):
        """
        Override create() to assign a meaningful unique name automatically.

        Logic:
        - Call super() to create records and assign `create_date`.
        - Build the `name` as: "<product_name> - <localized create_date>".
        - Timezone conversion is based on the current user's timezone.

        Returns:
            recordset: newly created `component.list` records.
        """
        res = super(ComponentList, self).create(vals_list)

        for rec in res:
            product_name = rec.product_id.name if rec.product_id else "Component"
            user_tz = pytz.timezone(self.env.user.tz or 'UTC')
            local_dt = rec.create_date.astimezone(user_tz)
            formatted_date = local_dt.strftime("%Y-%m-%d %H:%M:%S")
            rec.name = f"{product_name} - {formatted_date}"
        return res

    def write(self, vals):
        """
        Override write() to automatically increment version number on changes.

        Logic:
        - If any field other than `version` is being updated,
          increment the current version by 1.0.
        - This provides a simple versioning mechanism for tracking updates.

        Args:
            vals (dict): field values being updated.

        Returns:
            bool: result of super().write(vals)
        """
        if vals and not ("version" in vals and len(vals) == 1):
            for record in self:
                vals["version"] = record.version + 1.0
        return super(ComponentList, self).write(vals)
