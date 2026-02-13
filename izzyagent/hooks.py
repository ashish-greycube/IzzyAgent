app_name = "izzyagent"
app_title = "Izzyagent"
app_publisher = "GreyCube Technologies"
app_description = "Customization for IzzyAgent"
app_email = "admin@greycube.in"
app_license = "mit"

# Apps
# ------------------

after_migrate = "izzyagent.migrate.after_migration"

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "izzyagent",
# 		"logo": "/assets/izzyagent/logo.png",
# 		"title": "Izzyagent",
# 		"route": "/izzyagent",
# 		"has_permission": "izzyagent.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/izzyagent/css/izzyagent.css"
# app_include_js = "/assets/izzyagent/js/izzyagent.js"

# include js, css files in header of web template
# web_include_css = "/assets/izzyagent/css/izzyagent.css"
# web_include_js = "/assets/izzyagent/js/izzyagent.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "izzyagent/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "izzyagent/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "izzyagent.utils.jinja_methods",
# 	"filters": "izzyagent.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "izzyagent.install.before_install"
# after_install = "izzyagent.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "izzyagent.uninstall.before_uninstall"
# after_uninstall = "izzyagent.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "izzyagent.utils.before_app_install"
# after_app_install = "izzyagent.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "izzyagent.utils.before_app_uninstall"
# after_app_uninstall = "izzyagent.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "izzyagent.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Sales Invoice": {
        "validate": "izzyagent.api.add_si_reference_to_subscription_plan"
    }
}


# Scheduled Tasks
# ---------------

# 1st day of every month at 12:30 AM
# 30 00 1 * *

scheduler_events = {
    "cron": {
        "45 23 30 4,6,9,11 *": [ "izzyagent.api.create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached_for_thirtyth_day" ], #30th April, June, Sept, Nov At 23:45 PM
        "45 23 31 1,3,5,7,8,10,12 *": [ "izzyagent.api.create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached_for_thirty_first_day" ],  #31st Jan, Mar, May, July, Aug, Oct, Dec At 23:45 PM
        "45 23 28,29 2 *": [ "izzyagent.api.create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached_for_february_last_day" ],  #28th/29th Feb At 23:45 PM
        # "*/5 * * * *": [ "izzyagent.api.create_subscription_plan_invoice" ] # for testing purpose, every 5 mins
    }
}

# scheduler_events = {
# 	"all": [
# 		"izzyagent.tasks.all"
# 	],
# 	"daily": [
# 		"izzyagent.tasks.daily"
# 	],
# 	"hourly": [
# 		"izzyagent.tasks.hourly"
# 	],
# 	"weekly": [
# 		"izzyagent.tasks.weekly"
# 	],
# 	"monthly": [
# 		"izzyagent.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "izzyagent.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "izzyagent.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "izzyagent.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["izzyagent.utils.before_request"]
# after_request = ["izzyagent.utils.after_request"]

# Job Events
# ----------
# before_job = ["izzyagent.utils.before_job"]
# after_job = ["izzyagent.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"izzyagent.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

