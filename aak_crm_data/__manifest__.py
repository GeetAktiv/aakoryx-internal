# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "CRM App - Data",
    "summary": "This module does initial configuration on CRM app",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["crm", "aak_base_data"],
    "data": [
        "data/crm_tag_data.xml",
        "data/crm_team_data.xml",
        "data/crm.stage.csv",
        "data/ir_config_parameter_data.xml",
        "data/res_groups_data.xml",
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
