// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SSNIT Tier 2"] = {
	"filters": [
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": ["Submitted", "Draft"],
			"default":"Submitted",
			"width": "100px",
		},
		{
			"fieldname":"from_date",
			"label": __("Date"),
			"fieldtype": "Date",
			"width": "100px",
		},
		

	]
};
