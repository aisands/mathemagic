*Author: Adrienne Sands (2010)
*Sample code only. Please see /sample_analysis/sample data analysis 5 for full analysis
*Questions from: http://www.math.wustl.edu/~jmding/math3200/chw/hw6.html

*PROBLEM 1:
TITLE "Homework 6 Question 1";
data hw6q1;                                                                                                                            
input CityType $ Action $ Wallets @@;
datalines;
Big		Returned 21 Big		Kept	9
Suburbs	Returned 18	Suburbs	Kept	12
Medium	Returned 17	Medium	Kept	13
Small		Returned 24	Small		Kept	6
;
run;
proc freq data=hw6q1 order=data;
table CityType*Action / chisq;
weight Wallets;
run;


*PROBLEM 2:
TITLE "Homework 6 Question 2";
data hw6q2;                                                                                                                            
input LAST NEXT @@;
datalines;
 
2.0	50
1.8	57
3.7	55
2.2	47
2.1	53
2.4	50
2.6	62
2.8	57
3.3	72
3.5	62
3.7	63
3.8	70
4.5	85
4.7	75
4.0	77
4.0	70
1.7	43
1.8	48
4.9	70
4.2	79
4.3	72
 
;
run;
proc gplot data=hw6q2;
plot NEXT*LAST;
run;
proc reg lineprinter;
model NEXT=LAST / r;
plot NEXT*LAST= 'Y' predicted.*LAST'P'/ overlay;
plot residual.*LAST = '*';
run;


*PROBLEM 3:
TITLE "Homework 6 Question 3";
data hw6q3;    
input h l  @@;
x=log(l);
y=log(h);
*For hospital cost h and length of stay l*;
*Data entered in single column in SAS. Listed as two columns to save paper*;

datalines;
 
13728	13
8062	8
4805	13
5099	6
14963	33
4295	2
4046	9
3193	13
15486	16
9413	11
9034	19
8939	20
17596	26
1884	3
1763	5
1233	1
6286	30
2849	4
2818	4
2265	2
1652	9
1846	4
25460	18
4570	16
12213	10
5870	12
24484	52
4735	19
13334	9
35381	85
5681	8
7161	20
10592	41
 
;
proc gplot data=hw6q3;
plot y*x;
run;
proc reg lineprinter;
model y=x / r clb corrb;
run;
quit;
Title 'Calculation and Test of Correlations, 95% CI';
ods output FisherPearsonCorr=corr;
proc corr data=hw6q3 fisher ( biasadj=no );
var x y;
run;


*PROBLEM 4:
TITLE "Homework 6 Question 4";
data hw6q4;    
input y x1 x2 x3 @@;
label y="Performance IQ" 	x1="Brain Size"	x2="Height"	x3= "Weight";
datalines;
124	81.69	64.50	118
150	103.84	73.30	143
128	96.54	68.80	172
134	95.15	65.00	147
110	92.88	69.00	146
131	99.13	64.50	138
98 	85.43	66.00	175
84	90.49	66.30	134
147	95.55	68.80	172
124	83.39	64.50	118
128	107.95	70.00	151
124	92.41	69.00	155
147	85.65	70.50	155
90	87.89	66.00	146
96	86.54	68.00	135
120	85.22	68.50	127
102	94.51	73.50	178
84	80.80	66.30	136
74	93.00	74.00	148
86	88.91	70.00	180
84	90.59	76.50	186
134	79.06	62.00	122
128	95.50	68.00	132
102	83.18	63.00	114
131	93.55	72.00	171
84	79.86	68.00	140
110	106.25	77.00	187
72	79.35	63.00	106
124	86.67	66.50	159
132	85.78	62.50	127
137	94.96	67.00	191
110	99.79	75.50	192
86	88.00	69.00	181
81	83.43	66.50	143
128	94.81	66.50	153
124	94.94	70.50	144
94	89.40	64.50	139
89	93.59	75.50	179
;
proc reg lineprinter;
model y=x1 x2 x3 / r clb corrb;
run;
quit;
Title 'Calculation and Test of Correlations, 95% CI';
ods output FisherPearsonCorr=corr;
proc corr data=hw6q3 fisher ( biasadj=no );
var x y;
run;
