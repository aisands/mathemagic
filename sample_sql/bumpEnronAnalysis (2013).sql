use test;
drop table if exists enron;

create table enron (
	sendTime	int not null,
	fromEmail	varchar(256),
	toEmail		varchar(256)
);

#create table to avoid multiple reads of space delimited file
load data infile 'D:/enron.txt' into table enron fields terminated by ' ';

/* ---- query design ----
>groups emails by unique from/to email combinations
>checks that emails happened around lunchtime (set between 11:30 and 1:30). 
	time period could be altered with cultural research on when most people got lunch
 	or additional analysis on lunch clock in/ clock out times
>excludes help desk, announcement, maintenance, non @enron.com emails
>excludes email sent to self
>uses percentage of total emails sent by users to contacts to account for skew by massive emailers
*/

use test;

drop table if exists lunchCorrespondence;
create table lunchCorrespondence (
	fromEmail	varchar(256),
	toEmail		varchar(256),
	numEmails	int
);

#returns top 500 lunch pairs for query performance

insert into lunchCorrespondence (
	select fromEmail, toEmail, count(*)
	from enron
	#checks if emails sent around lunch time
	where FROM_UNIXTIME(sendTime,'%T') >= '11:30:00' and FROM_UNIXTIME(sendTime,'%T') <= '13:30:00'
	#excludes email sent to self
	and fromEmail != toEmail
	#excludes email sent to all staff
	and not toEmail REGEXP '^(all|enron|maintenance)'
	and toEmail REGEXP '@enron.com$'
	and not fromEmail REGEXP '^(announcements|enron|maintenance)'
	and fromEmail REGEXP '@enron.com$'
	#groups emails by unique to/from combinations
	group by fromEmail,toEmail
	order by count(*) desc
	limit 500
	);

drop table if exists lunchEmailTotal;

create table lunchEmailTotal (
	fromEmail varchar(256),
	numLunchEmails	int
);

#gathers the number of total emails they sent around lunch time
insert into lunchEmailTotal(
	select fromEmail, sum(numEmails)
	from lunchCorrespondence
	group by fromEmail
	order by sum(numEmails) desc
);

select c.fromEmail, c.toEmail, c.numEmails, 
	concat(cast((c.numEmails/t.numLunchEmails)*100 as char(3)),'%') as "% senders lunch emails"
from lunchCorrespondence c
	join lunchEmailTotal t
		on c.fromEmail = t.fromEmail
group by fromEmail, toEmail
order by numEmails/numLunchEmails desc;

/*other approaches:
1. compare punch in/ punch out data, add to email frequency analysis (new data)
2. compare office proximity (new data)
3. compare team membership, account similarities (new data)
4. compare work day start/ end times (could indicate companionship, new data)
5. analyze subject lines (exclude emails with account numbers, marked as confidential, etc. include emails w/ string "lunch") (new data)
6. consider emails throughout the day instead of just around lunch time
7. consider balance between sent and received emails between pairs 

issues:
1. entries show up twice (to A from B, to B from A)
2. slow query speed/ unable to make indices
*/
