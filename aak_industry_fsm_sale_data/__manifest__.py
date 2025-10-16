# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Field Service - Sale App - Data",
    "summary": "This module does initial configuration on database",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["aak_sales_data", "industry_fsm_sale"],
    "data": [
        "data/product_product_data.xml",
    ],
    "assets": {
    },
    "post_init_hook": "_post_data_process",
    "application": False,
    "installable": True
}
