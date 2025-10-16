# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, fields, models, _


class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    vehicle_id_custom = fields.Char(
        string="Vehicle ID",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New')
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        help='Owner of the vehicle'
    )
    make_id = fields.Many2one(
        'fleet.vehicle.model.brand',
        string='Make',
        required=True,
        help='Vehicle manufacturer (e.g. Ford, Toyota, Nissan)'
    )
    previous_installations = fields.Text(
        string='Previous Installations',
        help='History of radio installations or previous setups'
    )
    radio_model = fields.Char(
        string='Radio Model',
        help='Current or planned radio model installed in the vehicle'
    )
    installation_location = fields.Char(
        string='Installation Location',
        help='Where the radio is mounted (e.g. Dashboard, Center Console, etc.)'
    )
    antenna_type = fields.Char(
        string='Antenna Type',
        help='Type of antenna used (e.g. Roof-mounted, Magnetic, etc.)'
    )
    photo_ids = fields.Many2many(
        'ir.attachment',
        'fleet_vehicle_ir_attachments_rel',
        'vehicle_id',
        'attachment_id',
        string='Photos',
        help='Attach multiple images or files related to the vehicle or installation'
    )

    @api.model
    def create(self, vals):
        """Automatically assign Vehicle ID using ir.sequence"""
        if vals.get('vehicle_id_custom', _('New')) == _('New'):
            # Generate a new sequence number based on your XML definition
            seq = self.env['ir.sequence'].next_by_code('fleet.vehicle.custom') or _('New')
            vals['vehicle_id_custom'] = seq
        return super(FleetVehicle, self).create(vals)
