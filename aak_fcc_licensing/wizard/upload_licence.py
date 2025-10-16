# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from markupsafe import Markup
from odoo import models, fields, api, _


class UploadLicence(models.TransientModel):
    _name = 'upload.licence'
    _description = 'Upload Licence'

    lic_type = fields.Selection([
        ('business_brand', 'Business Brand (Part 90)'),
        ('special_temporary_authority', 'Special Temporary Authority'),
        ('license_modification', 'License Modification'),
    ], string='License Type', required=True)
    application_for = fields.Char(string='Application For', reaonly=True)
    lic_file = fields.Binary('License File', reaonly=True)
    lic_file_name = fields.Char('License File Name')

    @api.onchange('lic_type')
    def _onchange_lic_type(self):
        """Auto-fill license details based on the latest matching FCC license.

        :return: None
        :rtype: NoneType
        """
        fcc_licensing = self.env['fcc.licensing'].search(
            [('lic_type', '=', self.lic_type)],
            order='id desc',
            limit=1
        )
        if fcc_licensing:
            self.application_for = fcc_licensing.application_for
            self.lic_file = fcc_licensing.lic_file
            self.lic_file_name = fcc_licensing.lic_file_name
        else:
            self.application_for = ''
            self.lic_file = ''
            self.lic_file_name = ''

    def action_upload_licence(self):
        """Upload license data and log details in related Sale Order.

        Adds a chatter log entry in the active sale order including all
        uploaded license details such as license type, application for,
        file name, and timestamp.

        :return: Action to close the wizard window
        :rtype: dict

        :warning: This action assumes it is triggered from a Sale Order record.
        """
        self.ensure_one()
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))

        if not sale_order:
            return {'type': 'ir.actions.act_window_close'}

        # Use safe HTML markup for chatter log
        msg = Markup("<b>%s</b><ul>") % _("License Uploaded")
        msg += Markup("<li>%s: %s</li>") % (
            _("License Type"),
            dict(self._fields['lic_type'].selection).get(self.lic_type, '-')
        )
        msg += Markup("<li>%s: %s</li>") % (_("Application For"), self.application_for or '-')
        msg += Markup("<li>%s: %s</li>") % (_("License File Name"), self.lic_file_name or '-')
        msg += Markup("</ul>")

        if self.lic_file:
            attachment = self.env['ir.attachment'].create({
                'name': self.lic_file_name or 'license_file',
                'res_model': 'sale.order',
                'res_id': sale_order.id,
                'type': 'binary',
                'datas': self.lic_file,
                'mimetype': 'application/octet-stream',
            })
            sale_order.message_post(
                body=msg,
                message_type='comment',
                subtype_xmlid='mail.mt_note',
                attachment_ids=[attachment.id]
            )
        else:
            sale_order.message_post(
                body=msg,
                message_type='comment',
                subtype_xmlid='mail.mt_note'
            )

        return {'type': 'ir.actions.act_window_close'}
