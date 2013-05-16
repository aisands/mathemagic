*Author: Adrienne Sands (2010)
*Sample code only. Please see /sample_analysis/sample data analysis 2 for full analysis
*Questions from:  http://www.math.wustl.edu/~jmding/math3200/chw/hw2.html

*PROBLEM 1:
**For a randomized schedule of the procedures;
OPTIONS LS=72 PS=60 CENTER NONUMBER;
DATA hw2data1a;
TITLE "HW2 Q1: Randomized Schedule of Pretzel Runs";
INPUT Name$ Method$;
CALL streaminit (12345);
RandomValue=rand('uniform');
DATALINES;
WorkerA 	Method1
WorkerA 	Method2
WorkerA 	Method3
WorkerB 	Method1
WorkerB 	Method2
WorkerB 	Method3
WorkerC 	Method1
WorkerC 	Method2
WorkerC 	Method3
;
proc sort data=hw2data1a OUT=hw2data1b;
by RandomValue;
RUN;
proc print data=hw2data1b (DROP=RandomValue);
RUN;

*PROBLEM 2:
OPTIONS LS=72 PS=60 CENTER NONUMBER;
TITLE "HW2 Q2: pH Measurements on Soil Samples";
data hw2data2;
INPUT PH @@;
DATALINES;
6.10	6.74	6.22	5.65	6.38	6.70	7.00	
6.43	7.00	6.70	6.70	5.94	6.28
6.34	6.62	6.55	2.92	6.10	6.20	6.70
7.00	6.85	6.31	6.26	6.36	6.28
6.38	6.70	6.62	7.00	6.45	6.31
2.86	6.31	6.09	6.17	6.64	6.45
7.00	6.18	6.58	5.38	6.34	7.00
5.70	6.65	6.56	6.00	6.70	6.45
;
**For more readable output of five number summary;
TITLE "HW2 Q2: Five Number Data Summary";
proc means DATA= hw2data2 min Q1 median Q3 max mean stddev skew ;
Var PH;
RUN;
**For more comprehensive summary statistics/ trimmed mean output;
TITLE "HW2 Q2: Trimmed Mean Output";
proc univariate data=hw2data2 trimmed=0.1;
VAR PH;
RUN;  
**For 4.15, the data is plotted without the 10% trim;
TITLE "HW2 Q2: Plot Outputs";
proc univariate data=hw2data2 plots;
VAR PH;
PROBPLOT PH/ normal (mu=est sigma=est) pctlminor;
RUN;

*PROBLEM 3:
OPTIONS LS=72 PS=60 CENTER NONUMBER;
TITLE "HW2 Q3: Initial Joint Impairment Scores";
Data hw2data3;
INPUT Score @@;
log_score= log(Score);
DATALINES;
6	5	10	9	13	8	8	22	9	18	3
12	11	14	8	32	9	12	17	6	14	9
4	18	18	14	22	9	2	5	3	3	29
;
TITLE "HW2 Q3: Normal Plots";
proc univariate data=hw2data3;
**Rotated to put Score on X axis to compare with normalized transformation*
*Normal Plot of Score;
PROBPLOT Score/normal (mu=est sigma=est) pctlminor ROTATE;

*Normal Plot of log(Score);
PROBPLOT log_Score/normal (mu=est sigma=est) pctlminor ROTATE;
RUN;

*PROBLEM 4:
OPTIONS LS=72 PS=60 CENTER NONUMBER;
Data hw2data4;
TITLE "Annual Snowfall and Unemployment Rate in Amherst, MA";
INPUT Year Snowfall Unemployment@@;
DATALINES;
1973	45	4.9
1974 	59	5.6
1975	82	8.5
1976	80	7.7
1977	71	7.1
1978	60	6.1
1979	55	5.8
1980	69	7.1
1981	79	7.6
1982	95	9.7
;
TITLE "Unemployment vs. Snowfall";
TITLE2 "Scatter Plot";

PROC gPlot DATA= hw2data4;
PLOT Unemployment*Snowfall;
RUN; 

TITLE2 "Covariance and Correlation Coefficient";
PROC corr DATA=hw2data4 COV;
VAR Unemployment Snowfall;
RUN;
