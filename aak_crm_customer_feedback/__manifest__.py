# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK CRM Customer Feedback",
    "summary": "Module for handling customer feedback surveys in CRM",
    "version": "18.0.1.1.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "category": "CRM",
    "depends": ["crm", "mail", "survey", "stock", "project"],
    "data": [
        'data/survey_data.xml',
        'data/crm_lead_cron.xml',
        'data/mail_template.xml',
    ],
    "assets": {},
    "application": False,
    "installable": True,
    "auto_install": False,
    "support": "support@aakoryx.com",
    "changelog": "CHANGELOG.md",
    "maintainer": "AAKORYX",
    "contributors": [
        "AAKORYX <office@aakoryx.com>"
    ],
}
