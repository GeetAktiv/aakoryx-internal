# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Activity Done Acknowledgement",
    "summary": """
        This module sends acknowledgement email to customer
        that call was done.
        """,
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["base_automation", "crm"],
    "data": [
        "data/mail_template_data.xml",
        "data/base_automation_data.xml",
        "data/ir_actions_server_data.xml",
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
