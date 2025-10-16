# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Field Service Stock App - Data",
    "summary": "This module does initial configuration on Field Service Stock app",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["aak_product_data", "aak_sales"],
    "data": [
        "data/component.list.csv",
        "data/product.components.csv",
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
