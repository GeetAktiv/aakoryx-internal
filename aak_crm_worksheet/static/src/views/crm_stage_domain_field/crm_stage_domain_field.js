/** @odoo-module **/

import { registry } from "@web/core/registry";
import { DomainField, domainField } from '@web/views/fields/domain/domain_field';


export class CRMStageDomainField extends DomainField {
    static template = "aak_crm_worksheet.CRMStageDomainField";
}

export const crmStageDomainField = {
    ...domainField,
    component: CRMStageDomainField,
};

registry.category("fields").add("crm_stage_domain_field", crmStageDomainField);
