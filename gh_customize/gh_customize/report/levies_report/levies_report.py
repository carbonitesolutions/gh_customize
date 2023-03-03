# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe 


def execute(filters=None):
    return get_columns(), get_data(filters)


def get_data(filters):
    conditions = "WHERE `tabSales Invoice`.`status` = %(submitted)s AND `tabSales Invoice`.`taxes_and_charges` < 2 AND `tabSales Invoice`.`company` = %(company)s"
    if filters.get("from_date"):
        conditions += " AND `tabSales Invoice`.`posting_date` >= %(from_date)s AND `tabSales Taxes and Charges`.`rate` IN (1, 2, 2.5)"
    if filters.get("to_date"):
        conditions += " AND `tabSales Invoice`.`posting_date` <= %(to_date)s"
    if filters.get("rates"):
        conditions += " AND `tabSales Taxes and Charges`.`rate` = %(rates)s"
    else:
        # If neither from_date nor rates filters are selected, return an empty list
        if not filters.get("from_date"):
            return []
    
    data = frappe.db.sql("""SELECT 
                              `tabSales Invoice`.`posting_date`,
                              `tabSales Invoice`.`name`,
                              `tabSales Invoice`.`customer`,
                              `tabSales Invoice`.`base_total`,
                              `tabSales Taxes and Charges`.`rate`,
                              `tabSales Invoice`.`base_total_taxes_and_charges`,
							  `tabSales Invoice`.`grand_total`
                            FROM 
                              `tabSales Invoice` JOIN `tabSales Taxes and Charges` 
                              ON (`tabSales Taxes and Charges`.`parent` = `tabSales Invoice`.`name`)
                            {0}
                          """.format(conditions), filters)
    return data


def get_columns():
    return [
        "Date:Data:150",
        "Transaction ID:Data:200",
        "Supplier ID:Data:150",
        "Base Value:150",
        "Rate:Data:80",
        "Vat:Currency:150",
		"Grand Total:Currency:150",

    ]
