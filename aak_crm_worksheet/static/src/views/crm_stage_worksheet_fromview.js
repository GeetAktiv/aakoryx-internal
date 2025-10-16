/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";

class WorksheetValidationController extends FormController {
    static template = "aak_crm_worksheet.WorksheetValidationController";

    setup() {
        super.setup();
        this.orm = useService("orm");
    }

    async validate() {
        const context = this.model.root.context;
        await this.saveButtonClicked({ closable: !context['wizard_id'] });
        const record = this.model.root.data;
        const resp = await this.orm.call(
            "crm.lead",
            "action_worksheet_check",
            [record.x_crm_lead_id[0]],
            { context }
        );
        if (!resp[1]) {
            alert('Lead doesn\'t  qualify for next stage. Please fill worksheet correctly.');
        }
        this.model.action.doAction(resp[0]);
    }

    async discard() {
        await this.saveButtonClicked({ closable:false });
        await super.discard();
        const record = this.model.root.data;
        const context = this.model.root.context;
        const action = await this.orm.call(
            "crm.lead",
            "action_worksheet_discard",
            [record.x_crm_lead_id[0]],
            { context }
        );
        this.model.action.doAction(action);
    }
}

export const WorksheetValidationFormView = {
    ...formView,
    Controller: WorksheetValidationController,
};

registry.category("views").add("crm_stage_worksheet_validation", WorksheetValidationFormView);
