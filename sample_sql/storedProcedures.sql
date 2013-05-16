/* 1 - creates and calls a stored procedure named test
#declares a variable, sets to count of all rows in invoices table w/ balance >= 5000
#displays result w/ a message like "3 invoices exceed $5000" */

use ap;

drop procedure if exists test;  

delimiter //

create procedure test()
begin
	declare invoice_count_var int;

	select count(invoice_id) 
	into invoice_count_var
	from invoices
	where payment_total >= 5000;

	if invoice_count_var > 0 then
		select concat(invoice_count_var,' invoice(s) exceed $5000') as message;
	else
		select 'No invoices exceed $5000' as message;
	end if;
end//

delimiter ;

call test();

/*2 - creates and calls stored procedure test
#uses 2 vars to store count of all invoices with balance due, sum of balances due for these invoices
#if balance due >= 30000, displays both variables, else displays "total balance due less than $30,000"
drop procedure if exists test;*/

delimiter //

create procedure test()
begin
	declare num_due_invoices_var int;
	declare sum_due_invoices_var decimal(9,2);

	select count(invoice_id), sum(invoice_total - payment_total - credit_total)
	into num_due_invoices_var, sum_due_invoices_var
	from invoices
	where invoice_total - payment_total - credit_total > 0;

	if sum_due_invoices_var >= 30000 then
		select num_due_invoices_var as "number of overdue invoices",
			concat("$",sum_due_invoices_var) as "total overdue";
	else
		select "Total balance due is less than $30,000" as message;
	end if;		
end //

delimiter ;

call test();

/*#3 - creates and calls proc test
#calculates 10! then displays a user friendly message
drop procedure if exists test;*/

delimiter //

create procedure test()
begin
	declare i int default 10;
	declare ten_factorial int default 1;
	
	while i > 0 do
		set ten_factorial = ten_factorial * i;
		set i = i-1;
	end while;

	select concat("The factorial of 10 is: ",format(ten_factorial,0),".") as message;

end//

delimiter ;

call test();

/*4 - creates a stored procedure named test
#creates a cursor for a result set that consists of the vendor_name, invoice_number,
#and balance_due for each invoice with a balance >=5000
#rows in this result set sorted in descending sequence by balance due
#procedure displays a string that includes balance due, invoice number, and vendor name for each invoice
#w/ each column separated by pipe (|) and rows separated by (//)
drop procedure if exists test;*/

delimiter //

create procedure test()
begin
	-- variable declaration
	declare s 					varchar(4000)	default '';
	declare vendor_name_var 	varchar(50);
	declare invoice_number_var 	varchar(50);
	declare balance_due_var		decimal(9,2);
	
	-- cursor and row end declaration
	declare row_not_found 		tinyint 		default false;
	declare vendor_cursor cursor for
		select vendor_name, invoice_number, 
			invoice_total - payment_total - credit_total as balance_due
		from vendors v join invoices i 
			on v.vendor_id = i.vendor_id
		where invoice_total - payment_total - credit_total >= 5000
		order by balance_due desc;

	-- cursor error handle
	declare continue handler for not found
		set row_not_found = true;

	-- open cursor
	open vendor_cursor;

	-- cursor loop
	while row_not_found = false do
		fetch vendor_cursor into vendor_name_var, invoice_number_var, balance_due_var;
	-- procedure for each row
		set s = concat(s,vendor_name_var,'|',invoice_number_var,'|',balance_due_var,'//');
	end while;
	
	-- close cursor
	close vendor_cursor;

	-- print output
	select s as message;

end//

delimiter ;

call test();

/*5 - creates and calls stored procedure test
#attempts to update invoice_due_date column = NULL for invoice_id =1.
#Displays "1 row was updated." if successful; 
#else, displays "Row was not updated - column cannot be null."*/

drop procedure if exists test;

delimiter //

create procedure test()
begin	
	-- declare error var
	declare null_value 	tinyint		default false;
	-- create conditions for error
	declare continue handler for 1048
		set null_value = true;
	
	-- try to update value	
	update invoices
	set invoice_due_date = NULL
	where invoice_id = 1;
	-- create and display message
	if null_value = TRUE then
		select 'Row was not updated - column cannot be null.' as message;
	else
		select '1 row was updated' as message;
	end if;	
end //

delimiter ;

call test();

/*6 - creates and calls stored procedure test
#Displays all prime numbers less than 100 */

-- kill old procedure test
drop procedure if exists test;
-- change delimeter for stored procedure
delimiter //

-- build procedure
create procedure test()
begin
	-- declare necessary variables
	declare i int			default 3;
	declare j int;			
	declare s varchar(400) 	default '2 |';
	declare divisor_found	tinyint	default false;

	-- while there are still numbers to test	
	while i < 100 do
	-- set j = largest possible divisor != i
		set j = i-1;
		-- while there are still divisors to test

		while j>1 do
			-- if j is a divisor
			if i%j = 0 then 
				-- satisfy condition to end the loop
				set j = 1;
				-- note that divisor is found, means i is not prime
				set divisor_found=true;
			-- else keep looking for a divisor
			else set j=j-1;
			end if;
		end while;	

		-- if we didn't find a divisor then this number is prime, add it to our string
		if divisor_found = false then
			set s = concat(s, i, ' | ');
		end if;
		
		-- choose our next i
		set i = i+2; -- skips all even numbers > 2
		set divisor_found = false;
	end while;
	select s as "prime number string";

end//

-- change delimiter for future scripts
delimiter ;

-- call new procedure
call test();

 
/*7 - enhances exercise 4 to show invoice data in three groups based on the balance due amount
# $20,000 or more, $10,000 to $20,000, $5,000 to $10,000 */

drop procedure if exists test;

delimiter //

create procedure test()
begin
	-- variable declaration
	declare s 					varchar(4000)	default '';
	declare vendor_name_var 	varchar(50);
	declare invoice_number_var 	varchar(50);
	declare balance_due_var		decimal(9,2);
	declare row_not_found 		tinyint 		default false;

	declare vendor_cursor cursor for
		select vendor_name, invoice_number, 
			invoice_total - payment_total - credit_total as balance_due
		from vendors v join invoices i 
			on v.vendor_id = i.vendor_id
		where invoice_total - payment_total - credit_total >= 5000
		order by balance_due desc;

	-- loop 1
	begin
	-- cursor error handle
	declare exit handler for not found
		set row_not_found = true;
	-- open cursor
	open vendor_cursor;
	-- cursor loop
	set s = concat(s,'$20,000 or More: ');
	while row_not_found = false do
		fetch vendor_cursor 
		into vendor_name_var, invoice_number_var, balance_due_var;
	-- procedure for each row where balance_due_var > $20,000
		if balance_due_var >= 20000 then	
			set s = concat(s,vendor_name_var,'|',invoice_number_var,'|',balance_due_var,'//');
		end if;
	end while;
	end;
	-- close cursor
	close vendor_cursor;

	-- loop 2
	set row_not_found = false;
	begin
	-- cursor error handle
	declare exit handler for not found
		set row_not_found = true;
	-- open cursor
	open vendor_cursor;
	-- cursor loop
	set s = concat(s,'$10,000 to $20,000: ');
	while row_not_found = false do
		fetch vendor_cursor 
		into vendor_name_var, invoice_number_var, balance_due_var;
	-- procedure for each row where balance_due_var between $10000 and $20000
		if balance_due_var >= 10000 and balance_due_var <20000 then	
			set s = concat(s,vendor_name_var,'|',invoice_number_var,'|',balance_due_var,'//');
		end if;
	end while;
	end;
	
	-- close cursor
	close vendor_cursor;

	-- loop 3
	set row_not_found = false;
	begin
	-- cursor error handle
	declare exit handler for not found
		set row_not_found = true;
	-- open cursor
	open vendor_cursor;
	-- cursor loop
	set s = concat(s,'$5,000 to $10,000: ');
	while row_not_found = false do
		fetch vendor_cursor 
		into vendor_name_var, invoice_number_var, balance_due_var;
	-- procedure for each row where balance_due_var bbetween $5,000 and $10,000
		if balance_due_var >= 5000 and balance_due_var < 10000 then	
			set s = concat(s,vendor_name_var,'|',invoice_number_var,'|',balance_due_var,'//');
		end if;
	end while;
	end;
	
	-- close cursor
	close vendor_cursor;

	-- print output
	select s as message;

end//

delimiter ;

call test();