from . import __version__ as app_version

app_name = "gh_customize"
app_title = "Gh Customize"
app_publisher = "Carbonite Solutions Limited"
app_description = "Customized reports and configurations"
app_email = "admin@carbonitesolutions.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gh_customize/css/gh_customize.css"
# app_include_js = "/assets/gh_customize/js/gh_customize.js"

# include js, css files in header of web template
# web_include_css = "/assets/gh_customize/css/gh_customize.css"
# web_include_js = "/assets/gh_customize/js/gh_customize.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gh_customize/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "gh_customize.utils.jinja_methods",
#	"filters": "gh_customize.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gh_customize.install.before_install"
# after_install = "gh_customize.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gh_customize.uninstall.before_uninstall"
# after_uninstall = "gh_customize.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gh_customize.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gh_customize.tasks.all"
#	],
#	"daily": [
#		"gh_customize.tasks.daily"
#	],
#	"hourly": [
#		"gh_customize.tasks.hourly"
#	],
#	"weekly": [
#		"gh_customize.tasks.weekly"
#	],
#	"monthly": [
#		"gh_customize.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "gh_customize.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gh_customize.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gh_customize.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gh_customize.utils.before_request"]
# after_request = ["gh_customize.utils.after_request"]

# Job Events
# ----------
# before_job = ["gh_customize.utils.before_job"]
# after_job = ["gh_customize.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gh_customize.auth.validate"
# ]
