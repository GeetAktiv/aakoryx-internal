# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Base App - Data",
    "summary": "This module does initial configuration on database",
    "version": "18.0.1.0.3",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["base","industry_fsm", "survey"],
    "data": [
        "data/ir_module_category_data.xml",
        "data/res_partner_data.xml",
        "data/res_company_data.xml",
        "data/res.partner.csv",
        "data/res.users.csv",
        "data/res_users_data.xml",
        "security/fsm_security.xml",
        "security/survey_security.xml",
        "security/service_team_groups.xml",
    ],
    "assets": {
    },
    "application": False,
    "installable": True,
    "pre_init_hook": "_unlock_survey_group",
    "post_init_hook": "_relock_survey_group",
}
