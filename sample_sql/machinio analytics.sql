-- create database machinio;
use machinio;

drop table if exists machinioAnalytics;
create table machinioAnalytics (
	trafficDay	char(50) primary key,
	numVisitors	int
);

load data local infile 'C:/Users/FruityLoops/Documents/R/machinio.txt'
	into table machinioAnalytics
	fields terminated by '	';		

select min(numVisitors), max(numVisitors), avg(numVisitors)
from machinioAnalytics;

