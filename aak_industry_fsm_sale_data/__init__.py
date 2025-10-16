# -*- coding: utf-8 -*-
# Part of Odoo, AAKORYX.
# See LICENSE file for full copyright & licensing details.

def _post_data_process(env):
    # LAUTTAMUS SECURITY, LLC - 2 Way Radio, project link to product
    env.ref('industry_fsm_sale.field_service_product').with_company(
        env.ref('aak_base_data.lauttamus_security_llc_company').id).project_id = env.ref('aak_sales_data.fsm_project_ls_2way_radio_service').id
    # LAUTTAMUS SECURITY, LLC - Answering Service, project link to product
    env.ref('aak_industry_fsm_sale_data.field_service_product_answering_service').with_company(
        env.ref('aak_base_data.lauttamus_security_llc_company').id).project_id = env.ref('aak_sales_data.fsm_project_ls_answering_service_service').id
    # LAUTTAMUS SECURITY, LLC - Paging, project link to product
    env.ref('aak_industry_fsm_sale_data.field_service_product_paging').with_company(
        env.ref('aak_base_data.lauttamus_security_llc_company').id).project_id = env.ref('aak_sales_data.fsm_project_ls_paging_service').id
    # LAUTTAMUS SECURITY, LLC - Security Service, project link to product
    env.ref('aak_industry_fsm_sale_data.field_service_product_security_service').with_company(
        env.ref('aak_base_data.lauttamus_security_llc_company').id).project_id = env.ref('aak_sales_data.fsm_project_ls_security_service_service').id
    # TRICONNEX, LP - 2 Way Radio, project link to product
    env.ref('industry_fsm_sale.field_service_product').with_company(
        env.ref('aak_base_data.triconnex_lp_company').id).project_id = env.ref('aak_sales_data.fsm_project_tc_2way_radio_service').id
    # TRICONNEX, LP - Answering Service, project link to product
    env.ref('aak_industry_fsm_sale_data.field_service_product_answering_service').with_company(
        env.ref('aak_base_data.triconnex_lp_company').id).project_id = env.ref('aak_sales_data.fsm_project_tc_answering_service_service').id
    # TRICONNEX, LP - Paging, project link to product
    env.ref('aak_industry_fsm_sale_data.field_service_product_paging').with_company(
        env.ref('aak_base_data.triconnex_lp_company').id).project_id = env.ref('aak_sales_data.fsm_project_tc_paging_service').id
    # TRICONNEX, LP - Security Service, project link to product
    env.ref('aak_industry_fsm_sale_data.field_service_product_security_service').with_company(
        env.ref('aak_base_data.triconnex_lp_company').id).project_id = env.ref('aak_sales_data.fsm_project_tc_security_service_service').id
