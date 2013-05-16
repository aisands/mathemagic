--Author: Adrienne Sands (2013)
--Purpose: Trigger practice

--1- updates trigger invoices_before_update to raise an error whenever payment total + credit total > invoice total
drop trigger if exists invoices_before_update;

delimiter //

create trigger invoices_before_update
	before update on invoices  
	for each row 
begin  
	declare sum_line_item_amount decimal(9,2);   

	select sum(line_item_amount)  
	into sum_line_item_amount  
	from invoice_line_items  
	where invoice_id = new.invoice_id;   

	if sum_line_item_amount != new.invoice_total then   
		signal sqlstate 'HY000'    
			set message_text = 'Line item total must match invoice total.';  

	elseif new.payment_total + new.credit_total > old.invoice_total then
		signal sqlstate 'HY000'
			set message_text = 'Payment and credit total cannot exceed invoice total.';
	end if;

end //

delimiter ;

UPDATE invoices
SET payment_total = 10976.06, credit_total = 10976.06
WHERE invoice_id = 112;

SELECT invoice_id, invoice_total, credit_total, payment_total
FROM invoices
WHERE invoice_id = 112;

#2 - trigger: invoices_after_update
#creates invoices_audit table
#inserts old data into the invoices_audit table

-- creates invoices_audit table
use ap;

create table invoices_audit
(
	vendor_id		int				not null,
	invoice_number	varchar(50)		not null,
	invoice_total	decimal(9,2)	not null,
	action_type		varchar(50)		not null,
	action_date		datetime		not null
);

drop trigger if exists invoices_after_update;

delimiter //

create trigger invoices_after_update
	after update on invoices
	for each row
begin
	insert into invoices_audit values
	(old.vendor_id, old.invoice_number, old.invoice_total, 'updated', now());
end //

delimiter ;

update invoices
set payment_total = 50
where invoice_id = 7;

select * from invoices_audit

#3
USE ap;

SET GLOBAL event_scheduler = ON;

DROP EVENT IF EXISTS minute_test;

DELIMITER //

CREATE EVENT minute_test
ON SCHEDULE EVERY 1 MINUTE
DO BEGIN
    INSERT INTO invoices_audit VALUES
    (9999, 'test', 999.99, 'INSERTED', NOW());
END//

DELIMITER ;

SHOW EVENTS LIKE '%min';

SELECT * FROM invoices_audit;

DROP EVENT minute_test;

