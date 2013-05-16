/*
Author: Adrienne Sands (2013)
Purpose: basic statements
*/

/*1 - select statement that returns one row for each vendor in the invoices table that contains these columns
#the vendor_id column from the vendors table
#the sum of the invoice_total columns in the invoices table for that vendor */

select distinct v.vendor_id, i.invoice_total
from vendors v, invoices i
where v.vendor_id = i.vendor_id
group by i.vendor_id;

/*2 - select statement that returns one row for each vendor that contains these columns
# the vendor_name column from the vendors table
# the sum of the payment_total columns in the invoices table for that vendor
#sort the result set in descending sequence by the payment total sum for each vendor */

select v.vendor_name, sum(i.payment_total)
from vendors v, invoices i
where v.vendor_id = i.vendor_id
group by v.vendor_id
order by sum(i.payment_total) desc;

/*3 - select statement that returns one row for each vendor that contains three columns:
# vendor_name column from the vendors table
# count of the invoices in the invoices table for each vendor
# sum of the invoice_total columns in the invoices table for each vendor
#sort the result set so teh vendor with the most invoices appears first */

select vendor_name as "vendor name", count(i.vendor_id) as "num of invoices",
	sum(invoice_total) as "invoice total"
from vendors v, invoices i
where v.vendor_id = i.vendor_id
group by vendor_name
order by count(i.vendor_id) desc;

/*4 - select statement that returns one row for each general ledger account number and contains
# account_description from the gen ledger table
# count of items in the line items table that have the same account_number
# sum of the line_item_amount columns in the invoice line items table w/ same account number
#return rows with more than 1 line item
#group by account description
#sort by sum of line item amounts in desc sequence */

select gl.account_description as "account description", count(li.account_number) as "num of line items", 
	sum(li.line_item_amount) as "total line items"
from general_ledger_accounts gl, invoice_line_items li
where gl.account_number = li.account_number
group by gl.account_description
having count(li.account_number) > 1
order by sum(li.line_item_amount) desc;

-- modified solution to 4 that returns only invoices dated in the 2nd quarter of 2011
select gl.account_description as "account description", count(li.account_number) as "num of line items", 
	sum(li.line_item_amount) as "total line items", i.invoice_date as "invoice date"
from general_ledger_accounts gl, invoice_line_items li, invoices i
where gl.account_number = li.account_number
	and i.invoice_id = li.invoice_id
group by gl.account_description
having count(li.account_number) > 1
	and i.invoice_date >= '2011-04-01'
	and i.invoice_date <= '2011-06-30'
order by sum(li.line_item_amount) desc;

/*6 - question: what is the total amount invoiced for each general ledger account number? return these columns:
# account number from the invoice_line_items table
# sum of the line item amounts */

select li.account_number as "account number", sum(li.line_item_amount) as "line item total"
from invoice_line_items li
group by li.account_number
with rollup;

/*7 - question: which vendors are being paid from more than one account.
# returns: vendor name, count of distinct general ledger accounts */

select distinct v.vendor_name as "vendor name", count( distinct gl.account_number) as "num of distinct general ledger accounts"
from general_ledger_accounts gl
	join invoice_line_items li
		on gl.account_number = li.account_number
	join invoices i
		on li.invoice_id = i.invoice_id
	join vendors v						
		on i.vendor_id = v.vendor_id
group by v.vendor_id
	having count(distinct gl.account_number) > 1;


