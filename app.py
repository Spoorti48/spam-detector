<!DOCTYPE html>
<!-- saved from url=(0047)https://github.com/s22223767-tech/spam-detector -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style><style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style>




  
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/light-f30be7a1f27bcb6b.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/dark-d9d99f8c9aa4fbfd.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-10373d2d112fc873.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-d0145171d79f94f6.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-1d2d2c4ffae648c4.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-11d6568044aeceeb.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-c38f22a98f01b293.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-f68e181a9067f808.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-c21a8c43bc3127eb.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-635d755c05590766.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-1abfbdc43c9465f6.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-5d5617ce453e2abb.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-9b6e5c8b7f02f5ae.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-1f2aa99a70f49a4b.css">

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-primitives-f9161d06200ae2dc.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-8fff84e4ecf561d1.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-6326a07d26552848.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/github-83d17778d5c4a394.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/repository-90ec7ed0aced8b41.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/code-6756960bc12d5d38.css">

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","action_yml_language_service","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_enable_snapshot_keyword","actions_image_version_event","actions_workflow_language_service","actions_workflow_language_service_allow_case_function","agent_session_retry_fetch_capi_on_401","alternate_user_config_repo","api_insights_show_missing_data_banner","arianotify_comprehensive_migration","batch_suggested_changes","billing_hard_budget_limits_for_licenses","billing_ui_budget_pagination_enabled","code_view_canvas_text_measurement","codeowners_validation_in_diff","codespaces_prebuild_region_target_update","coding_agent_model_selection","copilot_3p_agent_hovercards","copilot_agent_sessions_alive_updates","copilot_agent_task_list_v2","copilot_agent_task_submit_with_modifier","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_capi_error_response_telemetry","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_disable_model_picker_while_streaming","copilot_chat_enable_tool_call_logs","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_repository_picker","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_coding_agent_free_users_exp","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_raycast_logo","copilot_features_sql_server_logo","copilot_features_zed_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_job_result_preview","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_issue_list_show_more","copilot_mc_cli_resume_any_users_task","copilot_mission_control_use_task_api_outside_of_repos","copilot_org_policy_page_focus_mode","copilot_premium_request_quotas","copilot_redirect_header_button_to_agents","copilot_security_alert_assignee_options","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_pagination","copilot_spaces_server_side_menu_actions","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_stable_conversation_view","copilot_swe_agent_use_subagents","copilot_unconfigured_is_inherited","custom_instructions_file_references","custom_properties_consolidate_default_value_input","dashboard_indexeddb_caching","dashboard_lists_max_age_filter","dashboard_universe_2025","dashboard_universe_2025_feedback_dialog","dom_node_counts","enterprise_ai_controls","failbot_report_error_react_apps_on_page","fgpat_permissions_selector_redesign","file_finder_skip_debounce","flex_cta_groups_mvp","github_models_scheduled_hydro_events","global_nav_react","hide_groups_list_for_few_groups","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","initial_per_page_pagination_updates","issue_comment_pinning","issue_fields_compact_view","issue_fields_global_search","issue_fields_report_usage","issue_fields_timeline_events","issues_cca_assign_actor_with_agent","issues_dashboard_inp_optimization","issues_expanded_file_types","issues_index_semantic_search","issues_lazy_load_comment_box_suggestions","issues_react_auto_retry_on_error","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_custom_hpc_metric","issues_react_include_bots_in_pickers","issues_react_low_quality_comment_warning","issues_react_prohibit_title_fallback","issues_react_resource_metrics","issues_react_safari_scroll_preservation","issues_react_ui_feedback","issues_react_use_turbo_for_cross_repo_navigation","landing_pages_ninetailed","lifecycle_label_name_updates","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_display_button_config_menu","memex_grouped_by_edit_route","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","mission_control_retry_on_401","mission_control_use_body_html","oauth_authorize_clickjacking_protection","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","pr_sfv_new_diff_fetch","primer_react_css_has_selector_perf","projects_assignee_max_limit","pull_request_files_accurate_size_estimates","pull_request_files_virtualization","react_quality_profiling","repository_suggester_elastic_search","ruleset_deletion_confirmation","sample_network_conn_type","session_logs_ungroup_reasoning_text","site_calculator_actions_2025","site_features_copilot_universe","site_homepage_collaborate_video","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","suppress_non_representative_vitals","swe_agent_member_requests","viewscreen_sandbox","webp_support","workbench_store_readonly"],"login":"s22223767-tech","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="module" src="./app_files/wp-runtime-edc7ff57d928a8fd.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/19762-11359aa726bfa310.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/49863-21c6cbfbf220bccc.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/22060-2b1469bdf1cc1896.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/environment-9b01f1112fc0be7a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/2966-53b8db02ad08bd88.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/96232-0565258814d2aa82.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/41013-e7bd6287f315076c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/51210-87cec99190c81f2a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/41121-3203d9fe85fba7fe.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/2302-e320dbbf74fc7c4c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/46740-0fc6ffa320a9d861.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/20425-88c41b1da1147477.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/github-elements-754fd95de4b65885.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/element-registry-34aa38c74fdb21f5.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/react-core-493ffbbe75f9f751.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/react-lib-9964c96af38eac83.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/7053-c78bcdab3e8bd57f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/79039-5571f52ba76736e8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/61110-e408dd06d053598a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/2887-06b8c433f93025a5.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/26533-3f904546a9adb09a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/62249-5a4eb7194c2cbfcc.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/16674-bcda6cd2fcd23a06.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/55821-dc65ccb0e2ea7977.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/84184-f40661709a372bf3.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/91160-1fa08a016bbe422f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/68160-0f8a659d1d48e69d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/34391-01f1ed172183e208.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/64453-7e3495be06388d2c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/behaviors-b7dedbefa689e598.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/20475-1830fd8d2066405f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/notifications-global-680c705879085e31.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/70447-46e8cc37d8812f30.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/59572-ce559e8f19ffe6df.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/64124-e3a455b720c17264.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/codespaces-42be3ca6fdfc9955.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/3064-260d1f705222f78e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/89756-4562e9b925ef0722.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/99291-2f83d0e37b445d9e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/repositories-19d113bcb9c474de.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/76181-21c19e0669ff9281.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./app_files/code-menu-f5d3c881fccea328.js.download" defer="defer"></script>
  
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.197622a63ecf569d.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/notifications-subscriptions-menu.56550e605164684b.module.css">


  



  
  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      
      

        


  <meta http-equiv="x-pjax-version" content="a3dfb0df5cdf595e172855db4fd08054a0c2c86c358546a9636255d0a69a79e9" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="21a43568025709b66240454fc92d4f09335a96863f8ab1c46b4a07f6a5b67102" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="27a0190f89189c3553ee8d331900a7c8a4f2b02ea12da5b42a218cbe7233cc92" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="8c7947c0c592efeab6162b9909ad11fa43bff8b0cb5ff43273dc25e41979d43e" data-turbo-track="reload">

  

      
  

  



      


    
  


  

  

  
  

  
  
  





  

  <link rel="stylesheet" type="text/css" href="./app_files/81758.2218287c46dd7a31.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/38963.cf1064b4d7266dd0.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/7872.55f3c7cfb052f16a.module.css" crossorigin="anonymous"><style data-styled="active" data-styled-version="5.3.11"></style><link rel="stylesheet" type="text/css" href="./app_files/71426.50987a90f8f27146.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/66888.3561e56fcac0bef2.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/56065.0cb7c0a01a842ec3.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/83194.b6f07f51ec792226.module.css" crossorigin="anonymous"><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link rel="stylesheet" type="text/css" href="./app_files/88778.415c4c6675ed20de.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/59372.71005479b8daa131.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/27774.0e246a97bb0464b2.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./app_files/77507.ade55ae7d3a3a154.module.css" crossorigin="anonymous"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/16920.8efbea4317449f6f.module.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/react-code-view.d982287172949ea1.module.css"><script type="module" src="./app_files/primer-react-44d811a04e9fe66e.js.download"></script><script type="module" src="./app_files/octicons-react-9a6515a21626d647.js.download"></script><script type="module" src="./app_files/59660-8ea0dc2363e97b3d.js.download"></script><script type="module" src="./app_files/73694-446e08f308acdc9e.js.download"></script><script type="module" src="./app_files/68751-174a536f355f93e2.js.download"></script><script type="module" src="./app_files/42688-b45ef6dd2ec89951.js.download"></script><script type="module" src="./app_files/13835-30961eef6b633f5b.js.download"></script><script type="module" src="./app_files/7463-5efd607521215233.js.download"></script><script type="module" src="./app_files/32769-0f2fd359d4cb24c6.js.download"></script><script type="module" src="./app_files/437-cabc74ea97096904.js.download"></script><script type="module" src="./app_files/94240-2eb1cbeac1b7d490.js.download"></script><script type="module" src="./app_files/58110-afe12f4509a7ed35.js.download"></script><script type="module" src="./app_files/18549-48a4a7f6e4386ac9.js.download"></script><script type="module" src="./app_files/97083-c0758eadaf623756.js.download"></script><script type="module" src="./app_files/77691-a7a81c5ee137b001.js.download"></script><script type="module" src="./app_files/46376-82e359a6ef8b6107.js.download"></script><script type="module" src="./app_files/36322-b74c3b399ffc94c8.js.download"></script><script type="module" src="./app_files/84085-f815be0b0d43a9ad.js.download"></script><script type="module" src="./app_files/82048-e88f4e7b65645ac2.js.download"></script><script type="module" src="./app_files/99028-fcab0957a037c95b.js.download"></script><script type="module" src="./app_files/81482-42c7323947783c91.js.download"></script><script type="module" src="./app_files/32288-9d651cb8d1a5af21.js.download"></script><script type="module" src="./app_files/78967-1cf7f9b619d28446.js.download"></script><script type="module" src="./app_files/69395-661f089259ae48cd.js.download"></script><script type="module" src="./app_files/51705-e6673e21e3947c09.js.download"></script><script type="module" src="./app_files/23270-b08b96000d658a4e.js.download"></script><script type="module" src="./app_files/21463-2705cd7bc424f00a.js.download"></script><script type="module" src="./app_files/67894-aa744f27a3270d9d.js.download"></script><script type="module" src="./app_files/45739-b3a998eb9c345005.js.download"></script><script type="module" src="./app_files/15460-83d183a6061c8f0b.js.download"></script><script type="module" src="./app_files/50343-f576b6baad263f08.js.download"></script><script type="module" src="./app_files/10870-877eea2477b3618e.js.download"></script><script type="module" src="./app_files/16920-de9153be381431a6.js.download"></script><script type="module" src="./app_files/react-code-view-7f9b1e975c66b8cd.js.download"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>s22223767-tech/spam-detector</title><meta name="route-pattern" content="/:user_id/:repository" data-turbo-transient=""><meta name="route-controller" content="files" data-turbo-transient=""><meta name="route-action" content="disambiguate" data-turbo-transient=""><meta name="fetch-nonce" content="v2:5ab2f79a-db96-aa11-1d90-8521afcbcb50"><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="DB16:5F6C9:CF63A0:F103F7:698DB11B" data-turbo-transient="true"><meta name="html-safe-nonce" content="889dbdff4c06a9d7e2cf1ae463ddb8ade2f3f776ee349dd2b37bd02e2de81d8a" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS8iLCJyZXF1ZXN0X2lkIjoiREIxNjo1RjZDOTpDRjYzQTA6RjEwM0Y3OjY5OERCMTFCIiwidmlzaXRvcl9pZCI6IjQ1NzMzNDQ4ODg3MzEyMTQxNiIsInJlZ2lvbl9lZGdlIjoiY2VudHJhbGluZGlhIiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-turbo-transient="true"><meta name="visitor-hmac" content="ea7d57b12fff7d04550902b10bf8936f1f2aaf0f85d3bf147431388197239c9c" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:1152624003" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="247223143"><meta name="octolytics-actor-login" content="s22223767-tech"><meta name="octolytics-actor-hash" content="72e1fa8026efac91aa821aca6aa28a5e4770a62a183bb2081a5ce903a830dd55"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-turbo-transient="true"><meta name="user-login" content="s22223767-tech"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="viewport" content="width=device-width"><meta name="description" content="Contribute to s22223767-tech/spam-detector development by creating an account on GitHub."><link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub"><link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub"><meta property="fb:app_id" content="1401488693436528"><meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/s22223767-tech/spam-detector"><meta name="twitter:image" content="https://opengraph.githubassets.com/7eabeb05afba398cb55ead9f7d1644695953465053d1a9f964345ba500cc45ee/s22223767-tech/spam-detector"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="s22223767-tech/spam-detector"><meta name="twitter:description" content="Contribute to s22223767-tech/spam-detector development by creating an account on GitHub."><meta property="og:image" content="https://opengraph.githubassets.com/7eabeb05afba398cb55ead9f7d1644695953465053d1a9f964345ba500cc45ee/s22223767-tech/spam-detector"><meta property="og:image:alt" content="Contribute to s22223767-tech/spam-detector development by creating an account on GitHub."><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="s22223767-tech/spam-detector"><meta property="og:url" content="https://github.com/s22223767-tech/spam-detector"><meta property="og:description" content="Contribute to s22223767-tech/spam-detector development by creating an account on GitHub."><link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/247223143/ws?session=eyJ2IjoiVjMiLCJ1IjoyNDcyMjMxNDMsInMiOjE5NjM2Mjg4NjAsImMiOjI0NTA5ODY1MzcsInQiOjE3NzA4OTM1OTZ9--77b97496b21b1373e8352be5c372f0b2d6d71a6fcb82b8432737c665d5f13e99" data-refresh-url="/_alive" data-session-id="08b134bf3439873b4968cfd4b5571ef4744d7aff5d79f9be375a68d9ab55f957"><link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-ed5bfa283decc23a.js"><meta name="hostname" content="github.com"><meta name="keyboard-shortcuts-preference" content="all"><meta name="hovercards-preference" content="true"><meta name="announcement-preference-hovercard" content="true"><meta name="expected-hostname" content="github.com"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/s22223767-tech/spam-detector git https://github.com/s22223767-tech/spam-detector.git"><meta name="octolytics-dimension-user_id" content="247223143"><meta name="octolytics-dimension-user_login" content="s22223767-tech"><meta name="octolytics-dimension-repository_id" content="1152624003"><meta name="octolytics-dimension-repository_nwo" content="s22223767-tech/spam-detector"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="1152624003"><meta name="octolytics-dimension-repository_network_root_nwo" content="s22223767-tech/spam-detector"><link rel="canonical" href="https://github.com/s22223767-tech/spam-detector" data-turbo-transient=""><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="disable-turbo" content="false"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="release" content="b22a9fbf4dea601ec149a9e5362e0558df79b505"><meta name="ui-target" content="full"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 15px;" data-dialog-scroll-optimized="">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent=""></div>
      

    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/s22223767-tech/spam-detector#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.197622a63ecf569d.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/keyboard-shortcuts-dialog.2ff65a9060a75215.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA__r_4j___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>





      

          

                  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.197622a63ecf569d.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-nav-bar.e6ee9df9ad607799.module.css">

<react-partial partial-name="global-nav-bar" data-ssr="true" data-attempted-ssr="true" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"contextRegion":{"crumbs":[{"crumb_type":"user","label":"s22223767-tech","is_root":false,"href":"/s22223767-tech"},{"crumb_type":"repository","label":"spam-detector","is_root":false,"href":"/s22223767-tech/spam-detector"}],"localNavigation":[{"id":"code","icon":"code","label":"Code","href":"/s22223767-tech/spam-detector","selectedLinks":["repo_source","repo_downloads","repo_commits","repo_releases","repo_tags","repo_branches","repo_packages","repo_deployments","repo_attestations"],"popoverTarget":false,"hotkey":"g c","reactNav":{"appTarget":"code-view","anchor":"code-view-repo-link"},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"issues","icon":"issue-opened","label":"Issues","href":"/s22223767-tech/spam-detector/issues","selectedLinks":["repo_issues","repo_labels","repo_milestones"],"count":0,"popoverTarget":false,"hotkey":"g i","reactNav":{"appTarget":"issues-react","anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"pull-requests","icon":"git-pull-request","label":"Pull requests","href":"/s22223767-tech/spam-detector/pulls","selectedLinks":["repo_pulls","checks"],"count":0,"popoverTarget":false,"hotkey":"g p","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"actions","icon":"play","label":"Actions","href":"/s22223767-tech/spam-detector/actions","selectedLinks":["repo_actions"],"popoverTarget":false,"hotkey":"g a","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"projects","icon":"table","label":"Projects","href":"/s22223767-tech/spam-detector/projects","selectedLinks":["repo_projects","new_repo_project","repo_project"],"count":0,"popoverTarget":false,"hotkey":"g b","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"wiki","icon":"book","label":"Wiki","href":"/s22223767-tech/spam-detector/wiki","selectedLinks":["repo_wiki"],"popoverTarget":false,"hotkey":"g w","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"security","icon":"shield","label":"Security","href":"/s22223767-tech/spam-detector/security","selectedLinks":["security","overview","alerts","policy","token_scanning","code_scanning"],"count":0,"popoverTarget":false,"hotkey":"g s","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"insights","icon":"graph","label":"Insights","href":"/s22223767-tech/spam-detector/pulse","selectedLinks":["repo_graphs","repo_contributors","dependency_graph","dependabot_updates","pulse","people","community"],"popoverTarget":false,"reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"settings","icon":"gear","label":"Settings","href":"/s22223767-tech/spam-detector/settings","selectedLinks":["code_review_limits","code_quality","codespaces_repository_settings","collaborators","custom_tabs","github_models_repo_settings","hooks","integration_installations","interaction_limits","issue_template_editor","key_links_settings","license_policy","notifications","repo_announcements","repo_branch_settings","repo_custom_properties","repo_keys_settings","repo_pages_settings","repo_protected_tags_settings","repo_rule_insights","repo_rules_bypass_requests","repo_rulesets","repo_settings_copilot_coding_guidelines","repo_settings_copilot_content_exclusion","repo_settings_copilot_swe_agent","repo_settings","reported_content","repository_actions_settings_add_new_runner","repository_actions_settings_general","repository_actions_settings_runner_details","repository_actions_settings_runners","repository_actions_settings","repository_actions_settings_policies","repository_environments","role_details","secrets_settings_actions","secrets_settings_codespaces","secrets_settings_dependabot","secrets","security_analysis","security_products"],"popoverTarget":false,"reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}}],"selectedLink":"repo_source"},"navMenu":{"home":{"href":"https://github.com/dashboard","hotkey":"g d"},"feed":{"show":false,"href":"https://github.com/feed"},"issues":{"href":"https://github.com/issues","hotkey":"g i"},"pulls":{"href":"https://github.com/pulls","hotkey":"g p"},"contributedRepos":{"show":true,"href":"https://github.com/repos","hotkey":null},"projects":{"href":"https://github.com/projects"},"discussions":{"show":true,"href":"https://github.com/discussions"},"codespaces":{"show":true,"href":"https://github.com/codespaces"},"copilot":{"show":true,"href":"/copilot"},"spark":{"show":false,"href":null},"marketplace":{"show":true,"href":"https://github.com/marketplace"},"mcp":{"show":true,"href":"https://github.com/mcp"},"explore":{"show":true,"href":"https://github.com/explore"},"richContent":{"show":true,"contentUrl":"/_side-panels/global.json","repositoriesSearchUrl":"/_side-panel-items/global/repositories.json"}},"accountSwitchDialog":{"show":false},"globalTransactionalMessage":null,"userMenu":{"owner":{"login":"s22223767-tech","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/247223143?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2Fs22223767-tech%2Fspam-detector","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/s22223767-tech?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false},"createMenu":{"showCreateRepo":true,"showImportRepo":true,"showCodespaces":true,"showSpark":false,"showCodingAgent":false,"showGist":true,"showCreateOrg":true,"showCreateProject":false,"showCreateLegacyProject":false,"showCreateIssue":true,"createProjectUrl":"/s22223767-tech?tab=projects","org":null,"owner":"s22223767-tech","repo":"spam-detector"},"headerLogo":{"href":"https://github.com/","hotkey":"g d","aria-label":"Homepage "},"notifications":{"hotkey":"g n","indicatorMode":"none","websocketChannel":"eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MjQ3MjIzMTQzIiwidCI6MTc3MDg5MzU5Nn0=--9fe22611f681044085e621dd0197986bfc69d44059df1516e937fb75bb88aa80","fetchIndicatorSrc":"/notifications/indicator","fetchIndicatorEnabled":true},"issues":{"href":"https://github.com/issues","hotkey":"g i"},"pulls":{"href":"https://github.com/pulls","hotkey":"g p"},"contributedRepos":{"show":true,"href":"https://github.com/repos","hotkey":null},"copilot":{"show":true,"showCopilotTitle":false,"showAgentsButton":false,"copilotChatUrl":"/github-copilot/chat?skip_anchor=true","copilotApiUrl":"https://api.individual.githubcopilot.com","agentsPanel":{"popoverAvailable":true,"repository":{"id":1152624003,"name":"spam-detector","ownerLogin":"s22223767-tech"},"showNotification":false,"linkToSessionsInRepo":true,"freeUserPopoverAvailable":false}},"search":{"show":true,"searchHotkey":"s,/","showCommandPalette":false,"commandPaletteHotkey":null,"isSearchPage":false,"isJumpToSearch":false,"fragmentsPath":"/_global-navigation/fragments","fragmentsParams":null},"enterpriseBanner":{"show":false}}}</script>
  <div data-target="react-partial.reactRoot"><header role="banner" aria-label="Global Navigation Menu" class="GlobalNav styles-module__appHeader__YzYWk prc-Stack-Stack-UQ9k6" data-gap="none" data-direction="vertical" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="none"><div class="prc-Stack-Stack-UQ9k6" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="center" data-padding="none"><div data-testid="top-nav-left" class="styles-module__left__Fylw7 styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-loading-wrapper="true"><button data-component="IconButton" type="button" aria-haspopup="dialog" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_4m_" fdprocessedid="7r3dsn"><svg aria-hidden="true" focusable="false" class="octicon octicon-three-bars" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path></svg></button></div><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_4m_" popover="auto">Open menu</span><div class="d-none"><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby="_r_4o_--label  " id="_r_4o_" data-size="medium" href="https://github.com/dashboard" data-testid="side-nav-menu-item-HOME" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-home" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id="_r_4o_--label" class="prc-ActionList-ItemLabel-81ohH">Home</span></span></a></li><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby="_r_4p_--label  " id="_r_4p_" data-size="medium" href="https://github.com/issues" data-testid="side-nav-menu-item-ISSUES" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id="_r_4p_--label" class="prc-ActionList-ItemLabel-81ohH">Issues</span></span></a></li><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby="_r_4q_--label  " id="_r_4q_" data-size="medium" href="https://github.com/pulls" data-testid="side-nav-menu-item-PULL_REQUESTS" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id="_r_4q_--label" class="prc-ActionList-ItemLabel-81ohH">Pull requests</span></span></a></li></div><a data-component="IconButton" type="button" href="https://github.com/" data-hotkey="g d" hotkey="g d" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderHome__nkA_U prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_4r_"><svg aria-hidden="true" focusable="false" class="octicon octicon-mark-github" viewBox="0 0 24 24" width="32" height="32" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_r_4r_">Homepage <span class="prc-src-InternalVisuallyHidden-2YaI6">(g then d)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">d</span><span aria-hidden="true">D</span></span></kbd></span></span></div><div data-testid="top-nav-center" class="styles-module__center__R3QRv styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><nav class="styles-module__contextRegion__VbSp2 prc-Breadcrumbs-BreadcrumbsBase-3Gb-B" aria-label="Breadcrumbs" data-overflow="menu" data-variant="normal"><ol class="prc-Breadcrumbs-BreadcrumbsList-BKjpe"><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/s22223767-tech" data-discover="true"><span class="">s22223767-tech</span></a></li><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/s22223767-tech/spam-detector" data-discover="true"><span class="styles-module__contextCrumbLast__tI2e3">spam-detector</span></a></li></ol></nav><div class="Search-module__searchButtonGroup__aetw5 prc-ButtonGroup-ButtonGroup-vFUrY"><div><a type="button" aria-label="Search or jump to…" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__searchButton__aiE0a" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="Search-module__placeholder__p9hbG Search-module__text__veSYi Search-module__value__TFoak">Type <kbd class="Search-module__kbd__WCskr">/</kbd> to search</span></span></span></a></div><div></div></div><button data-component="IconButton" type="button" data-hotkey="s,/" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__smallSearchButton___8Gvn prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_4u_"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_r_4u_">Search or jump to…<span class="prc-src-InternalVisuallyHidden-2YaI6">(s,/)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">s,/</span><span aria-hidden="true">S,/</span></span></kbd></span></span><div class="d-none"><qbsearch-input class="search-input" data-scope="repo:s22223767-tech/spam-detector" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="Mt9RtsPOgMFQb3MPNhALjJr-IkbwuyZHfbI8S1tuuYQCFRYWmoFZF_SFsxSH8OYbS6qSXlyc6aqG6VT-Mt2pjw" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="s22223767-tech/spam-detector" data-current-org="" data-current-owner="s22223767-tech" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/s22223767-tech/spam-detector" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-88ee280a-3920-460b-b7e6-f13dd8121485" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-88ee280a-3920-460b-b7e6-f13dd8121485" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="O6bIrM9NQfJjjv_OoW6KvRwKG18ncOlclRCSk3Cv0JdN7OEyzdvnLBt0OXJFfI-6rjyt-jUSZyhICx26slqqHQ">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="5dZizR09Mb367OFeXcTKRVf5np10t6u55pJxife7Y7kybkWW0ye3UJeY8rAYqDldWQ5T30_3f18ee64siHaj2A">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="pMXJ8PmA7VXhBrCWZj6GCqbitxWV5XPPq2Q0NVZ4ZGMzjZLHnj5guBlIL0I8jck2dpTREwRuz3V11OeKfym3ZQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="v02D5IE08zeT1H6ceCQ2RcQrj-Aopy813Yo9J3Bj2k7VQG6Or_g-dNZZpBJ27QRJrOGUmWLl7jxDdcG3f2xIrQ" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf"></div></div><div data-testid="top-nav-right" class="styles-module__right__mlBQg styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-testid="top-bar-actions" class="hide-sm hide-md prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="none"><span><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="IconButton" type="button" href="https://github.com/copilot" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_50_"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_50_" popover="auto">Chat with Copilot</span></div><div><div class="d-none"></div><button type="button" aria-label="Open Copilot…" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ CopilotItems-module__CopilotMenu__DVdfE" data-loading="false" data-size="medium" data-variant="invisible" id="_r_53_" fdprocessedid="wmm19i"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button></div></div><div class="CopilotChat-module__CopilotChatContainer__qrVEG"></div><div class="PortalContainerUtils-module__chatPortalContainer__ZwauZ"></div><div class="PortalContainerUtils-module__menuPortalContainer__q0Ygl CopilotChat-module__menuPortalContainer__DqZy4"></div></span><div class="styles-module__itemDivider__nunbs"></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk GlobalCreateMenu-module__actionMenuButton__Hj_iB" data-loading="false" data-size="medium" data-variant="invisible" aria-labelledby="global-create-menu-tooltip-_r_56_" id="_r_57_" fdprocessedid="muid3r"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="global-create-menu-tooltip-_r_56_" popover="auto">Create new...</span><a data-component="IconButton" type="button" href="https://github.com/issues" data-hotkey="g i" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_5b_"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_r_5b_">Issues<span class="prc-src-InternalVisuallyHidden-2YaI6">(g then i)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">i</span><span aria-hidden="true">I</span></span></kbd></span></span><a data-component="IconButton" type="button" href="https://github.com/pulls" data-hotkey="g p" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_5d_"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto" style="top: 52px; left: 1306.43px;"><span id="_r_5d_">Pull requests<span class="prc-src-InternalVisuallyHidden-2YaI6">(g then p)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">p</span><span aria-hidden="true">P</span></span></kbd></span></span><a data-component="IconButton" type="button" href="https://github.com/repos" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_5f_"><svg aria-hidden="true" focusable="false" class="octicon octicon-repo" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_5f_" popover="auto">Repositories</span></div><a data-component="IconButton" type="button" href="https://github.com/notifications" data-hotkey="g n" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_5h_"><svg aria-hidden="true" focusable="false" class="octicon octicon-inbox" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_r_5h_">You have no unread notifications<span class="prc-src-InternalVisuallyHidden-2YaI6">(g then n)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">n</span><span aria-hidden="true">N</span></span></kbd></span></span><div class="GlobalNavUserMenu-module__container__NaVIt"><button data-component="IconButton" type="button" aria-haspopup="menu" data-login="s22223767-tech" class="prc-Button-ButtonBase-9n-Xk GlobalNavUserMenu-module__anchor__Dcej6 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_r_5j_" fdprocessedid="lclkl6"><img data-component="Avatar" class="Box-sc-62in7e-0 lpqgUB prc-Avatar-Avatar-0xaUi" alt="User avatar" width="32" height="32" data-testid="github-avatar" src="./app_files/247223143" style="--avatarSize-regular: 32px;"></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_5j_" popover="auto">Open user navigation menu</span></div></div></div><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj LocalNavigation-module__LocalNavigation__b0Xc0" aria-label="Repository" data-variant="inset"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector" aria-current="page" data-hotkey="g c" data-react-nav="code-view" data-react-nav-anchor="code-view-repo-link" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" data-content="Code">Code</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/issues" data-hotkey="g i" data-react-nav="issues-react" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span data-component="text" data-content="Issues">Issues</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/pulls" data-hotkey="g p" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span data-component="text" data-content="Pull requests">Pull requests</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/actions" data-hotkey="g a" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-play" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg></span><span data-component="text" data-content="Actions">Actions</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/projects" data-hotkey="g b" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-table" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path></svg></span><span data-component="text" data-content="Projects">Projects</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/wiki" data-hotkey="g w" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="Wiki">Wiki</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/security" data-hotkey="g s" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg></span><span data-component="text" data-content="Security">Security</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/pulse" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-graph" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></span><span data-component="text" data-content="Insights">Insights</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector/settings" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-gear" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg></span><span data-component="text" data-content="Settings">Settings</span></a></li></ul></nav></header><script type="application/json" id="__PRIMER_DATA__r_4l___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


      <div class="js-global-bar" style="display: none;">
        


<qbsearch-input class="search-input" data-scope="repo:s22223767-tech/spam-detector" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="Mt9RtsPOgMFQb3MPNhALjJr-IkbwuyZHfbI8S1tuuYQCFRYWmoFZF_SFsxSH8OYbS6qSXlyc6aqG6VT-Mt2pjw" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="s22223767-tech/spam-detector" data-current-org="" data-current-owner="s22223767-tech" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/s22223767-tech/spam-detector" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-88ee280a-3920-460b-b7e6-f13dd8121485" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-88ee280a-3920-460b-b7e6-f13dd8121485" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="O6bIrM9NQfJjjv_OoW6KvRwKG18ncOlclRCSk3Cv0JdN7OEyzdvnLBt0OXJFfI-6rjyt-jUSZyhICx26slqqHQ">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="5dZizR09Mb367OFeXcTKRVf5np10t6u55pJxife7Y7kybkWW0ye3UJeY8rAYqDldWQ5T30_3f18ee64siHaj2A">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="pMXJ8PmA7VXhBrCWZj6GCqbitxWV5XPPq2Q0NVZ4ZGMzjZLHnj5guBlIL0I8jck2dpTREwRuz3V11OeKfym3ZQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="v02D5IE08zeT1H6ceCQ2RcQrj-Aopy813Yo9J3Bj2k7VQG6Or_g-dNZZpBJ27QRJrOGUmWLl7jxDdcG3f2xIrQ" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


      </div>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/s22223767-tech/spam-detector">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/s22223767-tech/spam-detector">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/s22223767-tech/spam-detector">Reload</a> to refresh your session.</span>

    <button id="icon-button-61451615-6568-49fa-87ba-2bfac82112d5" aria-labelledby="tooltip-788182c0-5fec-4765-97e4-06009bacb88f" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-788182c0-5fec-4765-97e4-06009bacb88f" for="icon-button-61451615-6568-49fa-87ba-2bfac82112d5" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MjQ3MjIzMTQzIiwidCI6MTc3MDg5MzU5Nn0=--9fe22611f681044085e621dd0197986bfc69d44059df1516e937fb75bb88aa80" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  


<template class="js-user-list-create-dialog-template" data-label="Create list"></template>



    






  
    

  <div id="repository-container-header" class="pt-3 hide-full-screen" data-turbo-replace="">

      <div class="d-flex flex-nowrap flex-justify-end mb-3  container-xl  px-3 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit">
              <div id="repo-title-component" class=" d-flex flex-nowrap flex-items-center wb-break-word f3 text-normal">
    <img class="avatar mr-2 d-none d-md-block avatar-user" alt="Owner avatar" src="./app_files/247223143(1)" width="24" height="24">
  

  <strong itemprop="name" class="mr-2 flex-self-stretch d-none d-md-block no-wrap overflow-x-hidden">
    <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" class="d-block overflow-x-hidden color-fg-default" style="text-overflow: ellipsis;" href="https://github.com/s22223767-tech/spam-detector">spam-detector</a>
  </strong>

  <span></span><span class="Label Label--secondary v-align-middle mr-1 d-none d-md-block">Public</span>
</div>

<div class="d-none d-md-block">
</div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace="" style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      <li>
  <div class="float-left">
    <!-- '"` --><!-- </textarea></xmp> --><form data-turbo="false" action="https://github.com/s22223767-tech/spam-detector/profile_pin" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Qpqnw6v99lqKIuegQ-InFLSIG9oJtjzCazd0TD8farlcWzzHfj3bhHU7bY9m4CPB0HZqlP9I65kMyEGl2OIjKQ" autocomplete="off">
        <button title="Pin this repository to your profile" type="submit" data-view-component="true" class="btn-sm btn" fdprocessedid="wi96e9">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pin mr-2">
    <path d="m11.294.984 3.722 3.722a1.75 1.75 0 0 1-.504 2.826l-1.327.613a3.089 3.089 0 0 0-1.707 2.084l-.584 2.454c-.317 1.332-1.972 1.8-2.94.832L5.75 11.311 1.78 15.28a.749.749 0 1 1-1.06-1.06l3.969-3.97-2.204-2.204c-.968-.968-.5-2.623.832-2.94l2.454-.584a3.08 3.08 0 0 0 2.084-1.707l.613-1.327a1.75 1.75 0 0 1 2.826-.504ZM6.283 9.723l2.732 2.731a.25.25 0 0 0 .42-.119l.584-2.454a4.586 4.586 0 0 1 2.537-3.098l1.328-.613a.25.25 0 0 0 .072-.404l-3.722-3.722a.25.25 0 0 0-.404.072l-.613 1.328a4.584 4.584 0 0 1-3.098 2.537l-2.454.584a.25.25 0 0 0-.119.42l2.731 2.732Z"></path>
</svg>Pin
</button></form>  </div>
</li>


  <li>
              <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.197622a63ecf569d.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/notifications-subscriptions-menu.56550e605164684b.module.css">

<react-partial partial-name="notifications-subscriptions-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"subscriptionType":"none","repositoryId":1152624003,"repositoryName":"s22223767-tech/spam-detector","watchersCount":0,"subscribableThreadTypes":[{"name":"Issue","enabled":true,"subscribed":false},{"name":"PullRequest","enabled":true,"subscribed":false},{"name":"Release","enabled":true,"subscribed":false},{"name":"Discussion","enabled":false,"subscribed":false},{"name":"SecurityAlert","enabled":true,"subscribed":false}],"repositoryLabels":[],"showLabelSubscriptions":false}}</script>
  <div data-target="react-partial.reactRoot"><button type="button" data-testid="notifications-subscriptions-menu-button" aria-label="Watch: Participating in s22223767-tech/spam-detector" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk NotificationsSubscriptionsMenu-module__ActionMenuButton__FVE3w" data-loading="false" data-size="small" data-variant="default" id="_r_6m_" fdprocessedid="f8plc"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-eye" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Watch<span class="ml-2 Counter rounded-3 NotificationsSubscriptionsMenu-module__watchCounter__iKoWw">0</span></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button><script type="application/json" id="__PRIMER_DATA__r_6l___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <button icon="repo-forked" id="fork-button" aria-disabled="true" type="button" data-view-component="true" class="btn-sm btn BtnGroup-item" aria-describedby="tooltip-a98e7088-1586-4831-bb08-227930dcac56" fdprocessedid="bxlrpf">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
        <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="0" data-view-component="true" class="Counter">0</span>
        <tool-tip id="tooltip-a98e7088-1586-4831-bb08-227930dcac56" for="fork-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Cannot fork because you own this repository and are not a member of any organizations.</tool-tip>
</button>
      <details group_item="true" id="my-forks-menu-1152624003" data-view-component="true" class="details-reset details-overlay BtnGroup-parent d-inline-block position-relative">
              <summary aria-label="See your forks of this repository" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/s22223767-tech/spam-detector/my_forks_menu_content?can_fork=false" role="menu">
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="my-forks-menu-1152624003">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </button>
      <div id="filter-menu-498814" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment aria-label="Loading" data-nonce="v2:5ab2f79a-db96-aa11-1d90-8521afcbcb50" data-view-component="true" class="SelectMenu-loading"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
                <p data-show-on-error="" hidden="">
                  Forks could not be loaded
                </p>
                <span data-hide-on-error="">
                                  <span data-view-component="true">
  <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>

                </span>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/s22223767-tech/spam-detector" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>        </div>
        
      </div>
    </div>
  </details-menu>
</details></div>
  </li>

  <li>
        <template class="js-unstar-confirmation-dialog-template" aria-live="polite"></template>

  <div data-view-component="true" class="js-toggler-container js-social-container starring-container d-flex">
    <div data-view-component="true" class="starred BtnGroup flex-1 ml-0">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto js-deferred-toggler-target" data-turbo="false" action="https://github.com/s22223767-tech/spam-detector/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="8yMwWT0E6S7GE3axK4EoXmo9L62WW92FRX2zb4il-pgaNxDWmUP5gNa1elPFqKn_kL2O_-AFBr3F5e8CEwjBGw" autocomplete="off">
          <input type="hidden" value="2wfHmOdWkt0XB-FZiTOcvJN-oh-Y4TKLPenFZmCKxo8yE-cXQxGCcweh7btnGh0daf4DTe6_6bO9cZkL-yf9DA" data-csrf="true" class="js-confirm-csrf-token">
        <input type="hidden" name="context" value="repository">
          <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:1152624003,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="3b93942cec60e8807ac9a6555bc327f534e247fb3b49ebb3e6533c986ceef42b" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" data-aria-prefix="Starred, click to unstar this repository" aria-label="Starred, click to unstar this repository (0)" type="submit" data-view-component="true" class="rounded-left-2 btn-with-aria-count btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
</svg><span data-view-component="true" class="d-inline">
              Starred
</span>              <span id="repo-stars-counter-unstar" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</button></form>          <user-list-menu data-controller="user-list-menu" data-repository-id="1152624003" data-update-url="/s22223767-tech/spam-detector/lists">
    <select-panel data-target="user-list-menu.selectPanel" data-select-variant="multiple" data-fetch-strategy="remote" data-open-on-load="false" id="details-user-list-1152624003-starred" anchor-align="end" anchor-side="outside-bottom" data-view-component="true" class="BtnGroup-parent js-user-list-menu" data-catalyst="">
  <dialog-helper>
    <button group_item="true" id="details-user-list-1152624003-starred-button" aria-controls="details-user-list-1152624003-starred-dialog" aria-haspopup="dialog" aria-expanded="false" aria-labelledby="tooltip-c14844a3-4f73-41cc-a47e-bf5315458679" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--small rounded-right-2 rounded-left-0 px-3">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-c14844a3-4f73-41cc-a47e-bf5315458679" for="details-user-list-1152624003-starred-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Add this repository to a list</tool-tip>

    <dialog id="details-user-list-1152624003-starred-dialog" aria-labelledby="details-user-list-1152624003-starred-dialog-title" data-target="select-panel.dialog" style="position: absolute;" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait">
      <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="details-user-list-1152624003-starred-dialog-title">
        Lists
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="details-user-list-1152624003-starred-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  <div data-view-component="true" class="Overlay-headerFilter">            <div data-target="select-panel.bannerErrorElement" hidden="">
              <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="Banner flash Banner--error flash-error mb-2">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">
                  </p><h2 class="f6 text-normal">Sorry, something went wrong.</h2>
<p></p>
</div></div></x-banner>            </div>
            <remote-input aria-owns="details-user-list-1152624003-starred-body" src="/s22223767-tech/spam-detector/lists?experimental=1" data-target="select-panel.remoteInput" data-view-component="true">
                <primer-text-field class="FormControl width-full FormControl--fullWidth" data-catalyst="">
      <label for="details-user-list-1152624003-starred-filter" class="sr-only FormControl-label position-absolute sr-only FormControl-label">
        Filter
</label>    
  <div class="FormControl-input-wrap FormControl-input-wrap--leadingVisual">
      <span class="FormControl-input-leadingVisualWrap">
        <svg data-target="primer-text-field.leadingVisual" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          <span hidden="hidden" data-target="primer-text-field.leadingSpinner" data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      </span>
    
      <input id="details-user-list-1152624003-starred-filter" type="search" autofocus="autofocus" data-target="primer-text-field.inputElement select-panel.filterInputTextField" aria-describedby="validation-9e666261-98f8-4256-bfa0-e500ad3f26a0" class="form-control FormControl-input FormControl-medium" name="filter" autocomplete="off" spellcheck="false">
</div>
      <div class="FormControl-inlineValidation" id="validation-9e666261-98f8-4256-bfa0-e500ad3f26a0" hidden="hidden">
  <span class="FormControl-inlineValidation--visual" data-target="primer-text-field.validationSuccessIcon" hidden=""><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-check-circle-fill">
    <path d="M6 0a6 6 0 1 1 0 12A6 6 0 0 1 6 0Zm-.705 8.737L9.63 4.403 8.392 3.166 5.295 6.263l-1.7-1.702L2.356 5.8l2.938 2.938Z"></path>
</svg></span>
  <span class=" FormControl-inlineValidation--visual" data-target="primer-text-field.validationErrorIcon"><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg></span>
  <span></span>
</div>
    
</primer-text-field>
</remote-input></div>
</div>      <div data-view-component="true" class="Overlay-body p-0">
        <focus-group direction="vertical" mnemonics="" retain="">
          <live-region data-target="select-panel.liveRegion"><template shadowrootmode="open">
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style>
<div id="polite" aria-live="polite" aria-atomic="true"></div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region>
          <div data-fetch-strategy="remote" data-target="select-panel.list" data-view-component="true">
            <div id="details-user-list-1152624003-starred-body">
                
                  <div id="details-user-list-1152624003-starred-list" aria-disabled="true" aria-busy="true" data-view-component="true" class="SelectPanel-loadingPanel mt-2 mb-2 d-flex flex-items-start flex-justify-center text-center">
                    <div data-hide-on-error="" class="pt-2">
                      <span data-target="select-panel.bodySpinner" data-view-component="true">
  <svg aria-label="Loading content..." style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" role="img" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg></span>
                    </div>
                    <div data-show-on-error="" hidden="" data-target="select-panel.fragmentErrorElement">
                        <div class="pt-2 pb-2">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert color-fg-danger">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
                          <h2 class="f5 mt-2">Sorry, something went wrong.</h2>
                        </div>
                    </div>
</div>            </div>
            <div data-target="select-panel.noResults" class="SelectPanel-emptyPanel" hidden="">
              <h2 class="v-align-middle m-3 f5">No results found</h2>
            </div>
</div>        </focus-group>
</div>      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">        <button data-repository-id="1152624003" type="button" data-view-component="true" class="js-user-lists-create-trigger Button--primary Button--medium Button Button--fullWidth">  <span class="Button-content">
    <span class="Button-label"><svg size="small" class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg>
          Create list</span>
  </span>
</button>
</div>
</dialog>  </dialog-helper>
</select-panel>  </user-list-menu>
  <template class="js-user-list-create-dialog-template" data-label="Create list"></template>


</div>
    <div data-view-component="true" class="unstarred BtnGroup ml-0 flex-1">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto" data-turbo="false" action="https://github.com/s22223767-tech/spam-detector/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Nl71BEvxXSAV-wc_9rxnRdBBDz-2DsLicYLwwUtpggQzN_RhvEof7nOqxkTBY7kAO-4F-Wb7hsh7yFmjo7n3oQ" autocomplete="off">
        <input type="hidden" name="context" value="repository">
          <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:1152624003,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="40a6f56141b5d66d4eabc3302ac83f3867924dd3cb501f015a2c3e8ad8c87001" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" data-aria-prefix="Star this repository" aria-label="Star this repository (0)" type="submit" data-view-component="true" class="js-toggler-target rounded-left-2 btn-with-aria-count btn-sm btn BtnGroup-item" fdprocessedid="egcfwp">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
              Star
</span>              <span id="repo-stars-counter-star" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</button></form>          <user-list-menu data-controller="user-list-menu" data-repository-id="1152624003" data-update-url="/s22223767-tech/spam-detector/lists">
    <select-panel data-target="user-list-menu.selectPanel" data-select-variant="multiple" data-fetch-strategy="remote" data-open-on-load="false" id="details-user-list-1152624003-unstarred" anchor-align="end" anchor-side="outside-bottom" data-view-component="true" class="BtnGroup-parent js-user-list-menu" data-catalyst="">
  <dialog-helper>
    <button group_item="true" id="details-user-list-1152624003-unstarred-button" aria-controls="details-user-list-1152624003-unstarred-dialog" aria-haspopup="dialog" aria-expanded="false" aria-labelledby="tooltip-c9159e3e-72e9-4350-b833-d8fb064899b9" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--small rounded-right-2 rounded-left-0 px-3" fdprocessedid="ce7nq">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-c9159e3e-72e9-4350-b833-d8fb064899b9" for="details-user-list-1152624003-unstarred-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 144px; --tool-tip-position-left: 1272.125051498413px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Add this repository to a list</tool-tip>

    <dialog id="details-user-list-1152624003-unstarred-dialog" aria-labelledby="details-user-list-1152624003-unstarred-dialog-title" data-target="select-panel.dialog" style="position: absolute;" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait">
      <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="details-user-list-1152624003-unstarred-dialog-title">
        Lists
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="details-user-list-1152624003-unstarred-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  <div data-view-component="true" class="Overlay-headerFilter">            <div data-target="select-panel.bannerErrorElement" hidden="">
              <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="Banner flash Banner--error flash-error mb-2">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">
                  </p><h2 class="f6 text-normal">Sorry, something went wrong.</h2>
<p></p>
</div></div></x-banner>            </div>
            <remote-input aria-owns="details-user-list-1152624003-unstarred-body" src="/s22223767-tech/spam-detector/lists?experimental=1" data-target="select-panel.remoteInput" data-view-component="true">
                <primer-text-field class="FormControl width-full FormControl--fullWidth" data-catalyst="">
      <label for="details-user-list-1152624003-unstarred-filter" class="sr-only FormControl-label position-absolute sr-only FormControl-label">
        Filter
</label>    
  <div class="FormControl-input-wrap FormControl-input-wrap--leadingVisual">
      <span class="FormControl-input-leadingVisualWrap">
        <svg data-target="primer-text-field.leadingVisual" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          <span hidden="hidden" data-target="primer-text-field.leadingSpinner" data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      </span>
    
      <input id="details-user-list-1152624003-unstarred-filter" type="search" autofocus="autofocus" data-target="primer-text-field.inputElement select-panel.filterInputTextField" aria-describedby="validation-2a3f6fe0-6a84-4c08-ae49-b62d61976f3a" class="form-control FormControl-input FormControl-medium" name="filter" autocomplete="off" spellcheck="false">
</div>
      <div class="FormControl-inlineValidation" id="validation-2a3f6fe0-6a84-4c08-ae49-b62d61976f3a" hidden="hidden">
  <span class="FormControl-inlineValidation--visual" data-target="primer-text-field.validationSuccessIcon" hidden=""><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-check-circle-fill">
    <path d="M6 0a6 6 0 1 1 0 12A6 6 0 0 1 6 0Zm-.705 8.737L9.63 4.403 8.392 3.166 5.295 6.263l-1.7-1.702L2.356 5.8l2.938 2.938Z"></path>
</svg></span>
  <span class=" FormControl-inlineValidation--visual" data-target="primer-text-field.validationErrorIcon"><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg></span>
  <span></span>
</div>
    
</primer-text-field>
</remote-input></div>
</div>      <div data-view-component="true" class="Overlay-body p-0">
        <focus-group direction="vertical" mnemonics="" retain="">
          <live-region data-target="select-panel.liveRegion"><template shadowrootmode="open">
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style>
<div id="polite" aria-live="polite" aria-atomic="true"></div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region>
          <div data-fetch-strategy="remote" data-target="select-panel.list" data-view-component="true">
            <div id="details-user-list-1152624003-unstarred-body">
                
                  <div id="details-user-list-1152624003-unstarred-list" aria-disabled="true" aria-busy="true" data-view-component="true" class="SelectPanel-loadingPanel mt-2 mb-2 d-flex flex-items-start flex-justify-center text-center">
                    <div data-hide-on-error="" class="pt-2">
                      <span data-target="select-panel.bodySpinner" data-view-component="true">
  <svg aria-label="Loading content..." style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" role="img" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg></span>
                    </div>
                    <div data-show-on-error="" hidden="" data-target="select-panel.fragmentErrorElement">
                        <div class="pt-2 pb-2">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert color-fg-danger">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
                          <h2 class="f5 mt-2">Sorry, something went wrong.</h2>
                        </div>
                    </div>
</div>            </div>
            <div data-target="select-panel.noResults" class="SelectPanel-emptyPanel" hidden="">
              <h2 class="v-align-middle m-3 f5">No results found</h2>
            </div>
</div>        </focus-group>
</div>      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">        <button data-repository-id="1152624003" type="button" data-view-component="true" class="js-user-lists-create-trigger Button--primary Button--medium Button Button--fullWidth">  <span class="Button-content">
    <span class="Button-label"><svg size="small" class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg>
          Create list</span>
  </span>
</button>
</div>
</dialog>  </dialog-helper>
</select-panel>  </user-list-menu>
  <template class="js-user-list-create-dialog-template" data-label="Create list"></template>


</div></div>
  </li>

</ul>

        </div>
      </div>

        <div class=" container-xl ">
          <div id="responsive-meta-container" data-turbo-replace="">
      <div class="d-block d-md-none mb-2 px-3 px-md-4 px-lg-5">
        <div class="d-flex gap-2 mt-n3 mb-3 flex-wrap">
          <div class="d-flex flex-row gap-2">
                <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.197622a63ecf569d.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/notifications-subscriptions-menu.56550e605164684b.module.css">

<react-partial partial-name="notifications-subscriptions-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"subscriptionType":"none","repositoryId":1152624003,"repositoryName":"s22223767-tech/spam-detector","watchersCount":0,"subscribableThreadTypes":[{"name":"Issue","enabled":true,"subscribed":false},{"name":"PullRequest","enabled":true,"subscribed":false},{"name":"Release","enabled":true,"subscribed":false},{"name":"Discussion","enabled":false,"subscribed":false},{"name":"SecurityAlert","enabled":true,"subscribed":false}],"repositoryLabels":[],"showLabelSubscriptions":false}}</script>
  <div data-target="react-partial.reactRoot"><button type="button" data-testid="notifications-subscriptions-menu-button" aria-label="Watch: Participating in s22223767-tech/spam-detector" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk NotificationsSubscriptionsMenu-module__ActionMenuButton__FVE3w" data-loading="false" data-size="small" data-variant="default" id="_r_6q_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-eye" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Watch<span class="ml-2 Counter rounded-3 NotificationsSubscriptionsMenu-module__watchCounter__iKoWw">0</span></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button><script type="application/json" id="__PRIMER_DATA__r_6p___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



              <div data-view-component="true" class="BtnGroup d-flex">
      <a id="fork-icon-button" variant="small" group_item="true" href="https://github.com/s22223767-tech/spam-detector/fork" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:1152624003,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="d1a7e56a465f41150a6071470a550369c1d9ba6b48b7a443b30c81a465cb249f" data-ga-click="Repository, show fork modal, action:files#disambiguate; text:Fork" aria-labelledby="tooltip-e9b47856-068d-4070-803b-c88f1d3e053c" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked Button-visual">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-e9b47856-068d-4070-803b-c88f1d3e053c" for="fork-icon-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Fork your own copy of s22223767-tech/spam-detector</tool-tip>

</div>
              <style>
  /*
    This is kind of gross but let me explain.
    The triangle-down icon in the user lists menu component needs to be larger on small screens
    but Primer doesn't accept a responsive value for size.
    So instead we use CSS to override the size on small screens only, to match the ⭐ button beside it.
    The selector is written this way to avoid affecting other buttons inside the lists dropdown.
  */
  @media (max-width: 767px) {
    .icon-button-group .BtnGroup-parent > * > button:first-child {
      height: var(--control-medium-size);
      width: var(--control-medium-size);
      min-width: var(--control-medium-size);
    }
  }

  /* No idea what this is though. It was like this when I got here. */
  @media (min-width: 544px) {
    .icon-button-group .SelectMenu {
      right: auto !important;
      left: 0 !important;
    }
  }
</style>
  <div data-view-component="true" class="js-toggler-container starring-container">
    <div data-view-component="true" class="starred BtnGroup icon-button-group flex-1 ml-0">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent" data-turbo="false" action="https://github.com/s22223767-tech/spam-detector/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="xesRRcsoEEs3NfcRHQ6nospabNX08BY7744_CofYcEAs_zHKb28A5SeT-_PzJyYDMNrNh4KuzQNvFmNnHHVLww" autocomplete="off">
        <input type="hidden" name="context" value="repository">
        <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:1152624003,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="3b93942cec60e8807ac9a6555bc327f534e247fb3b49ebb3e6533c986ceef42b" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" id="icon-button-4053a5fb-0052-46c7-bc3b-74c81a43d4d5" aria-labelledby="tooltip-03a6df37-fc83-4588-8567-e2c06d8381b0" type="submit" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium js-toggler-target starred-button-icon BtnGroup-item rounded-left-2">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill Button-visual">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
</svg>
</button><tool-tip id="tooltip-03a6df37-fc83-4588-8567-e2c06d8381b0" for="icon-button-4053a5fb-0052-46c7-bc3b-74c81a43d4d5" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Unstar this repository</tool-tip>

</form>          <user-list-menu data-controller="user-list-menu" data-repository-id="1152624003" data-update-url="/s22223767-tech/spam-detector/lists">
    <select-panel data-target="user-list-menu.selectPanel" data-select-variant="multiple" data-fetch-strategy="remote" data-open-on-load="false" id="details-user-list-1152624003" anchor-align="end" anchor-side="outside-bottom" data-view-component="true" class="BtnGroup-parent js-user-list-menu" data-catalyst="">
  <dialog-helper>
    <button group_item="true" id="details-user-list-1152624003-button" aria-controls="details-user-list-1152624003-dialog" aria-haspopup="dialog" aria-expanded="false" aria-labelledby="tooltip-c2bacbf7-a555-45f3-add2-82ceb77e49e2 tooltip-97c5787a-10ac-4062-a002-5ba9725b3810" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--small rounded-right-2 rounded-left-0 px-3">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-c2bacbf7-a555-45f3-add2-82ceb77e49e2" for="details-user-list-1152624003-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Add this repository to a list</tool-tip>

    <dialog id="details-user-list-1152624003-dialog" aria-labelledby="details-user-list-1152624003-dialog-title" data-target="select-panel.dialog" style="position: absolute;" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait">
      <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="details-user-list-1152624003-dialog-title">
        Lists
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="details-user-list-1152624003-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  <div data-view-component="true" class="Overlay-headerFilter">            <div data-target="select-panel.bannerErrorElement" hidden="">
              <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="Banner flash Banner--error flash-error mb-2">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">
                  </p><h2 class="f6 text-normal">Sorry, something went wrong.</h2>
<p></p>
</div></div></x-banner>            </div>
            <remote-input aria-owns="details-user-list-1152624003-body" src="/s22223767-tech/spam-detector/lists?experimental=1" data-target="select-panel.remoteInput" data-view-component="true">
                <primer-text-field class="FormControl width-full FormControl--fullWidth" data-catalyst="">
      <label for="details-user-list-1152624003-filter" class="sr-only FormControl-label position-absolute sr-only FormControl-label">
        Filter
</label>    
  <div class="FormControl-input-wrap FormControl-input-wrap--leadingVisual">
      <span class="FormControl-input-leadingVisualWrap">
        <svg data-target="primer-text-field.leadingVisual" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          <span hidden="hidden" data-target="primer-text-field.leadingSpinner" data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      </span>
    
      <input id="details-user-list-1152624003-filter" type="search" autofocus="autofocus" data-target="primer-text-field.inputElement select-panel.filterInputTextField" aria-describedby="validation-0ea8f54f-5bb2-49a8-b89e-627c15de6796" class="form-control FormControl-input FormControl-medium" name="filter" autocomplete="off" spellcheck="false">
</div>
      <div class="FormControl-inlineValidation" id="validation-0ea8f54f-5bb2-49a8-b89e-627c15de6796" hidden="hidden">
  <span class="FormControl-inlineValidation--visual" data-target="primer-text-field.validationSuccessIcon" hidden=""><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-check-circle-fill">
    <path d="M6 0a6 6 0 1 1 0 12A6 6 0 0 1 6 0Zm-.705 8.737L9.63 4.403 8.392 3.166 5.295 6.263l-1.7-1.702L2.356 5.8l2.938 2.938Z"></path>
</svg></span>
  <span class=" FormControl-inlineValidation--visual" data-target="primer-text-field.validationErrorIcon"><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg></span>
  <span></span>
</div>
    
</primer-text-field>
</remote-input></div>
</div>      <div data-view-component="true" class="Overlay-body p-0">
        <focus-group direction="vertical" mnemonics="" retain="">
          <live-region data-target="select-panel.liveRegion"><template shadowrootmode="open">
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style>
<div id="polite" aria-live="polite" aria-atomic="true"></div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region>
          <div data-fetch-strategy="remote" data-target="select-panel.list" data-view-component="true">
            <div id="details-user-list-1152624003-body">
                
                  <div id="details-user-list-1152624003-list" aria-disabled="true" aria-busy="true" data-view-component="true" class="SelectPanel-loadingPanel mt-2 mb-2 d-flex flex-items-start flex-justify-center text-center">
                    <div data-hide-on-error="" class="pt-2">
                      <span data-target="select-panel.bodySpinner" data-view-component="true">
  <svg aria-label="Loading content..." style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" role="img" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg></span>
                    </div>
                    <div data-show-on-error="" hidden="" data-target="select-panel.fragmentErrorElement">
                        <div class="pt-2 pb-2">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert color-fg-danger">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
                          <h2 class="f5 mt-2">Sorry, something went wrong.</h2>
                        </div>
                    </div>
</div>            </div>
            <div data-target="select-panel.noResults" class="SelectPanel-emptyPanel" hidden="">
              <h2 class="v-align-middle m-3 f5">No results found</h2>
            </div>
</div>        </focus-group>
</div>      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">        <button data-repository-id="1152624003" type="button" data-view-component="true" class="js-user-lists-create-trigger Button--primary Button--medium Button Button--fullWidth">  <span class="Button-content">
    <span class="Button-label"><svg size="small" class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg>
          Create list</span>
  </span>
</button>
</div>
</dialog>  </dialog-helper>
</select-panel>  </user-list-menu>
  <template class="js-user-list-create-dialog-template" data-label="Create list"></template>


</div>
    <div data-view-component="true" class="unstarred BtnGroup icon-button-group flex-1 ml-0">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent" data-turbo="false" action="https://github.com/s22223767-tech/spam-detector/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="HQxMIkepCYwoUISx8ElEV1mp9GhFslC0ZOz_JG5_2GQYZU1HsBJLQk4BRcrHlpoSsgb-rpVHFJ5uplZGhq-twQ" autocomplete="off">
        <input type="hidden" name="context" value="repository">
        <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:1152624003,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="40a6f56141b5d66d4eabc3302ac83f3867924dd3cb501f015a2c3e8ad8c87001" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" id="icon-button-9e1f551e-4c6e-4696-9403-087904360c50" aria-labelledby="tooltip-4d18ffaf-e616-414b-a286-65faa3227a1c" type="submit" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium js-toggler-target BtnGroup-item rounded-left-2">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star Button-visual">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
</button><tool-tip id="tooltip-4d18ffaf-e616-414b-a286-65faa3227a1c" for="icon-button-9e1f551e-4c6e-4696-9403-087904360c50" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Star this repository</tool-tip>

</form>          <user-list-menu data-controller="user-list-menu" data-repository-id="1152624003" data-update-url="/s22223767-tech/spam-detector/lists">
    <select-panel data-target="user-list-menu.selectPanel" data-select-variant="multiple" data-fetch-strategy="remote" data-open-on-load="false" id="details-user-list-1152624003" anchor-align="end" anchor-side="outside-bottom" data-view-component="true" class="BtnGroup-parent js-user-list-menu" data-catalyst="">
  <dialog-helper>
    <button group_item="true" id="details-user-list-1152624003-button" aria-controls="details-user-list-1152624003-dialog" aria-haspopup="dialog" aria-expanded="false" aria-labelledby="tooltip-97c5787a-10ac-4062-a002-5ba9725b3810" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--small rounded-right-2 rounded-left-0 px-3">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-97c5787a-10ac-4062-a002-5ba9725b3810" for="details-user-list-1152624003-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Add this repository to a list</tool-tip>

    <dialog id="details-user-list-1152624003-dialog" aria-labelledby="details-user-list-1152624003-dialog-title" data-target="select-panel.dialog" style="position: absolute;" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait">
      <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="details-user-list-1152624003-dialog-title">
        Lists
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="details-user-list-1152624003-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  <div data-view-component="true" class="Overlay-headerFilter">            <div data-target="select-panel.bannerErrorElement" hidden="">
              <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="Banner flash Banner--error flash-error mb-2">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">
                  </p><h2 class="f6 text-normal">Sorry, something went wrong.</h2>
<p></p>
</div></div></x-banner>            </div>
            <remote-input aria-owns="details-user-list-1152624003-body" src="/s22223767-tech/spam-detector/lists?experimental=1" data-target="select-panel.remoteInput" data-view-component="true">
                <primer-text-field class="FormControl width-full FormControl--fullWidth" data-catalyst="">
      <label for="details-user-list-1152624003-filter" class="sr-only FormControl-label position-absolute sr-only FormControl-label">
        Filter
</label>    
  <div class="FormControl-input-wrap FormControl-input-wrap--leadingVisual">
      <span class="FormControl-input-leadingVisualWrap">
        <svg data-target="primer-text-field.leadingVisual" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          <span hidden="hidden" data-target="primer-text-field.leadingSpinner" data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
      </span>
    
      <input id="details-user-list-1152624003-filter" type="search" autofocus="autofocus" data-target="primer-text-field.inputElement select-panel.filterInputTextField" aria-describedby="validation-e776bacc-203e-4f0a-a6d6-024274f4ca0c" class="form-control FormControl-input FormControl-medium" name="filter" autocomplete="off" spellcheck="false">
</div>
      <div class="FormControl-inlineValidation" id="validation-e776bacc-203e-4f0a-a6d6-024274f4ca0c" hidden="hidden">
  <span class="FormControl-inlineValidation--visual" data-target="primer-text-field.validationSuccessIcon" hidden=""><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-check-circle-fill">
    <path d="M6 0a6 6 0 1 1 0 12A6 6 0 0 1 6 0Zm-.705 8.737L9.63 4.403 8.392 3.166 5.295 6.263l-1.7-1.702L2.356 5.8l2.938 2.938Z"></path>
</svg></span>
  <span class=" FormControl-inlineValidation--visual" data-target="primer-text-field.validationErrorIcon"><svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg></span>
  <span></span>
</div>
    
</primer-text-field>
</remote-input></div>
</div>      <div data-view-component="true" class="Overlay-body p-0">
        <focus-group direction="vertical" mnemonics="" retain="">
          <live-region data-target="select-panel.liveRegion"><template shadowrootmode="open">
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style>
<div id="polite" aria-live="polite" aria-atomic="true"></div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region>
          <div data-fetch-strategy="remote" data-target="select-panel.list" data-view-component="true">
            <div id="details-user-list-1152624003-body">
                
                  <div id="details-user-list-1152624003-list" aria-disabled="true" aria-busy="true" data-view-component="true" class="SelectPanel-loadingPanel mt-2 mb-2 d-flex flex-items-start flex-justify-center text-center">
                    <div data-hide-on-error="" class="pt-2">
                      <span data-target="select-panel.bodySpinner" data-view-component="true">
  <svg aria-label="Loading content..." style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" role="img" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg></span>
                    </div>
                    <div data-show-on-error="" hidden="" data-target="select-panel.fragmentErrorElement">
                        <div class="pt-2 pb-2">
                          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert color-fg-danger">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
                          <h2 class="f5 mt-2">Sorry, something went wrong.</h2>
                        </div>
                    </div>
</div>            </div>
            <div data-target="select-panel.noResults" class="SelectPanel-emptyPanel" hidden="">
              <h2 class="v-align-middle m-3 f5">No results found</h2>
            </div>
</div>        </focus-group>
</div>      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">        <button data-repository-id="1152624003" type="button" data-view-component="true" class="js-user-lists-create-trigger Button--primary Button--medium Button Button--fullWidth">  <span class="Button-content">
    <span class="Button-label"><svg size="small" class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg>
          Create list</span>
  </span>
</button>
</div>
</dialog>  </dialog-helper>
</select-panel>  </user-list-menu>
  <template class="js-user-list-create-dialog-template" data-label="Create list"></template>


</div></div>
          </div>
          <div class="d-flex flex-row gap-2">
            

          </div>
        </div>

    

    <div class="mb-3">
        


<ul class="d-flex flex-wrap mb-2 gap-2" aria-label="Repository details">
  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/s22223767-tech/spam-detector/stargazers">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-1">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
    <span class="text-bold color-fg-default">0</span>
    stars
</a>  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/s22223767-tech/spam-detector/forks">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-1">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
    <span class="text-bold color-fg-default">0</span>
    forks
</a>  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/s22223767-tech/spam-detector/watchers">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-1">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
    <span class="text-bold color-fg-default">0</span>
    watching
</a>  <include-fragment loading="lazy" src="/s22223767-tech/spam-detector/branch-and-tag-count" data-nonce="v2:5ab2f79a-db96-aa11-1d90-8521afcbcb50" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
    <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/s22223767-tech/spam-detector/branches">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch mr-1">
    <path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path>
</svg>
    <span class="color-fg-muted">Branches</span>
</a><a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/s22223767-tech/spam-detector/tags">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag mr-1">
    <path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path>
</svg>
    <span class="color-fg-muted">Tags</span>
</a>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/s22223767-tech/spam-detector" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/s22223767-tech/spam-detector/activity">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-1">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
    <span>Activity</span>
</a>
</ul>

<div class="mb-2 d-flex color-fg-muted">
  <div class="d-flex flex-items-center" style="height: 21px">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-globe flex-shrink-0 mr-2">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM5.78 8.75a9.64 9.64 0 0 0 1.363 4.177c.255.426.542.832.857 1.215.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a9.927 9.927 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.507 6.507 0 0 0 4.666 5.5c-.123-.181-.24-.365-.352-.552-.715-1.192-1.437-2.874-1.581-4.948Zm-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948.12-.197.237-.381.353-.552a6.507 6.507 0 0 0-4.666 5.5Zm10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948-.12.197-.237.381-.353.552a6.507 6.507 0 0 0 4.666-5.5Zm2.733-1.5a6.507 6.507 0 0 0-4.666-5.5c.123.181.24.365.353.552.714 1.192 1.436 2.874 1.58 4.948Z"></path>
</svg>
  </div>
  <span class="flex-auto min-width-0 width-fit">
    Public repository
  </span>
</div>

    </div>
  </div>

</div>

          <div class="border-bottom  mx-xl-5 "></div>
        </div>

  </div>



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class=""><div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/s22223767-tech/spam-detector?resume=1">Open in codespace</a>




    
      
  <h1 class="sr-only">s22223767-tech/spam-detector</h1>
  <div class="clearfix container-xl px-md-4 px-lg-5 px-3">
    <div>

  <div style="max-width: 100%" data-view-component="true" class="Layout Layout--flowRow-until-md react-repos-overview-margin Layout--sidebarPosition-end Layout--sidebarPosition-flowRow-end">
  <div data-view-component="true" class="Layout-main">      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.197622a63ecf569d.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/12365.56c0b14954ccf022.module.css">

<react-partial partial-name="repos-overview" data-ssr="true" data-attempted-ssr="true" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"initialPayload":{"allShortcutsEnabled":true,"path":"/","repo":{"id":1152624003,"defaultBranch":"main","name":"spam-detector","ownerLogin":"s22223767-tech","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2026-02-08T12:14:24.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/247223143?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":{"id":247223143,"login":"s22223767-tech","userEmail":"s22223767@gmail.com"},"refInfo":{"name":"main","listCacheKey":"v0:1770533064.0","canEdit":true,"refType":"branch","currentOid":"2fc64dccc90c2858c2ef0f9fa6288d33a37986a1"},"tree":{"items":[{"name":"README.md","path":"README.md","contentType":"file"},{"name":"app.py","path":"app.py","contentType":"file"},{"name":"requirements.txt","path":"requirements.txt","contentType":"file"},{"name":"spam_model.pkl","path":"spam_model.pkl","contentType":"file"},{"name":"vectorizer.pkl","path":"vectorizer.pkl","contentType":"file"}],"totalCount":5,"templateDirectorySuggestionUrl":null,"readme":null,"showBranchInfobar":false},"fileTree":null,"fileTreeProcessingTime":null,"foldersToFetch":[],"userNameDisplayConfiguration":null,"treeExpanded":false,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"isOverview":true,"overview":{"banners":{"shouldRecommendReadme":true,"isPersonalRepo":false,"showUseActionBanner":false,"actionSlug":null,"actionId":null,"showProtectBranchBanner":false,"transactionalMessageBanner":null,"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_repo","releasePath":"/s22223767-tech/spam-detector/releases/new?marketplace=true","showPublishActionBanner":false},"interactionLimitBanner":null,"showInvitationBanner":false,"inviterName":null,"actionsMigrationBannerInfo":{"releaseTags":[],"showImmutableActionsMigrationBanner":false,"initialMigrationStatus":null},"showDeployBanner":false,"detectedStack":{"framework":null,"packageManager":null}},"codeButton":{"contactPath":"/contact","isEnterprise":false,"local":{"protocolInfo":{"httpAvailable":true,"sshAvailable":true,"httpUrl":"https://github.com/s22223767-tech/spam-detector.git","showCloneWarning":true,"sshUrl":"git@github.com:s22223767-tech/spam-detector.git","sshCertificatesRequired":false,"sshCertificatesAvailable":null,"ghCliUrl":"gh repo clone s22223767-tech/spam-detector","defaultProtocol":"http","newSshKeyUrl":"/settings/ssh/new","setProtocolPath":"/users/set_protocol"},"platformInfo":{"cloneUrl":"https://desktop.github.com","showVisualStudioCloneButton":false,"visualStudioCloneUrl":"https://windows.github.com","showXcodeCloneButton":false,"xcodeCloneUrl":"xcode://clone?repo=https%3A%2F%2Fgithub.com%2Fs22223767-tech%2Fspam-detector","zipballUrl":"/s22223767-tech/spam-detector/archive/refs/heads/main.zip"}},"repoPolicyInfo":{"allowed":true,"canBill":true,"changesWouldBeSafe":true,"disabledByBusiness":false,"disabledByOrganization":false,"hasIpAllowLists":false},"currentUserIsEnterpriseManaged":false,"enterpriseManagedBusinessName":null,"codespacesEnabled":true,"hasAccessToCodespaces":true},"popovers":{"rename":null,"renamedParentRepo":null},"commitCount":"4","overviewFiles":[{"displayName":"README.md","repoName":"spam-detector","refName":"main","path":"README.md","preferredFileType":"readme","tabName":"README","richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch1 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003espam-detector\u003c/h1\u003e\u003ca id=\"user-content-spam-detector\" class=\"anchor\" aria-label=\"Permalink: spam-detector\" href=\"#spam-detector\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003c/article\u003e","loaded":true,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":[{"level":1,"text":"spam-detector","anchor":"spam-detector","htmlText":"spam-detector"}],"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fs22223767-tech%2Fspam-detector"}}],"overviewFilesProcessingTime":0,"copilotSWEAgentEnabled":false,"createFromTemplatePath":"/new?template_name=spam-detector\u0026template_owner=s22223767-tech"}},"appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-66b264d4e6bdb347.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-e709747f43b28c97.js","githubDevUrl":"https://github.dev/","enabled_features":{"copilot_workspace":false,"code_nav_ui_events":false,"react_blob_overlay":true}}}}</script>
  <div data-target="react-partial.reactRoot">   <div class="OverviewContent-module__Box__PF75K"><div class="OverviewHeader-module__Box__cC1RH"></div><div class="OverviewContent-module__Box_1__MPS0U"><div class="OverviewContent-module__Box_2__Di8Pb"><div class="OverviewContent-module__Box_3__wzlJx"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" data-hotkey="w" aria-label="main branch" data-testid="anchor-button" class="prc-Button-ButtonBase-9n-Xk overview-ref-selector width-full RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn__a3WK3" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector" fdprocessedid="2grdjq" style="min-width: 0px;"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer__yaf4p"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader__XtXRG"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer__Di3rk"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText__w_fmP">&nbsp;main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey="w" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="OverviewContent-module__Box_4__qf73o"><a type="button" href="https://github.com/s22223767-tech/spam-detector/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button___Uotu" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span><strong class="color-fg-default">1 </strong>Branch</span></span></span></a><a type="button" href="https://github.com/s22223767-tech/spam-detector/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button___Uotu" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span><strong class="color-fg-default">0 </strong>Tags</span></span></span></a></div><div class="OverviewContent-module__Box_5__Zc3i7"><a type="button" aria-label="Go to Branches page" href="https://github.com/s22223767-tech/spam-detector/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1__vmS6D" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></a><a type="button" aria-label="Go to Tags page" href="https://github.com/s22223767-tech/spam-detector/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1__vmS6D" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></a></div></div><div class="OverviewContent-module__Box_6__Y_Yb_"><div class="OverviewContent-module__Box_7__JuRXo"><button hidden="" data-hotkey="t,Shift+T"></button><div class="OverviewContent-module__Box_8__UZCZh"><div class="Box-sc-62in7e-0 OverviewContent-module__FileResultsList__EjrTH"><span class="TextInput__StyledTextInput-sc-ttxlvl-0 d-flex FileResultsList-module__FilesSearchBox__ivVkc TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id="_r_5v_" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby="_r_5v_ _r_60_" data-component="input" class="prc-components-Input-IwWrt" type="text" value="" fdprocessedid="60tuu"><span class="TextInput-icon" id="_r_60_" aria-hidden="true"><kbd>t</kbd></span></span></div></div><div class="OverviewContent-module__Box_9__bqMPw"><button type="button" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Go to file</span></span></button></div><div><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Add file</h2><button type="button" aria-label="Add file" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" id="_r_66_" fdprocessedid="13ofr9"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><span class="react-directory-add-file-button">Add file<svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span><svg aria-hidden="true" focusable="false" class="octicon octicon-plus react-directory-add-file-icon" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></span></span></button></div></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-size="medium" data-variant="primary" id="_r_69_" fdprocessedid="0j6eu8"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-code hide-sm" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Code</span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><div class="OverviewContent-module__Box_10__mGSb4"><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_6d_" id="_r_6b_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_r_6d_" popover="auto">Open more actions menu</span></div></div></div><div class="OverviewContent-module__Box_11__F19kY"><div data-hpc="true"><button hidden="" data-testid="focus-next-element-button" data-hotkey="j"></button><button hidden="" data-testid="focus-previous-element-button" data-hotkey="k"></button><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="folders-and-files">Folders and files</h2><table class="Table-module__Box__HZKiQ" aria-labelledby="folders-and-files"><thead class="DirectoryContent-module__OverviewHeaderRow__hOrKy Table-module__Box_1__VacXC"><tr class="Table-module__Box_2__PBp9s"><th colspan="2" class="DirectoryContent-module__Box__iC_5e"><span class="text-bold">Name</span></th><th colspan="1" class="DirectoryContent-module__Box_1__fuSBO"><span class="text-bold">Name</span></th><th class="hide-sm"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit message" style="--truncate-max-width: 125px;"><span class="text-bold">Last commit message</span></div></th><th colspan="1" class="DirectoryContent-module__Box_2__Ccrx7"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit date" style="--truncate-max-width: 125px;"><span class="text-bold">Last commit date</span></div></th></tr></thead><tbody><tr class="DirectoryContent-module__Box_3__gl6dE"><td colspan="3" class="bgColor-muted p-1 rounded-top-2"><div class="LatestCommit-module__Box__B25ZT"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1__YkEgg"><div class="CommitAttribution-module__CommitAttributionContainer__I_rfs"><div data-testid="author-avatar" class="Box-sc-62in7e-0 AuthorAvatar-module__AuthorAvatarContainer__n0MVc"><a class="Link__StyledLink-sc-1syctfj-0 prc-Link-Link-9ZwDx" href="https://github.com/s22223767-tech" data-testid="avatar-icon-link" data-hovercard-url="/users/s22223767-tech/hovercard" data-hovercard-type="user" octo-click="hovercard-link-click" octo-dimensions="link_type:self" aria-keyshortcuts="Alt+ArrowUp"><img data-component="Avatar" class="Box-sc-62in7e-0 kglDHV AuthorAvatar-module__authorAvatarImage__a3R8x prc-Avatar-Avatar-0xaUi" alt="s22223767-tech" width="20" height="20" data-testid="github-avatar" aria-label="s22223767-tech" src="./app_files/247223143(2)" style="--avatarSize-regular: 20px;"></a><a class="Link__StyledLink-sc-1syctfj-0 iIGVMW AuthorAvatar-module__authorHoverableLink__MHTT8 prc-Link-Link-9ZwDx" data-muted="true" href="https://github.com/s22223767-tech/spam-detector/commits?author=s22223767-tech" aria-label="commits by s22223767-tech" data-hovercard-url="/users/s22223767-tech/hovercard" data-hovercard-type="user" octo-click="hovercard-link-click" octo-dimensions="link_type:self" aria-keyshortcuts="Alt+ArrowUp">s22223767-tech</a></div><span class=""></span></div><div class="d-none d-sm-flex LatestCommit-module__Box_2__pSPKJ"><div class="Truncate flex-items-center f5"><span class="Text__StyledText-sc-1klmep6-0 Truncate-text prc-Text-Text-9mHv3" data-testid="latest-commit-html"><a href="https://github.com/s22223767-tech/spam-detector/commit/2fc64dccc90c2858c2ef0f9fa6288d33a37986a1" class="Link--secondary" data-pjax="true" data-hovercard-url="/s22223767-tech/spam-detector/commit/2fc64dccc90c2858c2ef0f9fa6288d33a37986a1/hovercard" aria-keyshortcuts="Alt+ArrowUp">Create requirements.txt</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time tense="past" datetime="2026-02-08T06:53:46.000Z" title="Feb 8, 2026, 12:23 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-9ZwDx" aria-label="Commit 2fc64dc" data-hovercard-url="/s22223767-tech/spam-detector/commit/2fc64dccc90c2858c2ef0f9fa6288d33a37986a1/hovercard" data-hovercard-type="commit" octo-click="hovercard-link-click" octo-dimensions="link_type:self" aria-keyshortcuts="Alt+ArrowUp" href="https://github.com/s22223767-tech/spam-detector/commit/2fc64dccc90c2858c2ef0f9fa6288d33a37986a1" data-discover="true">2fc64dc</a>&nbsp;·&nbsp;<relative-time tense="past" datetime="2026-02-08T06:53:46.000Z" title="Feb 8, 2026, 12:23 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="https://github.com/s22223767-tech/spam-detector/commits/main/" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">4 Commits</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-9n-Xk LatestCommit-module__IconButton__mkJr_ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_6t_"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_6t_" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><a aria-label="View commit history for this file." href="https://github.com/s22223767-tech/spam-detector/commits/main/" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="_r_6g_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" role="tooltip" aria-hidden="true" id="_r_6g_" popover="auto">4 Commits</span></div></div></div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-0"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Initial commit" class="Link--secondary" href="https://github.com/s22223767-tech/spam-detector/commit/add2315388b968ffad28602613c3391891409dd1">Initial commit</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2026-02-08T06:44:24.000Z" title="Feb 8, 2026, 12:14 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-1"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="app.py" aria-label="app.py, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/app.py" data-discover="true">app.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="app.py" aria-label="app.py, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/app.py" data-discover="true">app.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Create app.py" class="Link--secondary" href="https://github.com/s22223767-tech/spam-detector/commit/71ef396e4dd00f4e8d2182082ac6dac4e4567aa8">Create app.py</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2026-02-08T06:47:04.000Z" title="Feb 8, 2026, 12:17 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-2"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="requirements.txt" aria-label="requirements.txt, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/requirements.txt" data-discover="true">requirements.txt</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="requirements.txt" aria-label="requirements.txt, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/requirements.txt" data-discover="true">requirements.txt</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Create requirements.txt" class="Link--secondary" href="https://github.com/s22223767-tech/spam-detector/commit/2fc64dccc90c2858c2ef0f9fa6288d33a37986a1">Create requirements.txt</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2026-02-08T06:53:46.000Z" title="Feb 8, 2026, 12:23 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-3"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="spam_model.pkl" aria-label="spam_model.pkl, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/spam_model.pkl" data-discover="true">spam_model.pkl</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="spam_model.pkl" aria-label="spam_model.pkl, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/spam_model.pkl" data-discover="true">spam_model.pkl</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add files via upload" class="Link--secondary" href="https://github.com/s22223767-tech/spam-detector/commit/6231242299a5a223ff3b81817e38ea119382c69c">Add files via upload</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2026-02-08T06:52:39.000Z" title="Feb 8, 2026, 12:22 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-4"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="vectorizer.pkl" aria-label="vectorizer.pkl, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/vectorizer.pkl" data-discover="true">vectorizer.pkl</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="vectorizer.pkl" aria-label="vectorizer.pkl, (File)" class="Link--primary" href="https://github.com/s22223767-tech/spam-detector/blob/main/vectorizer.pkl" data-discover="true">vectorizer.pkl</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add files via upload" class="Link--secondary" href="https://github.com/s22223767-tech/spam-detector/commit/6231242299a5a223ff3b81817e38ea119382c69c">Add files via upload</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2026-02-08T06:52:39.000Z" title="Feb 8, 2026, 12:22 PM GMT+5:30"><template shadowrootmode="open">4 days ago</template>Feb 8, 2026</relative-time></div></td></tr><tr class="d-none DirectoryContent-module__Box_4__RhIsE" data-testid="view-all-files-row"><td colspan="3" class="DirectoryContent-module__Box_5__GaE8N"><div><button class="prc-Link-Link-9ZwDx">View all files</button></div></td></tr></tbody></table><document-dropzone data-catalyst=""><div class="repo-file-upload-tree-target js-upload-manifest-tree-view" data-testid="dragzone" data-drop-url="/s22223767-tech/spam-detector/upload/main" data-target="document-dropzone.dropContainer"><div class="repo-file-upload-outline"><div class="repo-file-upload-slate"><div class="fgColor-muted"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 24 24" width="32" height="32" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v18a.5.5 0 0 0 .5.5h14a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4Zm10 0v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5Z"></path></svg></div><h2 aria-hidden="true">Drop to upload your files</h2></div></div></div></document-dropzone></div><div class="OverviewRepoFiles-module__Box_1__OXeac"><div class="OverviewRepoFiles-module__Box_2__zsLGk"><div itemscope="" itemtype="https://schema.org/abstract" class="OverviewRepoFiles-module__Box_3__bBU1C"><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository files navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj OverviewRepoFiles-module__UnderlineNav__QbWWv" aria-label="Repository files" data-variant="inset"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s22223767-tech/spam-detector#" aria-current="page" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="README">README</span></a></li></ul></nav><button data-component="IconButton" type="button" data-hotkey="e,Shift+E" class="prc-Button-ButtonBase-9n-Xk IconButton__StyledIconButton-sc-i53dt6-0 jCdPVA prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_6j_" fdprocessedid="4lti9"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_6j_" popover="auto">Edit file</span></div><div class="Box-sc-62in7e-0 js-snippet-clipboard-copy-unpositioned DirectoryRichtextContent-module__SharedMarkdownContent__hHXUL" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">spam-detector</h1><a id="user-content-spam-detector" class="anchor" aria-label="Permalink: spam-detector" href="https://github.com/s22223767-tech/spam-detector#spam-detector"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
</article></div></div></div></div></div>   <script type="application/json" id="__PRIMER_DATA__r_5m___">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


      <input type="hidden" value="hefn_sLTSdXQoL9l7Gfv40iq0xLvq_sBH5YilwZa70gS-8rWescnB5XQMNtpHPZKiv7iBxXpNhfOEx3nNg7WgQ" data-csrf="true" id="react-codespace-csrf">
</div>
  <div data-view-component="true" class="Layout-sidebar">      

<div class="BorderGrid about-margin">
  <div class="BorderGrid-row">
    <div class="BorderGrid-cell">
        <details class="details-reset details-overlay details-overlay-dark ">
          <summary class="float-right" role="button">
        <div class="Link--secondary pt-1 pl-2">
          <svg aria-label="Edit repository metadata" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear float-right">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </div>
      </summary>

  <details-dialog class="Box d-flex flex-column anim-fade-in fast Box-overlay--wide overflow-x-hidden" aria-label="Edit repository details" role="dialog" aria-modal="true">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
        <h1 class="Box-title">Edit repository details</h1>
    </div>
      <div class="Box-body overflow-auto">
              <div class="js-topic-form-area">
        <!-- '"` --><!-- </textarea></xmp> --><form id="repo_metadata_form" data-turbo="false" action="https://github.com/s22223767-tech/spam-detector/settings/update_meta" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" autocomplete="off"><input type="hidden" name="authenticity_token" value="cVzUNGUkUb6MGPJ8XUB8gomWSCZAQ-mrkSWhT_hgn7UgXfXxRgnTqkd3RiZpmtO11FZkZM4KgQsNYucspBQjuw">
          <div class="form-group mt-0 mb-3 js-length-limited-input-container">
            <div class="mb-2">
              <label for="repo_description">Description</label>
            </div>
            <input type="text" id="repo_description" class="form-control input-contrast width-full js-length-limited-input" name="repo_description" placeholder="Short description of this repository" autofocus="" value="" data-input-max-length="350" data-warning-length="50" data-warning-text="{{remaining}} characters remaining">
            <div class="d-none mt-1 js-length-limited-input-warning text-right color-fg-danger"></div>
          </div>
          <div class="form-group my-3">
            <div class="mb-2">
              <label for="repo_homepage">Website</label>
            </div>
             <input type="url" id="repo_homepage" class="color-bg-default form-control input-contrast width-full" name="repo_homepage" value="" placeholder="Enter a valid URL">
          </div>
          <div class="width-full tag-input-container topic-input-container d-inline-block js-tag-input-container">
            <div class="js-tag-input-wrapper">
              <div class="form-group my-0">
                <div class="mb-2">
                  <label for="repo_topics" class="d-block">Topics <span class="text-normal color-fg-muted">(separate with spaces)</span></label>
                </div>
                <div class="tag-input form-control d-inline-block color-bg-default py-0 position-relative">
                  <ul class="js-tag-input-selected-tags d-inline">
                    <li class="d-none topic-tag-action my-1 mr-1 f6 float-left js-tag-input-tag js-template">
                      <span class="js-placeholder-tag-name"></span>
                      <button type="button" class="delete-topic-button f5 no-underline ml-1 js-remove" tabindex="-1">
                        <svg aria-label="Remove topic" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
                      </button>
                      <input type="hidden" name="repo_topics[]" class="js-topic-input" value="">
                    </li>

                  </ul>

                    <auto-complete src="/s22223767-tech/spam-detector/topic_autocomplete" for="repo-topic-popup">
                      <input type="text" id="repo_topics" class="tag-input-inner form-control color-bg-default short d-inline-block p-0 my-1 border-0" autocomplete="off" autofocus="" role="combobox" aria-controls="repo-topic-popup" aria-expanded="false" aria-autocomplete="list" aria-haspopup="listbox" spellcheck="false">
                      <ul class="suggester border width-full color-bg-default left-0" id="repo-topic-popup" style="top: 100%;" hidden="" aria-label="results" role="listbox"></ul>
                    </auto-complete>
                </div>
              </div>
            </div>
          </div>

          <div class="form-group mt-3 mb-0" role="group" aria-labelledby="hidden_sidebar_options">
            <div class="text-bold mb-2" id="hidden_sidebar_options">Include in the home page</div>
            <label class="d-block mb-2 text-normal">
              <input name="repo_sections[releases]" type="hidden" value="0" autocomplete="off"><input class="mr-1" type="checkbox" value="1" checked="checked" name="repo_sections[releases]" id="repo_sections_releases"> Releases
            </label>
            <label class="d-block mb-2 text-normal">
              <input name="repo_sections[packages]" type="hidden" value="0" autocomplete="off"><input class="mr-1" type="checkbox" value="1" checked="checked" name="repo_sections[packages]" id="repo_sections_packages"> Packages
            </label>

            <label class="d-block text-normal">
              <input name="repo_sections[deployments]" type="hidden" value="0" autocomplete="off"><input class="mr-1" type="checkbox" value="1" checked="checked" name="repo_sections[deployments]" id="repo_sections_deployments"> Deployments
            </label>
          </div>
</form>      </div>

      </div>
        <div class="Box-footer">
                <div class="form-actions">
        <button type="submit" class="btn btn-primary" form="repo_metadata_form">Save changes</button>
        <button type="reset" class="btn" data-close-dialog="" form="repo_metadata_form">Cancel</button>
      </div>

        </div>
  </details-dialog>
</details>
<div class="hide-sm hide-md">
  <h2 class="mb-3 h4">About</h2>

      <div class="f4 my-3 color-fg-muted text-italic">
        No description, website, or topics provided.
      </div>


    <h3 class="sr-only">Resources</h3>
    <div class="mt-2">
      <a class="Link--muted" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="https://github.com/s22223767-tech/spam-detector#readme-ov-file">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        Readme
</a>    </div>

  





  <include-fragment src="/s22223767-tech/spam-detector/hovercards/citation/sidebar_partial?tree_name=main" data-nonce="v2:5ab2f79a-db96-aa11-1d90-8521afcbcb50" data-view-component="true" class="is-error"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/s22223767-tech/spam-detector" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>
    <div class="mt-2">
      <a href="https://github.com/s22223767-tech/spam-detector/activity" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-2">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
        <span class="color-fg-muted">Activity</span></a>    </div>


    <h3 class="sr-only">Stars</h3>
    <div class="mt-2">
      <a href="https://github.com/s22223767-tech/spam-detector/stargazers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        <strong>0</strong>
        stars</a>    </div>

    <h3 class="sr-only">Watchers</h3>
    <div class="mt-2">
      <a href="https://github.com/s22223767-tech/spam-detector/watchers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
        <strong>0</strong>
        watching</a>    </div>

    <h3 class="sr-only">Forks</h3>
    <div class="mt-2">
      <a href="https://github.com/s22223767-tech/spam-detector/forks" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
        <strong>0</strong>
        forks</a>    </div>


</div>

    </div>
  </div>

  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          <h2 class="h4 mb-3" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
  <a href="https://github.com/s22223767-tech/spam-detector/releases" data-view-component="true" class="Link--primary no-underline Link" data-turbo-frame="repo-content-turbo-frame">Releases</a></h2>

    <div class="text-small color-fg-muted">No releases published</div>
    <div class=" text-small"><a class="Link--inTextBlock" href="https://github.com/s22223767-tech/spam-detector/releases/new">Create a new release</a></div>

        </div>
      </div>

  
  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          
  <h2 class="h4 mb-3">
  <a href="https://github.com/users/s22223767-tech/packages?repo_name=spam-detector" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Packages
      <span title="0" hidden="hidden" data-view-component="true" class="Counter ml-1">0</span></a></h2>


      <div class="text-small color-fg-muted">
        No packages published <br>
          <a class="Link--inTextBlock" href="https://github.com/s22223767-tech/spam-detector/packages">Publish your first package</a>
      </div>



        </div>
      </div>

  
  
  
  
      <div class="BorderGrid-row">
        <div class="BorderGrid-cell">
          <h2 class="h4 mb-3">Languages</h2>
<div class="mb-2">
  <span data-view-component="true" class="Progress">
    <span style="background-color:#3572A5 !important;;width: 100.0%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="https://github.com/s22223767-tech/spam-detector/search?l=python" data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#3572A5;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">Python</span>
          <span>100.0%</span>
        </a>
    </li>
</ul>

        </div>
      </div>

  
        <div class="BorderGrid-row js-notice">
  <div class="BorderGrid-cell">
    <div data-view-component="true" class="Subhead border-bottom-0 mb-2">
  <h2 data-view-component="true" class="h4 Subhead-heading Subhead-heading--large">        Suggested workflows
</h2>
  <div data-view-component="true" class="Subhead-description">         Based on your tech stack
</div>
  
</div>    <ol class="list-style-none">
        <li class="list-style-none">
          <div data-view-component="true" class="mb-2 p-3 border rounded-2">
  <div data-view-component="true" class="d-flex flex-items-stretch">
    <div aria-hidden="true" style="color: #3572A5 !important; background-color: var(--bgColor-white, var(--color-scale-white)) !important; width: 32px !important; height: 32px !important; min-width: 32px !important;" data-view-component="true" class="CircleBadge">
      <img class="CircleBadge-icon" src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBoZWlnaHQ9IjQ4IiB3aWR0aD0iNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMjMuNTkxYy4wMi0uMDY2LjAzNi0uMTM0LjA0NS0uMjAyLjAzNy0uNjk3LjA0NS0xLjQwMi4xMi0yLjEuMTE3LTIuMjYuODcxLTQuNDQgMi4xNzUtNi4yOWE2LjMyMiA2LjMyMiAwIDAxNS4wODUtMi41NjVIMjMuNjFjLjMxNSAwIC4zMTUgMCAuMzE1LS4zMTV2LTEuMTI1YzAtLjIzMi0uMDY4LS4yODQtLjI4NS0uMjg0SDEyLjYyM2MtLjE4OCAwLS4yNTUtLjA1My0uMjU1LS4yNDhWNC45NjZjLjAzNi0uNzk2LjM2OC0xLjU1LjkzLTIuMTE1YTYuNjgzIDYuNjgzIDAgMDEyLjcwNy0xLjc0NyAxNi42NjggMTYuNjY4IDAgMDEzLjktLjg5MiAzMi44NDMgMzIuODQzIDAgMDE1LjQ4Mi0uMTY1YzEuOTcyLjAzNyAzLjkyMy4zOTkgNS43NzYgMS4wNzJhNy4wOTUgNy4wOTUgMCAwMTMuMjQgMi4yNSA0LjUzNiA0LjUzNiAwIDAxLjk0NSAzLjA3NGMtLjA0NS45MyAwIDEuODY3IDAgMi44MDR2NS4xOWMwIDEuMDE5IDAgMi4wNDYtLjA0NSAzLjA1OGE1LjQyMSA1LjQyMSAwIDAxLTMuNTE4IDUuMDQgOC4wNDIgOC4wNDIgMCAwMS0zLjE0My41OTloLTExLjQ2YTYuNTQgNi41NCAwIDAwLTMuNDUuOTA3IDUuOTk5IDUuOTk5IDAgMDAtMi42NDcgMy43MDQgOC42NTYgOC42NTYgMCAwMC0uMzIzIDIuMzc3djUuMTk2YzAgLjM0NSAwIC4zMzgtLjM0NS4zNDUtMS4yNDUgMC0yLjQ5LjAzOC0zLjc1IDBBNS4yNSA1LjI1IDAgMDEzLjM0NSAzNC4zYTguMjQ4IDguMjQ4IDAgMDEtMi4yOTUtMy41NTQgMTUuMTQyIDE1LjE0MiAwIDAxLS44NDgtMy44NDdjLS4wNzUtLjg0LS4xMDUtMS42OC0uMTU3LTIuNTEyQTIuNDc1IDIuNDc1IDAgMDAwIDI0LjExdi0uNTE4eiIgZmlsbD0iIzM3NzJhNCIvPjxwYXRoIGQ9Ik0xNS4yMDMgNS43MzhhMi4xMDcgMi4xMDcgMCAxMDIuMTA3LTIuMTIyIDIuMTIzIDIuMTIzIDAgMDAtMi4xMDcgMi4xMjJ6IiBmaWxsPSIjMDAwIi8+PHBhdGggZD0iTTE1LjIwMyA1LjczOGEyLjExIDIuMTEgMCAxMTQuMjIgMCAyLjExIDIuMTEgMCAwMS00LjIyIDB6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTQ4IDI0LjQwMWMtLjAyLjA2Ni0uMDM2LjEzNC0uMDQ1LjIwMy0uMDM3LjY5Ny0uMDQ1IDEuNDAyLS4xMiAyLjFhMTEuOTk1IDExLjk5NSAwIDAxLTIuMTc1IDYuMjkgNi4zMjIgNi4zMjIgMCAwMS01LjA4NSAyLjU3MkgyNC4zOWMtLjMxNSAwLS4zMTUgMC0uMzE1LjMxNXYxLjEyNWMwIC4yMzIuMDY4LjI4NS4yODUuMjg1aDExLjAxOGMuMTg3IDAgLjI1NS4wNTIuMjU1LjI0N3Y1LjQ5NmEzLjIwOSAzLjIwOSAwIDAxLS45MyAyLjExNSA2LjY4MyA2LjY4MyAwIDAxLTIuNzA4IDEuNzQ3IDE2LjY2OSAxNi42NjkgMCAwMS0zLjg5Mi44OTJjLTEuODIuMjA4LTMuNjU0LjI2My01LjQ4My4xNjVhMTcuODc3IDE3Ljg3NyAwIDAxLTUuNzc1LTEuMDcyIDcuMDk1IDcuMDk1IDAgMDEtMy4yNC0yLjI1IDQuNTM2IDQuNTM2IDAgMDEtLjk0NS0zLjA3NGMuMDQ1LS45MyAwLTEuODY3IDAtMi44MDR2LTUuMTljMC0xLjAxOSAwLTIuMDQ2LjA0NS0zLjA1OGE1LjQyIDUuNDIgMCAwMTMuNTE3LTUuMDQgOC4wNDIgOC4wNDIgMCAwMTMuMTQzLS41OTloMTEuNDUzYTYuNTQgNi41NCAwIDAwMy40NS0uOTA3IDYgNiAwIDAwMi42NDctMy43MTIgOC42NiA4LjY2IDAgMDAuMzIzLTIuMzc3di01LjE5NmMwLS4zNDUgMC0uMzM3LjM0NS0uMzQ1IDEuMjQ1IDAgMi40OS0uMDM3IDMuNzUgMGE1LjI1IDUuMjUgMCAwMTMuMzIyIDEuMzY1IDguMjQ5IDguMjQ5IDAgMDEyLjI5NSAzLjU1NCAxNS4xNSAxNS4xNSAwIDAxLjg0IDMuODYxYy4wNzUuODQuMTA1IDEuNjguMTU4IDIuNTEyLjAxLjA5MS4wMjUuMTgxLjA0NS4yNy4wMDUuMTY1LjAwNy4zMzUuMDA3LjUxeiIgZmlsbD0iI2ZmZGE0YiIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTA3IDIuMTA3IDAgMTAtMi4xMDcgMi4xMjIgMi4xMjMgMi4xMjMgMCAwMDIuMTA3LTIuMTIyeiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTEgMi4xMSAwIDExLTQuMjIgMCAyLjExIDIuMTEgMCAwMTQuMjIgMHoiIGZpbGw9IiNmZmYiLz48L3N2Zz4=" alt="Pylint logo">
</div>
    <div data-view-component="true" class="d-flex flex-column">
      <span data-view-component="true" class="f5 text-bold ml-2">Pylint</span>
      <span data-view-component="true" class="color-fg-muted ml-2 text-small"></span>
</div>    <a href="https://github.com/s22223767-tech/spam-detector/new/main?filename=.github%2Fworkflows%2Fpylint.yml&amp;workflow_template=ci%2Fpylint" data-hydro-click="{&quot;event_type&quot;:&quot;actions.onboarding_setup_workflow_click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:1152624003,&quot;workflow_template&quot;:&quot;ci/pylint&quot;,&quot;view_section&quot;:&quot;repository_sidebar&quot;,&quot;view_rank&quot;:1,&quot;templates_count&quot;:3,&quot;template_creator&quot;:null,&quot;new_with_filter_view&quot;:false,&quot;correlation_id&quot;:&quot;DB16:5F6C9:CF63A0:F103F7:698DB11B&quot;,&quot;category&quot;:&quot;Continuous integration&quot;,&quot;search_query&quot;:null,&quot;template_source_visibility&quot;:&quot;shared&quot;,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="d45c2acac975bb6ef6b636af062db1e24e4a8a30468a90d659eb189f58eaca9c" style="min-width: 80px" aria-describedby="pylint-description" data-view-component="true" class="Button--secondary Button--small Button ml-auto">  <span class="Button-content">
    <span class="Button-label">Configure<span class="sr-only">&nbsp;Pylint</span></span>
  </span>
</a>
</div>  <span id="pylint-description" aria-hidden="true" data-view-component="true" class="d-flex color-fg-muted f6 ml-5 mt-1 pl-2">Lint a Python application with pylint.</span>
</div>
        </li>
        <li class="list-style-none">
          <div data-view-component="true" class="mb-2 p-3 border rounded-2">
  <div data-view-component="true" class="d-flex flex-items-stretch">
    <div aria-hidden="true" style="color: #00ADD8 !important; background-color: var(--bgColor-white, var(--color-scale-white)) !important; width: 32px !important; height: 32px !important; min-width: 32px !important;" data-view-component="true" class="CircleBadge">
      <img class="CircleBadge-icon" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyBmaWxsPSJub25lIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAxNDAgMTQwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzEpIiBjbGlwLXBhdGg9InVybCgjYSkiPgo8cGF0aCBkPSJtMTYxLjUzIDMuMDk5NGUtNSAwLjM4NS0wLjQzNTQzLTcuNDkzLTYuNjIyMi0zLjMxMSAzLjc0NjVjLTAuOTg5IDEuMTE4NC0xLjk5MSAyLjIyMjItMy4wMDggMy4zMTExaC0xMTcuMXY3Ljc5MTlsLTYuODc5OSA0LjI0MDMgMi42MjM0IDQuMjU2NWMxLjM3MzUgMi4yMjg1IDIuNzkyOSA0LjQxOTYgNC4yNTY1IDYuNTcyNHY5My40MjFjLTAuMDMzOSAxZS0zIC0wLjA2NzggMWUtMyAtMC4xMDE4IDJlLTNsLTQuOTk4OSAwLjEwMiAwLjIwMzUgOS45OTggNC44OTcyLTAuMXYxMy43MTZoMTQwdi04OC42ODRjMS40NC0yLjA3MzQgMi44NC00LjE4MyA0LjE5Ni02LjMyODIgMi4yNzktMy40MjkyIDMuOTcxLTYuMzYxMyA1LjEwMy04LjQ1NzkgMC41Ny0xLjA1NCAwLjk5OC0xLjg5ODYgMS4yOS0yLjQ5MTIgMC4xNDYtMC4yOTY0IDAuMjU4LTAuNTI5OSAwLjMzNi0wLjY5NTMgMC4wMzktMC4wODI3IDAuMDY5LTAuMTQ4NCAwLjA5MS0wLjE5NjRsMC4wMjctMC4wNTg3IDllLTMgLTAuMDE5MiAzZS0zIC0wLjAwNzEgMWUtMyAtMC4wMDI5IDFlLTMgLTAuMDAxM2MwLTZlLTQgMC0wLjAwMTEtNC41NTctMi4wNTc4bDQuNTU3IDIuMDU2NyAyLjA1Ny00LjU1NzUtOS4xMTUtNC4xMTMyLTIuMDU0IDQuNTUxOHYxZS0zbC0xZS0zIDllLTQgLTFlLTMgMC4wMDE3djJlLTNsLThlLTMgMC4wMTc0Yy0wLjAxMSAwLjAyMzQtMC4wMyAwLjA2NDItMC4wNTcgMC4xMjE2LTAuMDU0IDAuMTE1LTAuMTQxIDAuMjk2Ny0wLjI2MSAwLjUzOTktMC4yMzkgMC40ODY2LTAuNjExIDEuMjE4OC0xLjExNiAyLjE1NS0wLjE1NSAwLjI4NTktMC4zMjIgMC41OTA3LTAuNTAxIDAuOTEzMXYtMzIuNjl6bTAgMGgtMTMuNDI3Yy0yMi4wNDYgMjMuNjE4LTUwLjU5MSA0MC4yNDYtODEuOTkxIDQ3Ljc3OS0xMS44NzUtMTAuNTQxLTIyLjMwNS0yMi44NzEtMzAuODUxLTM2LjczN2wtMi42MjM0LTQuMjU2NS0xLjYzMzEgMS4wMDY1djE1LjA2OWM4LjcwNzYgMTIuODA3IDE4Ljk4MiAyNC4yNTkgMzAuNDgyIDM0LjE1NiAxNi41MyAxNC4yMjYgMzUuNTkxIDI1LjI0MiA1Ni4xNyAzMi40NjEtMTcuNDI0IDExLjM4Ny0zNi45NjIgMTkuNDQ4LTU3LjYxMiAyMy42MDUtOS40Nzc0IDEuOTA3LTE5LjE5IDIuOTkyLTI5LjA0IDMuMTk5djEwLjAwMmwwLjEwMTgtMmUtM2MxMC40ODQtMC4yMTMgMjAuODIzLTEuMzY1IDMwLjkxMS0zLjM5NiAyNS40MDMtNS4xMTMgNDkuMjE3LTE1Ljc5NiA2OS43ODYtMzEuMDkgMTUuMDEtMTEuMTYxIDI4LjI5Mi0yNC43NzkgMzkuMjAxLTQwLjQ4di0xOC42MjZjLTAuOTk2IDEuNzkwOC0yLjM4IDQuMTI3LTQuMTYzIDYuODA4bC0wLjAzMyAwLjA0OTEtMC4wMzEgMC4wNDk4Yy0xMC41MTIgMTYuNjM5LTIzLjc1OSAzMS4wMTUtMzguOTYyIDQyLjY4LTE4Ljg4MS01LjcwOS0zNi41NTUtMTQuNzU4LTUyLjE4LTI2LjY2MiAzMS45ODItOS4xMjkyIDYwLjgyNy0yNy4yNSA4Mi45NjktNTIuMzA0eiIgY2xpcC1ydWxlPSJldmVub2RkIiBmaWxsPSIjZjAzMTAwIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJhIj4KPHBhdGggZD0ibTMxIDI4YzAtMTUuNDY0IDEyLjUzNi0yOCAyOC0yOGg4NGMxNS40NjQgMCAyOCAxMi41MzYgMjggMjh2ODRjMCAxNS40NjQtMTIuNTM2IDI4LTI4IDI4aC04NGMtMTUuNDY0IDAtMjgtMTIuNTM2LTI4LTI4eiIgZmlsbD0iI2ZmZiIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=" alt="SLSA Generic generator logo">
</div>
    <div data-view-component="true" class="d-flex flex-column">
      <span data-view-component="true" class="f5 text-bold ml-2">SLSA Generic generator</span>
      <span data-view-component="true" class="color-fg-muted ml-2 text-small"></span>
</div>    <a href="https://github.com/s22223767-tech/spam-detector/new/main?filename=.github%2Fworkflows%2Fgenerator-generic-ossf-slsa3-publish.yml&amp;workflow_template=ci%2Fgenerator-generic-ossf-slsa3-publish" data-hydro-click="{&quot;event_type&quot;:&quot;actions.onboarding_setup_workflow_click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:1152624003,&quot;workflow_template&quot;:&quot;ci/generator-generic-ossf-slsa3-publish&quot;,&quot;view_section&quot;:&quot;repository_sidebar&quot;,&quot;view_rank&quot;:2,&quot;templates_count&quot;:3,&quot;template_creator&quot;:&quot;Open Source Security Foundation (OpenSSF)&quot;,&quot;new_with_filter_view&quot;:false,&quot;correlation_id&quot;:&quot;DB16:5F6C9:CF63A0:F103F7:698DB11B&quot;,&quot;category&quot;:&quot;Continuous integration&quot;,&quot;search_query&quot;:null,&quot;template_source_visibility&quot;:&quot;shared&quot;,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="46fc3ff4073f7340bf71a32d4f81a6b8f858fc1964ae21cd930e1bf0a7ca1f69" style="min-width: 80px" aria-describedby="slsa-generic-generator-description" data-view-component="true" class="Button--secondary Button--small Button ml-auto">  <span class="Button-content">
    <span class="Button-label">Configure<span class="sr-only">&nbsp;SLSA Generic generator</span></span>
  </span>
</a>
</div>  <span id="slsa-generic-generator-description" aria-hidden="true" data-view-component="true" class="d-flex color-fg-muted f6 ml-5 mt-1 pl-2">Generate SLSA3 provenance for your existing release workflows</span>
</div>
        </li>
        <li class="list-style-none">
          <div data-view-component="true" class="mb-2 p-3 border rounded-2">
  <div data-view-component="true" class="d-flex flex-items-stretch">
    <div aria-hidden="true" style="color: #3572A5 !important; background-color: var(--bgColor-white, var(--color-scale-white)) !important; width: 32px !important; height: 32px !important; min-width: 32px !important;" data-view-component="true" class="CircleBadge">
      <img class="CircleBadge-icon" src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBoZWlnaHQ9IjQ4IiB3aWR0aD0iNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMjMuNTkxYy4wMi0uMDY2LjAzNi0uMTM0LjA0NS0uMjAyLjAzNy0uNjk3LjA0NS0xLjQwMi4xMi0yLjEuMTE3LTIuMjYuODcxLTQuNDQgMi4xNzUtNi4yOWE2LjMyMiA2LjMyMiAwIDAxNS4wODUtMi41NjVIMjMuNjFjLjMxNSAwIC4zMTUgMCAuMzE1LS4zMTV2LTEuMTI1YzAtLjIzMi0uMDY4LS4yODQtLjI4NS0uMjg0SDEyLjYyM2MtLjE4OCAwLS4yNTUtLjA1My0uMjU1LS4yNDhWNC45NjZjLjAzNi0uNzk2LjM2OC0xLjU1LjkzLTIuMTE1YTYuNjgzIDYuNjgzIDAgMDEyLjcwNy0xLjc0NyAxNi42NjggMTYuNjY4IDAgMDEzLjktLjg5MiAzMi44NDMgMzIuODQzIDAgMDE1LjQ4Mi0uMTY1YzEuOTcyLjAzNyAzLjkyMy4zOTkgNS43NzYgMS4wNzJhNy4wOTUgNy4wOTUgMCAwMTMuMjQgMi4yNSA0LjUzNiA0LjUzNiAwIDAxLjk0NSAzLjA3NGMtLjA0NS45MyAwIDEuODY3IDAgMi44MDR2NS4xOWMwIDEuMDE5IDAgMi4wNDYtLjA0NSAzLjA1OGE1LjQyMSA1LjQyMSAwIDAxLTMuNTE4IDUuMDQgOC4wNDIgOC4wNDIgMCAwMS0zLjE0My41OTloLTExLjQ2YTYuNTQgNi41NCAwIDAwLTMuNDUuOTA3IDUuOTk5IDUuOTk5IDAgMDAtMi42NDcgMy43MDQgOC42NTYgOC42NTYgMCAwMC0uMzIzIDIuMzc3djUuMTk2YzAgLjM0NSAwIC4zMzgtLjM0NS4zNDUtMS4yNDUgMC0yLjQ5LjAzOC0zLjc1IDBBNS4yNSA1LjI1IDAgMDEzLjM0NSAzNC4zYTguMjQ4IDguMjQ4IDAgMDEtMi4yOTUtMy41NTQgMTUuMTQyIDE1LjE0MiAwIDAxLS44NDgtMy44NDdjLS4wNzUtLjg0LS4xMDUtMS42OC0uMTU3LTIuNTEyQTIuNDc1IDIuNDc1IDAgMDAwIDI0LjExdi0uNTE4eiIgZmlsbD0iIzM3NzJhNCIvPjxwYXRoIGQ9Ik0xNS4yMDMgNS43MzhhMi4xMDcgMi4xMDcgMCAxMDIuMTA3LTIuMTIyIDIuMTIzIDIuMTIzIDAgMDAtMi4xMDcgMi4xMjJ6IiBmaWxsPSIjMDAwIi8+PHBhdGggZD0iTTE1LjIwMyA1LjczOGEyLjExIDIuMTEgMCAxMTQuMjIgMCAyLjExIDIuMTEgMCAwMS00LjIyIDB6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTQ4IDI0LjQwMWMtLjAyLjA2Ni0uMDM2LjEzNC0uMDQ1LjIwMy0uMDM3LjY5Ny0uMDQ1IDEuNDAyLS4xMiAyLjFhMTEuOTk1IDExLjk5NSAwIDAxLTIuMTc1IDYuMjkgNi4zMjIgNi4zMjIgMCAwMS01LjA4NSAyLjU3MkgyNC4zOWMtLjMxNSAwLS4zMTUgMC0uMzE1LjMxNXYxLjEyNWMwIC4yMzIuMDY4LjI4NS4yODUuMjg1aDExLjAxOGMuMTg3IDAgLjI1NS4wNTIuMjU1LjI0N3Y1LjQ5NmEzLjIwOSAzLjIwOSAwIDAxLS45MyAyLjExNSA2LjY4MyA2LjY4MyAwIDAxLTIuNzA4IDEuNzQ3IDE2LjY2OSAxNi42NjkgMCAwMS0zLjg5Mi44OTJjLTEuODIuMjA4LTMuNjU0LjI2My01LjQ4My4xNjVhMTcuODc3IDE3Ljg3NyAwIDAxLTUuNzc1LTEuMDcyIDcuMDk1IDcuMDk1IDAgMDEtMy4yNC0yLjI1IDQuNTM2IDQuNTM2IDAgMDEtLjk0NS0zLjA3NGMuMDQ1LS45MyAwLTEuODY3IDAtMi44MDR2LTUuMTljMC0xLjAxOSAwLTIuMDQ2LjA0NS0zLjA1OGE1LjQyIDUuNDIgMCAwMTMuNTE3LTUuMDQgOC4wNDIgOC4wNDIgMCAwMTMuMTQzLS41OTloMTEuNDUzYTYuNTQgNi41NCAwIDAwMy40NS0uOTA3IDYgNiAwIDAwMi42NDctMy43MTIgOC42NiA4LjY2IDAgMDAuMzIzLTIuMzc3di01LjE5NmMwLS4zNDUgMC0uMzM3LjM0NS0uMzQ1IDEuMjQ1IDAgMi40OS0uMDM3IDMuNzUgMGE1LjI1IDUuMjUgMCAwMTMuMzIyIDEuMzY1IDguMjQ5IDguMjQ5IDAgMDEyLjI5NSAzLjU1NCAxNS4xNSAxNS4xNSAwIDAxLjg0IDMuODYxYy4wNzUuODQuMTA1IDEuNjguMTU4IDIuNTEyLjAxLjA5MS4wMjUuMTgxLjA0NS4yNy4wMDUuMTY1LjAwNy4zMzUuMDA3LjUxeiIgZmlsbD0iI2ZmZGE0YiIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTA3IDIuMTA3IDAgMTAtMi4xMDcgMi4xMjIgMi4xMjMgMi4xMjMgMCAwMDIuMTA3LTIuMTIyeiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTEgMi4xMSAwIDExLTQuMjIgMCAyLjExIDIuMTEgMCAwMTQuMjIgMHoiIGZpbGw9IiNmZmYiLz48L3N2Zz4=" alt="Python package logo">
</div>
    <div data-view-component="true" class="d-flex flex-column">
      <span data-view-component="true" class="f5 text-bold ml-2">Python package</span>
      <span data-view-component="true" class="color-fg-muted ml-2 text-small"></span>
</div>    <a href="https://github.com/s22223767-tech/spam-detector/new/main?filename=.github%2Fworkflows%2Fpython-package.yml&amp;workflow_template=ci%2Fpython-package" data-hydro-click="{&quot;event_type&quot;:&quot;actions.onboarding_setup_workflow_click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:1152624003,&quot;workflow_template&quot;:&quot;ci/python-package&quot;,&quot;view_section&quot;:&quot;repository_sidebar&quot;,&quot;view_rank&quot;:3,&quot;templates_count&quot;:3,&quot;template_creator&quot;:null,&quot;new_with_filter_view&quot;:false,&quot;correlation_id&quot;:&quot;DB16:5F6C9:CF63A0:F103F7:698DB11B&quot;,&quot;category&quot;:&quot;Continuous integration&quot;,&quot;search_query&quot;:null,&quot;template_source_visibility&quot;:&quot;shared&quot;,&quot;originating_url&quot;:&quot;https://github.com/s22223767-tech/spam-detector&quot;,&quot;user_id&quot;:247223143}}" data-hydro-click-hmac="e5cc718aaece2e65c802b8ffad3f2304f1788510f6b53287fc44354b6b83840b" style="min-width: 80px" aria-describedby="python-package-description" data-view-component="true" class="Button--secondary Button--small Button ml-auto">  <span class="Button-content">
    <span class="Button-label">Configure<span class="sr-only">&nbsp;Python package</span></span>
  </span>
</a>
</div>  <span id="python-package-description" aria-hidden="true" data-view-component="true" class="d-flex color-fg-muted f6 ml-5 mt-1 pl-2">Create and test a Python package on multiple Python versions.</span>
</div>
        </li>
    </ol>
    <div data-view-component="true" class="d-flex flex-justify-between">
      <a data-analytics-event="{&quot;category&quot;:&quot;suggested_workflows_in_repository_sidebar&quot;,&quot;action&quot;:&quot;clicked_on_see_more_button&quot;,&quot;label&quot;:&quot;owner:247223143;ref_cta:configure;ref_loc:respository_sidebar&quot;}" href="https://github.com/s22223767-tech/spam-detector/actions/new" data-view-component="true" class="Link">More workflows</a>
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-notice-dismiss" data-turbo="false" action="https://github.com/users/s22223767-tech/dismiss_repository_notice" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="delete" autocomplete="off"><input type="hidden" name="authenticity_token" value="TWhwr1AKynTXq8lWqN-jOaFhIWXBIP_QwJlqEVyc55Cb_D4hYtIFw0zAYNb30bNWtm15NJulNw0DBqOLbYWXJw" autocomplete="off">
        <input type="hidden" name="notice_name" value="repo_suggested_workflows">
        <input type="hidden" name="repository_id" value="1152624003">
        <button data-analytics-event="{&quot;category&quot;:&quot;suggested_workflows_in_repository_sidebar&quot;,&quot;action&quot;:&quot;dismissed_component&quot;,&quot;label&quot;:&quot;owner:247223143;ref_cta:configure;ref_loc:respository_sidebar&quot;}" type="submit" data-view-component="true" class="Button--link Button--medium Button text-small color-fg-muted text-normal" fdprocessedid="jtatjd">  <span class="Button-content">
    <span class="Button-label">Dismiss suggestions</span>
  </span>
</button>

</form></div>  </div>
</div>

</div>

</div>
  
</div></div>

  </div>


  </div></turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-7 pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</a>
      <span>
        © 2026 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}" fdprocessedid="8kv55l">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}" fdprocessedid="mteu4p">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/s22223767-tech"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/s22223767-tech"]:before,
      .user-mention[href$="/s22223767-tech"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true"></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div><live-region><template shadowrootmode="open">
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style>
<div id="polite" aria-live="polite" aria-atomic="true"></div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region><span id="PING_CONTENT_ANNOTATION" style="display: none;"></span><span id="PING_IFRAME_FORM_DETECTION" style="display: none;"></span></body></html>