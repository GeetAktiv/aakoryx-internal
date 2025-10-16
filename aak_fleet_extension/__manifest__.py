# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK Fleet Extension",
    "summary": "AAK Fleet Extension",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["fleet"],
    "data": [
        "data/ir_sequence.xml",
        'views/fleet_vehicle_views.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
