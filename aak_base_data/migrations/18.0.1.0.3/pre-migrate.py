# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def migrate(cr, version):
    """
    Migration script to temporarily unlock survey.group_survey_user
    and allow XML updates if needed.
    """
    # Use SUPERUSER_ID to avoid access issues
    cr.execute("""
        UPDATE ir_model_data
        SET noupdate = FALSE
        WHERE module = 'survey' AND name = 'group_survey_user';
    """)
