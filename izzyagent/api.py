import frappe
from frappe import _
from frappe.utils import getdate, nowdate, get_last_day, add_to_date

@frappe.whitelist()
def create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached():
	today = getdate(nowdate())
	cur_month_last_date = get_last_day(today)
	# print(cur_month_last_date, "========cur_month_last_date=========")
	# if today == cur_month_last_date:
	if today == today:            ### For testing purpose, to run the function every day. change it to above condition for production use.
		plan_list = frappe.get_all("Izzy Subscription Plan", filters={"status": "Active"}, pluck="name")
		izzy_settings = frappe.get_doc("Izzy Settings")
		if len(plan_list) > 0:
			for plan in plan_list:
				create_sales_invoice = False
				plan_doc = frappe.get_doc("Izzy Subscription Plan", plan)
				item_rate = plan_doc.rate

				item_description = "IzzyAgents Monthly Fee - {0}".format(today.strftime("%B %Y"))

				if getdate(plan_doc.start_date).month == today.month and getdate(plan_doc.start_date).year == today.year:
					create_sales_invoice = True
					#Prorated for first month   
					per_day_rate = plan_doc.rate / getdate(cur_month_last_date).day
					total_plan_days = (getdate(cur_month_last_date).day - getdate(plan_doc.start_date).day) + 1
					item_rate = per_day_rate * total_plan_days
					if getdate(plan_doc.start_date).day != 1:
						item_description = "IzzyAgents Fee - Prorated ({0}-{1}, Plan Start: {2})".format(getdate(plan_doc.start_date).day, getdate(cur_month_last_date).day, plan_doc.start_date)

				elif plan_doc.end_date and getdate(plan_doc.end_date).month == today.month and getdate(plan_doc.end_date).year == today.year:
					create_sales_invoice = True
					#Prorated for last month
					per_day_rate = plan_doc.rate / getdate(cur_month_last_date).day
					total_plan_days = getdate(plan_doc.end_date).day
					item_rate = per_day_rate * total_plan_days

					if getdate(plan_doc.end_date).day != getdate(cur_month_last_date).day:
						item_description = "IzzyAgents Fee - Prorated ( {0} days, Plan End: {1})".format(total_plan_days, plan_doc.end_date)

					plan_doc.status = "Inactive"
					plan_doc.add_comment("Comment", _("Subscription Plan marked as Inactive as end date {0} is reached").format(plan_doc.end_date))

				elif (getdate(plan_doc.start_date) <= today) and (not plan_doc.end_date or getdate(plan_doc.end_date) >= today):
					create_sales_invoice = True

				if create_sales_invoice:
					si = frappe.new_doc("Sales Invoice")
					si.customer = plan_doc.customer
					si.custom_izzy_si_type = "Subscription"
					si.custom_izzy_plan_ref = plan_doc.name
					# si.due_date = getdate(nowdate())
					si.project = plan_doc.project
					si.company = izzy_settings.company

					if izzy_settings.payment_due_date > 0:
						due_days = izzy_settings.payment_due_date
					else:
						due_days = 1

					si.due_date = add_to_date(getdate(today), days=due_days)

					if plan_doc.billing_currency == "NZD":
						item_tax_template = izzy_settings.item_tax_template_for_nz
					else:
						item_tax_template = izzy_settings.item_tax_template_for_non_nz
					
					item_name, uom = frappe.db.get_value("Item", plan_doc.item, ["item_name", "stock_uom"])
					si.append("items", {
						"item_code": plan_doc.item,
						"qty": 1,
						"rate": item_rate,
						"item_tax_template": item_tax_template,
						"item_name": item_name, 
						"uom": uom,
						"description": item_description
					})
					
					si.run_method("set_missing_values")
					si.run_method("calculate_taxes_and_totals")
					si.save(ignore_permissions=True)
					si.submit()

					plan_doc.append("subscription_invoices", {
						"sales_invoice": si.name,
						"si_date": si.posting_date
					})
					plan_doc.save(ignore_permissions=True)

					print("Created Subscription Sales Invoice: {}".format(si.name))

@frappe.whitelist()
def create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached_for_thirtyth_day():
	create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached()

@frappe.whitelist()
def create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached_for_thirty_first_day():
	create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached()

@frappe.whitelist()
def create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached_for_february_last_day():
	create_subscription_plan_invoice_and_set_plan_inactive_if_end_date_reached()



def add_si_reference_to_subscription_plan(doc, method):
	if doc.is_new() and doc.custom_izzy_si_type == "Setup" and doc.custom_izzy_plan_ref:
		frappe.db.set_value("Izzy Subscription Plan", doc.custom_izzy_plan_ref, "si_reference_for_setup_fee", doc.name)
