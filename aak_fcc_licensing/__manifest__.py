# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK FCC Licensing",
    "summary": "Manage FCC Licensing for Sales Teams",
    "version": "18.0.1.1.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "category": "sale",
    "depends": ["sale", "crm"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/upload_licence.xml",
        "views/fcc_licensing.xml",
        "views/crm_team_view_form.xml",
        "views/sale_order_view.xml",
    ],
    "assets": {},
    "application": False,
    "installable": True,
    "auto_install": False,
    "support": "support@aakoryx.com",
    "maintainer": "AAKORYX",
    "contributors": [
        "AAKORYX <office@aakoryx.com>"
    ],
}
