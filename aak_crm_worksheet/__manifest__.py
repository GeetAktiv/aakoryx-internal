# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "CRM Stage Worksheet",
    "summary": "Link worksheet templates to CRM stages and quickly open them from leads",
    "version": "18.0.1.0.3",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["crm","worksheet"],
    "data": [
        "security/ir.model.access.csv",
        "security/crm_stage_security.xml",
        "views/crm_stage_views.xml",
        "views/worksheet_template_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "aak_crm_worksheet/static/src/model/**/*",
            "aak_crm_worksheet/static/src/views/**/*",
        ],
    },
    "application": False,
    "installable": True
}
