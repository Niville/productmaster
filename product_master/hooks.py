# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "product_master"
app_title = "Product Master"
app_publisher = "Ragav"
app_description = "App for displaying the product details like delivery conditions , chemical composition , dimensions and mechanical properties"
app_icon = "octicon octicon-beaker"
app_color = "#202020"
app_email = "srinivasragav@hotmail.com"
app_version = "0.0.1"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/product_master/css/product_master.css"
# app_include_js = "/assets/product_master/js/product_master.js"

# include js, css files in header of web template
# web_include_css = "/assets/product_master/css/product_master.css"
# web_include_js = "/assets/product_master/js/product_master.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "product_master.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "product_master.install.before_install"
# after_install = "product_master.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "product_master.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"product_master.tasks.all"
# 	],
# 	"daily": [
# 		"product_master.tasks.daily"
# 	],
# 	"hourly": [
# 		"product_master.tasks.hourly"
# 	],
# 	"weekly": [
# 		"product_master.tasks.weekly"
# 	]
# 	"monthly": [
# 		"product_master.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "product_master.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "product_master.event.get_events"
# }

