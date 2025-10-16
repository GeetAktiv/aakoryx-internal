# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

{
    "name": "Product - Data",
    "summary": "This module adds service/rental/consumable/storable products.",
    "version": "18.0.1.0.0",
    "author": "AAKORYX",
    "website": "https://www.aakoryx.com/",
    "license": "OPL-1",
    "depends": ["sale_renting", "sale_subscription", "sale_timesheet", "stock"],
    "data": [
        'data/product.category.csv',
        'data/2wayparts/product.template.csv',
        'data/kenwood/product.template.csv',
        'data/kenwood/lmrdealer/product.template.csv',
        'data/motorola/commercial/radio/product.template.csv',
        'data/motorola/commercial/radio/product_template_data.xml',
        'data/motorola/commercial/radio/product.attribute.csv',
        'data/motorola/commercial/radio/product.attribute.value.csv',
        'data/motorola/commercial/radio/product.template.attribute.line.csv',
        'data/motorola/commercial/radio/product_template_attribute_value_data.xml',
        'data/motorola/commercial/radio/product.template.attribute.exclusion.csv',
        'data/motorola/commercial/radio/product_product_data.xml',
        'data/motorola/commercial/accessories/product.template.csv',
        'data/motorola/professional/radio/product.template.csv',
        'data/motorola/professional/accessories/product.template.csv',
        'data/product_data.xml',
        'data/res_groups_data.xml',
    ],
    "assets": {
    },
    "application": False,
    "installable": True
}
