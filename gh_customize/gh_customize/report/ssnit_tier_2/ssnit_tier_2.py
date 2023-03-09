from __future__ import unicode_literals
from frappe import _
import frappe
from datetime import datetime


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

    slip_data = frappe.db.sql("""SELECT 
                              `tabEmployee`.`ssnit_id`,
                              `tabEmployee`.`ghana_card`,
                              `tabEmployee`.`last_name`,
                              `tabEmployee`.`first_name`,
                              `tabEmployee`.`middle_name`,
                              "",
                              "",
                              MAX(CASE WHEN `tabSalary Detail`.`salary_component` = 'Basic' THEN `tabSalary Detail`.`amount` END),
                              MAX(CASE WHEN `tabSalary Detail`.`salary_component` = 'Basic' THEN
								CASE
								WHEN `tabSalary Detail`.`amount` <= 402.76 THEN 402.76 * 0.5
								WHEN `tabSalary Detail`.`amount` > 402.76 AND `tabSalary Detail`.`amount` <= 42000 THEN `tabSalary Detail`.`amount` * 0.05
								ELSE 42000 * 0.5
								END
								END)
                            FROM 
                              `tabSalary Slip`
                            INNER JOIN `tabEmployee` ON `tabSalary Slip`.`employee` = `tabEmployee`.`employee`
                            INNER JOIN `tabSalary Detail` ON `tabSalary Slip`.`name` = `tabSalary Detail`.`parent`
                            {0}
                          """.format(slip_conditions), filters)
    
    #the below sql code will run when the date in the filter is greater 2023, 12, 31. new ssnit minimum wage for 2024 needs to be inserted in the query. so the current 402.76 will be change to the new minimum wage.

    slip2_data = frappe.db.sql("""SELECT 
                              `tabEmployee`.`ssnit_id`,
                              `tabEmployee`.`ghana_card`,
                              `tabEmployee`.`last_name`,
                              `tabEmployee`.`first_name`,
                              `tabEmployee`.`middle_name`,
                              "",
                              "",
                              MAX(CASE WHEN `tabSalary Detail`.`salary_component` = 'Basic' THEN `tabSalary Detail`.`amount` END),
                              MAX(CASE WHEN `tabSalary Detail`.`salary_component` = 'Basic' THEN
								CASE
								WHEN `tabSalary Detail`.`amount` <= 402.76 THEN 402.76 * 0.5
								WHEN `tabSalary Detail`.`amount` > 402.76 AND `tabSalary Detail`.`amount` <= 42000 THEN `tabSalary Detail`.`amount` * 0.05
								ELSE 42000 * 0.5
								END
								END)
                            FROM 
                              `tabSalary Slip`
                            INNER JOIN `tabEmployee` ON `tabSalary Slip`.`employee` = `tabEmployee`.`employee`
                            INNER JOIN `tabSalary Detail` ON `tabSalary Slip`.`name` = `tabSalary Detail`.`parent`
                            {0}
                          """.format(slip_conditions), filters)
    
    

    year = filters.get("from_date")
    if year is not None:
        year_date = datetime.strptime(year, '%Y-%m-%d')  # Convert the year string to a datetime object
        if year_date > datetime(2022, 12, 31):
            return slip_data
        elif year_date > datetime(2023, 12, 31):
            return slip2_data
    else:
    # handle case where year is None
        return []



def get_columns():
    return [
        "SSNIT NUMBER:Data:150",
        "NIA NUMBER:Data:200",
        "SURNAME:Data:150",
        "FIRST NAME:Data:150",
        "OTHER NAME:Data:80",
        "OPTION CODE (PNDCL 247/ACT 766):Data:150",
        "HAZARDOUS (Y/N):Data:150",
        "BASIC SALARY:currency",
        "TIER TWO CONTRIBUTIONS:currency",
    ]
