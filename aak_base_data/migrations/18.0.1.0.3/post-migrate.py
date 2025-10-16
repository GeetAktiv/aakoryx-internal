# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def migrate(cr, version):
    # restore noupdate
    cr.execute("""
        UPDATE ir_model_data
        SET noupdate = TRUE
        WHERE module = 'survey' AND name = 'group_survey_user';
    """)
