# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import models, fields, api


class FCCLicensing(models.Model):
    _name = 'fcc.licensing'
    _description = 'FCC Licensing'
    _rec_name = 'application_for'

    lic_type = fields.Selection([
        ('business_brand', 'Business Brand (Part 90)'),
        ('special_temporary_authority', 'Special Temporary Authority'),
        ('license_modification', 'License Modification'),
    ], string='License Type', required=True)
    application_for = fields.Char(string='Application For', required=True)
    lic_file = fields.Binary('License File', reaonly=True)
    lic_file_name = fields.Char('License File Name')
