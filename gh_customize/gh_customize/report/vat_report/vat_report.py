from __future__ import unicode_literals
from frappe import _
import frappe


def execute(filters=None):
    return get_columns(), add_totals(get_data(filters))


def get_data(filters):
    sales_conditions = "WHERE `tabSales Invoice`.`docstatus` = %(submitted)s AND `tabSales Invoice`.`company` = %(company)s"
    purchase_conditions = "WHERE `tabPurchase Invoice`.`status` = %(submitted)s AND `tabPurchase Invoice`.`taxes_and_charges` < 2 AND `tabPurchase Invoice`.`company` = %(company)s"
    if filters.get("from_date"):
        sales_conditions += " AND `tabSales Invoice`.`posting_date` >= %(from_date)s AND `tabSales Taxes and Charges`.`rate` IN (3, 12.5, 15)"
        purchase_conditions += " AND `tabPurchase Invoice`.`posting_date` >= %(from_date)s AND `tabPurchase Taxes and Charges`.`rate` IN (3, 12.5, 15)"
    if filters.get("to_date"):
        sales_conditions += " AND `tabSales Invoice`.`posting_date` <= %(to_date)s AND `tabSales Taxes and Charges`.`rate` IN (3, 12.5, 15)"
        purchase_conditions += " AND `tabPurchase Invoice`.`posting_date` <= %(to_date)s AND `tabPurchase Taxes and Charges`.`rate` IN (3, 12.5, 15)"
    if filters.get("rates"):
        sales_conditions += " AND `tabSales Taxes and Charges`.`rate` = %(rates)s"
        purchase_conditions += " AND `tabPurchase Taxes and Charges`.`rate` = %(rates)s"
    else:
        # If neither from_date nor rates filters are selected, return an empty list
        if not filters.get("from_date"):
            return []

    sales_data = frappe.db.sql("""SELECT 
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
                          """.format(sales_conditions), filters)

    purchase_data = frappe.db.sql("""SELECT 
                              `tabPurchase Invoice`.`posting_date`,
                              `tabPurchase Invoice`.`name`,
                              `tabPurchase Invoice`.`bill_no`,
                              `tabPurchase Invoice`.`base_total`,
                              `tabPurchase Taxes and Charges`.`rate`,
                              `tabPurchase Invoice`.`base_total_taxes_and_charges`,
                              `tabPurchase Invoice`.`grand_total`
                            FROM 
                              `tabPurchase Invoice` JOIN `tabPurchase Taxes and Charges` 
                              ON (`tabPurchase Taxes and Charges`.`parent` = `tabPurchase Invoice`.`name`)
                            {0}
                          """.format(purchase_conditions), filters)

    return sales_data + purchase_data


def get_columns():
    return [
        "Date:Data:150",
        "Transaction ID:Data:200",
        "Supplier / Customer ID:Data:150",
        "Base Value:Currency:150",
        "Rate:Data:80",
        "Vat:Currency:150",
        "Grand Total:Currency:150",
    ]


def add_totals(data):
    if not data:
        return []

    sales_total = 0
    sales_vat_total = 0
    purchase_total = 0
    purchase_vat_total = 0

    for row in data:
        if row[1].startswith("ACC-SINV-"):
            sales_total += row[3]
            sales_vat_total += row[5]
        elif row[1].startswith("ACC-PINV-"):
            purchase_total += row[3]
            purchase_vat_total += row[5]

    grand_total = sales_total - purchase_total
    grand_vat_total = sales_vat_total - purchase_vat_total

    sales_row = ["", "", "<b>Sales Total</b>", sales_total, "", sales_vat_total, ""]
    purchase_row = ["", "", "<b>Purchase Total</b>", purchase_total, "", purchase_vat_total, ""]
    sales_row[-1] = sales_total + sales_vat_total
    purchase_row[-1] = purchase_total + purchase_vat_total
    total_row = ["", "", "<b>VAT To Be Paid</b>", grand_total, "", grand_vat_total, grand_total + grand_vat_total]
    return tuple(data) + (sales_row, purchase_row, total_row)

