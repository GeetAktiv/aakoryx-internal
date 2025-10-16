# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Auto-generated Work Ticket ID
    work_ticket_id = fields.Char(
        string='Work Ticket ID',
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('project.task.work.ticket')
    )
    service_type = fields.Selection(
        [
            ('security', 'Security'),
            ('two_way_radio', '2-Way Radio'),
            ('wan_tower', 'WAN/Tower'),
            ('other', 'Other'),
        ],
        string='Service Type',
        required=True,
        help='Category of work, e.g. Security, 2-Way Radio, WAN/Tower'
    )
    bom_id = fields.Many2one(
        'mrp.bom',
        string='Bill of Materials',
        required=True,
        help='Complete list of required items for this work order.'
    )
    technical_requirements = fields.Text(
        string='Technical Requirements',
        required=True,
        help='Specifications, configurations, or setup details for this task.'
    )
    fcc_license = fields.Char(
        string='FCC Licensing',
        required=False,
        help='Licensing status and details, e.g., GMRS license verified, tower permit pending.'
    )
    scheduled_datetime = fields.Datetime(
        string='Scheduled Date/Time',
        help='Date and time when the work is scheduled to be performed.'
    )
    vehicle_assignment_id = fields.Many2one(
        'fleet.vehicle',
        string='Vehicle Assignment',
        required=False,
        help='Assigned service vehicle for tower or large-scale projects, e.g., Heavy Truck #3.'
    )
    vehicle_information = fields.Char(
        string='Vehicle Information',
        help='Vehicle involved in the installation, e.g., 2025 Ford F-150, VIN #12345.'
    )
    special_instructions = fields.Text(
        string='Special Instructions',
        help='Additional notes or requirements for technicians, e.g., customer requires safety briefing.'
    )
    reference_documents = fields.Many2many(
        'ir.attachment',
        string='Reference Documents',
        help='Attach site surveys, quotations, manuals, or related documents.'
    )
    product_ids = fields.Many2many(
        comodel_name='product.product',
        string='Products',
        help='Products linked to this task based on related sale order lines.'
    )
    sol_products_count = fields.Integer(
        string='Products Count',
        compute='_compute_sol_products_count',
        help='Total count of products linked to this task.'
    )

    @api.depends('product_ids')
    def _compute_sol_products_count(self):
        """Compute total number of linked products.

        :return: None
        :rtype: NoneType
        """
        self.sol_products_count = len(self.product_ids)

    def action_fsm_view_sol_products(self):
        """Open the list of products linked to the task.

        :return: Action to open product view filtered by related products.
        :rtype: dict

        :warning: Will raise no error if no product exists, simply opens an empty view.
        """
        self.ensure_one()
        product_ids = self.product_ids.ids

        action = self.env.ref('product.product_normal_action').read()[0]
        action.update({
            'domain': [('id', 'in', product_ids)],
            'context': {'create': False},
        })
        return action

    def action_open_related_vehicle(self):
        """
        Opens the form view of the assigned vehicle.

        :return: Action dictionary to open the related vehicle form view.
        :rtype: dict
        """
        self.ensure_one()
        if not self.vehicle_assignment_id:
            return {'type': 'ir.actions.act_window_close'}

        return {
            'name': 'Vehicle',
            'type': 'ir.actions.act_window',
            'res_model': 'fleet.vehicle',
            'res_id': self.vehicle_assignment_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
