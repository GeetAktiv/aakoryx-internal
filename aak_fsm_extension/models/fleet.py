# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, fields, models

class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    vehicle_capacity_type = fields.Selection(
        selection=[
            ("light_truck", "Light truck (F-150 class)"),
            ("medium_truck", "Medium truck (F-250 class)"),
            ("heavy_truck", "Heavy truck (F-350 class)"),
            ("off_road", "Off-road capable truck"),
        ],
        string="Vehicle Capacity Type",
        required=True
    )
    tool = fields.Char(string="Tool")
    rack = fields.Char(string="Rack")
    capacity = fields.Char(string="Capacity")
