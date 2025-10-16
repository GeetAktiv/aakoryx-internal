# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK Industry FSM",
    "summary": "Email notification with Yes/No button for Planned Date updates in FSM.",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "category": "Services/Field Service",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "mail",
        "industry_fsm",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/mail_template.xml",
        "wizard/set_visit_date_view.xml",
        "views/fsm_templates.xml",
        "views/project_task_inherit_view.xml",
    ],
}
