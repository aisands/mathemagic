*Author: Adrienne Sands (2010)
*Sample code only. Please see /sample_analysis/sample data analysis 4 for full analysis
*Questions from: http://www.math.wustl.edu/~jmding/math3200/chw/hw4.html

*PROBLEM 1:
TITLE "Homework 4 Question 1";
data hw4q1;
	do i=1 to 1000;
		array z(5);
		do j=1 to 5;
			z[j]=rand('NORMAL',7,5);
	zmean= mean(of z1-z5);
	zstdev= std(of z1-z5);

	zlower= zmean-1.96*zstdev/sqrt(5);
	zupper= zmean+1.96*zstdev/sqrt(5);
*Note: n=5 for each sample, so df=4 and alpha/2=0.05/2=0.025;
	
tlower= zmean-2.776*zstdev/sqrt(5);
	tupper= zmean+2.776*zstdev/sqrt(5);
	if zlower<7 and zupper> 7 then XZ=1;
	else XZ=99;
	if tlower<7 and tupper>7 then XT=1;
	else XT=99; 
	end;
	output;
	end;
	drop i j;
	run;
*Only the first page of the SAS output has been included;
proc print data=hw4q1;
var zmean zstdev zlower zupper tlower tupper;
proc freq data=hw4q1;
tables XZ XT;
run;


*PROBLEM 2:
TITLE "Homework 4 Question 2";
data hw4q2;                                                                                                                            
input rating @@;                                                                                                                           
datalines;
87.5	86.9	86.6	87.3	87.9	88	86.7	87.5	87.2	87
88.1	87.5	86.5	87.7	88	87.1	87	87.6	87.5	88.3
;
run;
proc univariate data=hw4q2 cibasic(type=lower alpha=.05);
var rating;
qqplot;
run;
TITLE2 "T-Test with H0: mu=87";
proc ttest data=hw4q2 h0=87;
var rating;
run;


*PROBLEM 3:
TITLE "Homework 4 Question 3"
data hw4q3;
	input results @@;
	datalines;
	125 123 117 123 115
	112 128 118 124 111
	116 109 125 120 113
	123 112 118 121 118
	122 115 105 118 131
	;
	run;
TITLE "HW 4, Q3: Testing Normality Assumption";
proc CAPABILITY data=hw4q3;
	qqplot;
run;
TITLE "HW 4, Q3: Upper One-Sided 90% CI"
proc univariate data= hw4q3 alpha=0.1 cibasic(type=upper alpha=.1);
	run;
