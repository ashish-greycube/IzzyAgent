# Copyright (c) 2026, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import getdate, nowdate, add_to_date

class IzzySubscriptionPlan(Document):
	pass


@frappe.whitelist()
def create_setup_fee_sales_invoice(source_name, target_doc=None):
	plan = frappe.get_doc("Izzy Subscription Plan", source_name)

	# print("======"*100)
	def set_missing_values(source, target):
		izzy_settings = frappe.get_doc("Izzy Settings")

		target.customer = source.customer
		target.custom_izzy_si_type = "Setup"
		target.custom_izzy_plan_ref = source.name
		target.project = source.project
		target.company = izzy_settings.company
		target.due_date = add_to_date(getdate(nowdate()), days=izzy_settings.payment_due_date)
		
		setup_item = izzy_settings.setup_fee_item
		if not setup_item:
			frappe.throw("Please set 'Setup Fee Item' in Izzy Settings")

		item_name, uom = frappe.db.get_value("Item", setup_item, ["item_name", "stock_uom"])

		income_account, cost_center = frappe.db.get_value("Item Default", {"parent": setup_item, "company": izzy_settings.company, "parentfield": "item_defaults"}, ["income_account", "selling_cost_center"])
		if not income_account:
			income_account = frappe.db.get_value("Company", izzy_settings.company, "default_income_account")
		if not cost_center:
			cost_center = frappe.db.get_value("Company", izzy_settings.company, "cost_center")

		target.append("items", {"item_code": setup_item,
									"qty": 1, 
									"item_name": item_name, 
									"uom": uom, 
									"income_account": income_account or '',
									"cost_center": cost_center or '',
									"description": "Setup Fee for Subscription Plan: {}".format(source.name)})

	si = get_mapped_doc(
		plan.doctype,
		plan.name,
		{
			plan.doctype: {
				"doctype": "Sales Invoice",
				"field_map": {
					"customer": "customer",
				},
			}
		},
		target_doc,
		set_missing_values,
	)
	return si