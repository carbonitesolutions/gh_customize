from __future__ import unicode_literals
from frappe import _
import frappe


def execute(filters=None):
    return get_columns(), get_data(filters)


def get_data(filters):
    slip_conditions = "WHERE `tabSalary Slip`.`docstatus` = '1' AND `tabSalary Slip`.`status` = %(status)s AND `tabSalary Slip`.`name` IN (SELECT DISTINCT `parent` FROM `tabSalary Detail` WHERE `salary_component` = 'Employee SSNIT' AND `amount` > 0)"
    if filters.get("from_date"):
        slip_conditions += " AND `tabSalary Slip`.`start_date` = %(from_date)s"
    else:
        # If neither from_date nor rates filters are selected, return an empty list
        if not filters.get("from_date"):
            return []

    sales_data = frappe.db.sql("""SELECT 
                              `tabEmployee`.`ssnit_id`,
                              `tabEmployee`.`ghana_card`,
                              `tabEmployee`.`last_name`,
                              `tabEmployee`.`first_name`,
                              `tabEmployee`.`middle_name`,
                              "",
                              "",
                              MAX(CASE WHEN `tabSalary Detail`.`salary_component` = 'Basic' THEN `tabSalary Detail`.`amount` END)
                            FROM 
                              `tabSalary Slip`
                            INNER JOIN `tabEmployee` ON `tabSalary Slip`.`employee` = `tabEmployee`.`employee`
                            INNER JOIN `tabSalary Detail` ON `tabSalary Slip`.`name` = `tabSalary Detail`.`parent`
                            {0}
                          """.format(slip_conditions), filters)
    

    return sales_data


def get_columns():
    return [
        "SSNIT NUMBER:Data:150",
        "NIA NUMBER:Data:200",
        "SURNAME:Data:150",
        "FIRST NAME:Data:150",
        "OTHER NAME:Data:80",
        "OPTION CODE (PNDCL 247/ACT 766):Data:150",
        "HAZARDOUS (Y/N):Data:150",
        "Basic Salary:currency",
    ]
