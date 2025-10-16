# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Field Service Extension",
    "summary": "Field Service Extension",
    "version": "18.0.1.3.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["industry_fsm", "mrp", "sale", "industry_fsm_stock", "fleet"],
    "data": [
        "data/ir_sequence.xml",
        "data/project_task_type_data.xml",
        'views/project_task_views.xml',
        'views/fleet_vehicle_views.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
