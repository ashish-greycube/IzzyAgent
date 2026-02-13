// Copyright (c) 2026, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Izzy Subscription Plan", {
    setup(frm){
        frappe.db.get_single_value("Izzy Settings", "company").then(company => {
             frm.set_query("project", () => {            
                return {
                    filters: {
                        company: company
                    }
                }
            })
        })
    },
    refresh(frm) {
        if (frm.is_new()) {
            frm.set_df_property("setup_fee", "hidden", 1);
        }
        else{
            frm.set_df_property("setup_fee", "hidden", 0);
        }
    },
    setup_fee(frm) {
        // console.log("=====inside setup_fee=====")
        if (frm.is_new()) {
            frappe.throw("Please save the Subscription Plan before creating Setup Fee Sales Invoice.");
        }
        else {
            frappe.model.open_mapped_doc({
                method: "izzyagent.izzyagent.doctype.izzy_subscription_plan.izzy_subscription_plan.create_setup_fee_sales_invoice",
                frm: frm,
            });
        }
    }
});
