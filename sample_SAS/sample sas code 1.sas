*Author: Adrienne Sands (2010)
*Sample code only. Please see /sample_analysis/sample data analysis 3 for full analysis
*Questions from: http://www.math.wustl.edu/~jmding/math3200/chw/hw1.html 

*Program for 1a;	
data mydata;
call streaminit(123456);
do i=1 to 100;
X_i=rand('uniform');
Y_i=1+floor(10*X_i);
put Y_i;
output;
end;
TITLE 'Homework 1: 1a';
proc print data=mydata;
proc means data=mydata mean stddev;
var X_i;
proc freq data=mydata;
table Y_i;
run;

*Program for 1b;
data mydata2;
      call streaminit(12345);
      do i=1 to 10000;
      XX=rand('uniform');
      YY=1+floor(10*XX);
      put YY;
      output;
      end;
	  TITLE "Homework 1:1b";
proc means mean stddev min max;
var XX;
proc freq data=mydata2;
table YY;
run;

*Program for 2;
data normdata;
do i=1 to 10000;
X_i=0.526+0.0035*rannor(92641);
Y_i=0.525+0.0043*rannor(23423);
if Y_i<X_i then K_i=1;
else K_i=0;
output;
end;
TITLE "Homework 1:2";
proc means mean stddev;
var X_i;
var Y_i;
proc freq data=normdata;
tables K_i;
run;
