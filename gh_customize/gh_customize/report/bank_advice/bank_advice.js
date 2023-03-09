// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bank Advice"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("Date"),
			"fieldtype": "Date",
			"width": "100px",
		},
		{
			"fieldname":"docstatus",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": [" ", "Submitted", "Draft"],
			"width": "100px",
		}


	]
};
