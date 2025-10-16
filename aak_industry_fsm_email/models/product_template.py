# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):

    _inherit = "product.template"

    under_warranty = fields.Boolean(string="Under Warranty")
    warranty_date = fields.Date(string="Warranty Date")
