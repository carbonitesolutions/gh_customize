# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe 


def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
    conditions = ""
    if filters.get("docstatus") and filters.get("from_date"):
        conditions += " AND `tabSalary Slip`.`status` = %(docstatus)s"
        conditions += " AND `tabSalary Slip`.`start_date` = %(from_date)s"
        data = frappe.db.sql("""SELECT `tabEmployee`.`bank_name`, `tabEmployee`.`employee_name`,
          `tabEmployee`.`sort_code`, `tabEmployee`.`bank_ac_no`, `tabSalary Slip`.`net_pay` 
          FROM `tabSalary Slip`, `tabEmployee` 
          WHERE `tabEmployee`.`employee` = `tabSalary Slip`.`employee` {0}""".format(conditions), filters)
    else:
        data = []
    return data



def get_columns():
	return[
		"Bank:Data:80",
		"Account Name:Data:150",
		"Sort Code:Data:100",
		"Account No:Data:150",
		"Amount:Currency:80",
	]


