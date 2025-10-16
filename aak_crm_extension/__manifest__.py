# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAk CRM Extension",
    "summary": "AAk CRM Extension",
    "version": "18.0.1.1.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["crm"],
    "data": [
        "data/ir_sequence.xml",
        'views/crm_lead_views.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
