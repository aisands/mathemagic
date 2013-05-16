*Author: Adrienne Sands (2010)
*Sample code only. Please see /sample_analysis/sample data analysis 3 for full analysis
*Questions from: http://www.math.wustl.edu/~jmding/math3200/chw/hw3.html

TITLE "Homework 3 Question 5.22a and b";
data hw3q1a;
	do i=1 to 100;
		array z(4);
		do j=1 to 4;
			z[j]=rand('NORMAL',0,1);
		X= z[1]**2 + z[2]**2 + z[3]**2 + z[4]**2; 
	end;
	output;
	end;
	drop i j;
	run;
*Only first page of output included;
proc print data=hw3q1a;
run;
proc univariate data=hw3q1a; 
var X;
run;

TITLE "Homework 3 Question 5.22b";
data dataset; 
p_25=cinv(.25,4);
p_50=cinv(.5,4);
p_90=cinv(.9,4);
proc print data=dataset;
run;

TITLE "Homework 3 Question 5.28a and b";
data hw3q2;
call streaminit(12345);
do i=1 to 100;
Z=rand('NORMAL',0,1);
U=rand('CHISQUARE',4);
T=Z/sqrt(U/4);
output;
end;
drop i;
run;
*Only first page of output included;
proc print data=hw3q2;
run;
proc univariate data=hw3q2;
var T;
run;’

TITLE "Homework 3 Question 5.28b";
data hw3q2b;
p_25=tinv(.25,4);
p_50=tinv(.5,4);
p_90=tinv(.9,4);
proc print data= hw3q2b;
run;

TITLE "Homework 3 Question 6.12a";
data hw3q3a;
*Optional: For part B, change 20 to 100;
	do i=1 to 25;
		array z(20);
		do j=1 to 20;
			z[j]=rand('NORMAL',50,6);
			zmean=mean(of z1-z20);
			zlower=zmean-1.96*6/sqrt(20);
			zupper=zmean+1.96*6/sqrt(20);
			CI_50=(zlower<=50 and zupper>=50);
			CI_53=(zlower<=53 and zupper>=53);
	end;
	output;
	end;
	drop i j;
	run;
proc print data=hw3q3a;
*Optional: If CL_50= 1, then the intervals contain the true mean;
*Optional: If CL_53= 1, then the intervals contain the wrong mean 53;
var zmean zlower zupper CI_50 CI_53;
run;


TITLE "HW 3 Question 6.23";
data hw3q4;
call streaminit(12345);
do i=1 to 100;
array z(9);
do j=1 to 9;
z[j]=rand('NORMAL',0,1);
end;
zmean=mean(of z1-z9);
zstat=zmean/(1/sqrt(9));
*Type=1 means a type 1 error has been committed;
*Type=0 means a type 1 error has not been committed;
if zstat>1.645 then Type=1;
else Type=0;
output;
end;
drop i j;
run;
TITLE "HW 3 Question 6.23: Frequency of Type I Error";
proc freq data=hw3q4;
tables Type;
run;



TITLE "Homework 3 6.23b";
data hw3q4b;
call streaminit(12345);
do i=1 to 100;
array x(9);
do j=1 to 9;
x[j]=rand('NORMAL',1,1);
end;
xmean=mean(of x1-x9);
*Type=2 means a type 2 error has been committed;
*Type=0 means a type 2 error has not been committed;
if xmean<0.548333333 then Type=2;
else Type=0;
output;
end;
drop i j;
run;
TITLE "HW 3 Question 6.23b: Frequency of Type II Error";
proc freq data=hw3q4b;
tables Type;
run;
