# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "AAK Sales",
    "summary": "This module does initial configuration for sales",
    "version": "18.0.1.0.3",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["sale_management", "stock"],
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/sale_components_views.xml',
        'views/component_list_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/sale_menus.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
