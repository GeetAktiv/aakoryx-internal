# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models


class ProductComponents(models.Model):
    _name = "product.components"
    _description = "Product Component"

    component_id = fields.Many2one('component.list', string='Component')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default="1.0")
