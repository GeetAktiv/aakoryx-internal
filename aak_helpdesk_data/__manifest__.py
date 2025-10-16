# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Helpdesk App - Data",
    "summary": "This module does initial configuration on Helpdesk app",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["aak_base_data", "aak_sales_data", "helpdesk", "helpdesk_fsm", "helpdesk_repair"],
    "data": [
        "data/helpdesk_team_data.xml",
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
