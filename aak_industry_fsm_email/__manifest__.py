# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK Field Service E-Mail",
    "summary": "This module provides functionality sent an email to client while making Field Service to 'Mark As Done'.",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["industry_fsm"],
    "data": [
        "data/email_template_data.xml",
        "views/product_template_views.xml",
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
