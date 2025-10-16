# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "CRM Worksheet - Data",
    "summary": "Add worksheet and link to stages",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["aak_base_data","aak_crm_data","aak_crm_worksheet"],
    "data": [
        "data/worksheet_template_data.xml",
        "data/crm.stage.csv",
    ],
    "assets": {
        "web.assets_backend": [
        ],
    },
    "application": False,
    "installable": True
}
