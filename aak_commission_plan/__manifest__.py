# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK Commission Plan",
    "summary": "This module does initial configuration for commission plans for sales person.",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["sale_commission", "aak_base_data"],
    "data": [
        'data/commission_plan_data.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}