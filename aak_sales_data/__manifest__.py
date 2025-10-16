# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK Sales Data",
    "summary": "This module does initial configuration for Project and Product.",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["industry_fsm_sale", "product", 'aak_base_data'],
    "data": [
        'data/project_data.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
