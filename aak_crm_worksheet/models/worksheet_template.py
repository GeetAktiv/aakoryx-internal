# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

from odoo import api, models


class WorksheetTemplate(models.Model):
    _inherit = 'worksheet.template'

    @api.model
    def _default_crm_lead_template_fields(self):
        return [
            (0, 0, {
                'name': 'x_passed',
                'ttype': 'boolean',
                'field_description': 'Passed',
            })
        ]

    @api.model
    def _get_crm_lead_user_group(self):
        return self.env.ref('sales_team.group_sale_salesman')

    @api.model
    def _get_crm_lead_manager_group(self):
        return self.env.ref('sales_team.group_sale_manager')

    @api.model
    def _get_crm_lead_access_all_groups(self):
        return self.env.ref('sales_team.group_sale_manager')

    @api.model
    def _get_crm_lead_module_name(self):
        return 'aak_crm_worksheet'

    @api.model
    def _default_crm_lead_worksheet_form_arch(self):
        return """
            <form create="false" js_class="crm_stage_worksheet_validation">
                <sheet>
                    <h1 invisible="context.get('studio') or context.get('default_x_crm_lead_id')">
                        <field name="x_crm_lead_id"/>
                    </h1>
                    <group>
                        <group>
                            <field name="x_comments"/>
                            <field name="x_passed"/>
                        </group>
                        <group>
                        </group>
                    </group>
                </sheet>
            </form>
        """
