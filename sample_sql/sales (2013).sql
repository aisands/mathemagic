--Author: Adrienne Sands (2013)
--Purpose: http://www.programmerinterview.com/index.php/database-sql/practice-interview-question-1/
use test;
drop table if exists Salesperson;

create table Salesperson ( 
	salesperson_id	int	primary key	not null,
	salesperson_name char(40)	not null,
	age	int,
	salary	int	not null
);

insert into Salesperson values
(1,"abe",61,140000),
(2,"bob",34,44000),
(5,"chris",34,40000),
(7,"dan",41,115000),
(8,"ken",57,115000),
(11,"joe",38,38000);

drop table if exists Customer;

create table Customer (
customer_id	int	not null primary key,
customer_name	char(40)	not null,
city	char(40),	
industryType char(1)	not null
);

create index industryTypeIX on Customer (industryType);

insert into Customer values
(4, "Samsonic", "pleasant", "J"),
(6, "Panasung", "oaktown", "J"),
(7, "Samony","jackson", "B"),
(9,	"Orange", "Jackson", "B");

set @@auto_increment_increment = 1;

drop table if exists Orders;

create table Orders (
	Numbers	int	primary key	not null auto_increment,
	order_date date not null,
	customer_id	int	not null,
	salesperson_id	int	not null,
	amount	int	not null,
	foreign key customer_id_fk (customer_id) references Customer (customer_id),
	foreign key salesperson_id_fk (salesperson_id) references Salesperson (salesperson_id)
);

insert into Orders values 
(default, "1996/08/02",4,2,540),
(default,"1999/01/30",4,8,1800),
(default,"1995/07/14",9,1,460),
(default,"1998/01/29",7,2,2400),
(default,"1998/02/03",6,7,600),
(default,"1998/03/02",6,7,720),
(default,"1998/05/06",9,7,150);

select salesperson_name 
from Salesperson s 
	join Orders o
		on s.salesperson_id = o.salesperson_id
	join Customer c
		on o.customer_id = c.customer_id
where customer_name = "samsonic";
#returns bob and ken

select distinct s.salesperson_name 
from Salesperson s
where salesperson_name not in (select salesperson_name 
		from Salesperson p 
		join Orders o
			on p.salesperson_id = o.salesperson_id
		join Customer c
			on o.customer_id = c.customer_id
		where customer_name = "samsonic")
order by salesperson_name;

select salesperson_name
	from Salesperson s
		join (
		select salesperson_id, count(*)
		from orders
		group by salesperson_id
		having count(*) > 1) moreThan2
	on s.salesperson_id = moreThan2. salesperson_id
	order by salesperson_name;

drop table if exists highAchiever;

create table highAchiever (
	highAchiever_name char(40) primary key,
	age	int	not null
);

insert into highAchiever
    (select salesperson_name, age
	from Salesperson
	where salary > 100000);

use test;
update Salesperson
set salary = 52000
where salesperson_name = "dan";

select highAchiever_name from highAchiever;







