import { patch } from "@web/core/utils/patch";
import { Record } from "@web/model/relational_model/record";

patch(Record.prototype, {
    async _save({ reload = true, onError, nextId } = {}) {
        if (this.resModel === 'crm.lead' &&
            "stage_id" in this._changes
        ) {
            const worksheet_avail = await this.model.orm.call(
                'crm.stage',
                'search_count',
                [[['id', '=', this._changes.stage_id[0]], ['worksheet_template_id', '!=', false]]]
            );
            if (!worksheet_avail) {
                return super._save(...arguments);
            }
            const action = await this.model.orm.call('crm.lead', 'action_crm_lead_worksheet', [this.resId, this._changes.stage_id[0], this._getChanges()]);
            this.model.action.doAction(action);
            this._changes = {};
            return super._save(...arguments);
        }
        else {
            return super._save(...arguments);
        }
    }
});
