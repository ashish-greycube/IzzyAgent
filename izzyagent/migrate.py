from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_migration():
    custom_fields = {
        "Sales Invoice" : [
            {
				"fieldname":"custom_izzy_si_type",
				"label":"Izzy SI Type",
				"fieldtype":"Select",
                "options": "\nSetup\nSubscription",
				"insert_after": "amended_from",
				"is_custom_field":1,
				"is_system_generated":0,
                "read_only":1,
            },
            {
				"fieldname":"custom_izzy_plan_ref",
				"label":"Izzy Plan",
				"fieldtype":"Link",
                "options": "Izzy Subscription Plan",
				"insert_after": "custom_izzy_si_type",
                "read_only":1,
				"is_custom_field":1,
				"is_system_generated":0
            },
        ],
    }

    print("Izzy: Adding Custom Fields In Following Doctypes.....")
    for dt, fields in custom_fields.items():
        print("**********\n %s: " % dt, [d.get("fieldname") for d in fields])
    create_custom_fields(custom_fields)