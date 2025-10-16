# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

def _unlock_survey_group(env):
    """
    Temporarily unlock the 'survey.group_survey_user' record
    by setting noupdate=False so it can be updated via XML.
    """
    env.cr.execute("""
        UPDATE ir_model_data
        SET noupdate = FALSE
        WHERE module = 'survey' AND name = 'group_survey_user';
    """)

def _relock_survey_group(env):
    """
    Restore noupdate=True for the record after modification.
    """
    env.cr.execute("""
        UPDATE ir_model_data
        SET noupdate = TRUE
        WHERE module = 'survey' AND name = 'group_survey_user';
    """)

