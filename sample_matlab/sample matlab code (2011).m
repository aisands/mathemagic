%Author: Adrienne Sands (2011)
%Sample code only. Please see /sample_analysis/sample nonparametric analysis for full analysis
%Questions available here: http://www.math.wustl.edu/~nlin/math408/exam/final.htm


%%%Question 1
control = [1 1 2 2 3 4 4 5 5 8 8 8 11 11 12 12]';
control_censoring = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]';
drug = [6 6 6 6 7 9 10 11 11 16 17 19 20 25 32 32]';
drug_censoring = [0 0 0 1 0 1 1 0 1 0 1 1 1 0 1 1]';
 
x1 = [control control_censoring];
x2 = [drug drug_censoring];
 
logrank(x1,x2, 0.05)

%%%Question 2

data = xlsread('prob2');
x = data(:,1);
y = data(:,2);
index = [1:size(data,1)]';
 
disp(' ');
disp('Pearson (rho), Kendall tau, and Spearman (R) correlation coefficients:');
disp('See Section 8.2 in text for Kendall tau and Section 8.5 for Spearman R');
 
% Rewrite data as one nnx3 array
ww = [index data];
nn=size(ww,1);      % Number of rows
ww=sortrows(ww,1);  % Sort on ordinal number
 
% Fetch Xs and Ys as nnx1 column vectors and wdat as [X Y];
xx=ww(:,2);  yy=ww(:,3);
wdat = [xx yy];
 
disp(' ');
disp('Pearson rho for X vs Y and Student-t P-value:');
Meanx=sum(xx)/nn;  Meany=sum(yy)/nn;
xxc=xx-Meanx;  yyc=yy-Meany;
sxx=sum(xxc.*xxc);  sxy=sum(xxc.*yyc);  syy=sum(yyc.*yyc);
 
rho = sxy/sqrt(sxx*syy);
tt = rho*sqrt((nn-2)/(1-rho*rho));
df=nn-2;
Tpval = pvtdist(tt,df);
 
fprintf ('  Rho=%g   T=%g   P=%6.4f  (df=%d)\n', rho, tt, Tpval, df);
disp(' ');
disp(' ');
disp('Kendall K and Kendall tau (assuming no ties):');
kstat=0;
for i=1:nn;  for j=i+1:nn;
  qq = (xx(j)-xx(i))*(yy(j)-yy(i));
  if (qq>0) kstat=kstat+1;
  elseif (qq<0) kstat=kstat-1;  end;
  end;  end;
tau=(2*kstat)/(nn*(nn-1));
var_noties = nn*(nn-1)*(2*nn+5)/18
zval = kstat/sqrt(var_noties);
Kpval = normpval(zval);
fprintf('  K=%g   tau=%g   Z=%g   P=%6.4f (2-sided)\n', kstat,tau,zval,Kpval);
 
[xmidr  xtiegr] = getmidranks(xx);
[ymidr  ytiegr] = getmidranks(yy);
ww = [ww(:,1)  xx  xmidr  yy  ymidr  xtiegr  ytiegr];
 
%to correct for ties
%Calculated by hand since there were so few ties
var_ties = (nn*(nn-1)*(2*nn + 5) - 2*(2-1)*(2*2 + 5))/18
var_noties
 
zval_ties = kstat/sqrt(var_ties);
Kpval_ties = normpval(zval_ties);
fprintf('  K=%g   tau=%g   Z=%g   tiecorrected P=%6.4f (2-sided)\n', kstat,tau,zval,Kpval_ties);
 
 
% Center midranks at average rank
rxc=xmidr - (nn+1)/2;  ryc = ymidr - (nn+1)/2;
% Spearman R correlation coefficient
rr = 12*sum(rxc.*ryc)/((nn-1)*nn*(nn+1));
% Large-sample normal approximation
zz = sqrt(nn-1)*rr;
Rpval = normpval(zz);
 
disp(' ');
disp(' ');
disp('Spearman R, large-sample Z, large-sample P-value:');
fprintf('    %6.4f    %6.4f    %6.4f (2-sided)\n', rr, zz, Rpval);
 

%%%Question 3

data = xlsread('prob2');
x = data(:,1);
y = data(:,2);
x0= linspace(min(x),max(x),20);
 
% Set some possible values for alpha.
alpha = 0:0.25:10;
CV = zeros(1,length(alpha));
for i = 1:length(CV);
    [x0, fhat, S] = cssplinesmth(x,y,alpha(i));
    num = y - fhat;
    den = 1 - diag(S);
    CV(i) = mean((num./den).^2);
end
% Find the minimum value of CV(alpha).
[m,ind] = min(CV);
% Find the corresponding alpha.
cvalpha = alpha(ind);
 
% Plot the CV function.
plot(alpha,CV)
 
result = cssplinesmth(x,y,cvalpha);
plot(x,y, 'k.', x0, result, 'k')
xlabel('x'),ylabel('y')
title('Smoothing spline with alpha found by CV')

 %%%Question 4

%Data
stimulant = [1; 1; 2; 1; 1; 2; 1; 1; 2; 1; 1; 2; 1; 1; 2; 1; 1; 2; 1];
reactiontime = [1.94; 3.27; 3.27; 1.94; 3.27; 3.27; 2.92; 3.27; 3.27;
    2.92; 3.70; 3.70; 2.92; 3.70; 3.70; 2.92; 3.74; 3.74; 3.27];
data= [stimulant reactiontime];
 
%Nonparametric analysis: Kruskal-Wallis test for no differences in treatment effect
%HO: Stimulant 1 effect equals Stimulant 2 effect
%HA: Stimulant 1 effect does not equal Stimulant 2 effect
 
%Data sorted by reaction time
sorted = sortrows(data);
 
%Total number of observations
num = size(sorted,1);
 
%Data and observations for stimulant 1
data_1 = [sorted(1:13,1) sorted(1:13,2)];
n1 = size(data_1,1)
 
%Data and observations for stimulant 2
data_2 = [sorted(14:num,1) sorted(14:num,2)];
n2 = size(data_2,1)
 
ordered = sortrows(data,2);
 
%Distinct reaction times (for tie correction)
distinctTimes = unique(ordered(:,2));
 
%Indices used to calculate average rank
index = [1:size(ordered)]';
ordered = [index ordered];
 
avgRank = zeros(size(distinctTimes,1),1);
counted = zeros(size(distinctTimes,1),1);
 
for i = 1:size(distinctTimes,1)
temp = 0;
count = 0;
%counts number of observations for each distinct reaction time and sums
%ranks without ties
for j= 1:size(ordered,1)
if ordered(j,3) == distinctTimes(i)
temp = temp + ordered(j,1);
count = count+1;
end
%average ranks to account for times
avgRank(i) = temp/count;
counted(i) = count;
end
end
 
distinctRanks = [avgRank distinctTimes]
 
rank = zeros(size(ordered,1),1);
 
%matches ranks to each observation
for i = 1:size(rank,1)
    for j = 1:size(distinctRanks,1)
        if ordered(i,3)== distinctRanks(j,2)
            rank(i)=distinctRanks(j);
        end
    end
end
 
orderednew = [rank ordered(:,2) ordered(:,3)];
sortednew = sortrows(orderednew,2);
 
new_1 = [sortednew(1:13,1) sortednew(1:13,3)];
new_2 = [sortednew(14:num,1) sortednew(14:num,3)];
 
%Sum of joint rankings for stimulant 1 observations
R1_temp = sum(new_1,1);
R1 = R1_temp(1,1);
 
%Sum of joint rankings for stimulant 2 observations
R2_temp = sum(new_2,1);
R2 = R2_temp(1,1);
%Calculates Kruskal-Wallis test statistic and large sample approximated p-value
H = ((12/(num*(num+1)))*((R1*R1/n1)+ (R2*R2/n2))) - 3*(num +1)
largesamplepvalue = pvchisq(H,1)
 
tiegroups = size(distinctRanks,1)
 
for i = 1:tiegroups
tj = counted(i);
tiesum = tiesum + (tj^3 - tj);
end
 
%Tie corrects Kruskal-Wallis test statistic and calculates large sample
%approximated p-value
Hprime = H/(1-(tiesum/(num^3 - num)))
tiecorrectedpvalue = pvchisq(Hprime,1)
 
 
%Parametric analysis: Two-sample t-test
[ttestresult,p,ci,stats] = ttest2(new_1(:,2),new_2(:,2),0.05,'both')

%%%Question 5


%Data
x = [30; 21; 41; 83; 76; 89; 35; 78; 39; 38; 57; 98; 64; 34; 55; 44; 22; 56; 74; 43;
    40; 54; 27; 77; 90; 97; 93; 80; 73; 67; 72; 88; 94; 84; 86; 60; 99; 46; 66; 75];
y = [3; 5; 5; 6; 9; 17; 22; 23; 27; 31; 31; 38; 40; 42; 56; 62; 64; 66; 142; 159;
    168; 170; 180; 197; 217; 235; 250; 354; 368; 441; 486; 622; 642; 659; 773; 
    850; 902; 1090; 1658; 4032];
index = [1:size(x)]';
data = [index x y];
nn = size(data,1);
 
 
disp('Theil`s Method for Estimation of Slope and testing');
disp('  H_0:beta=beta_0 for a simple regression');
disp('See Sections 9.1-9.3 in text');
 
% Are there any ties?
[midrx  xties] = getmidranks(x);
xg=0;
for i=1:nn;  
  if xties(i)>0 xg=i;  else break;  end;  end;
 
[midry  yties] = getmidranks(y);
yg=0;
for i=1:nn;  
  if yties(i)>0 yg=i;  else break;  end;  end;
fprintf('\nWithin-sample tie groups:  X: %d   Y: %d\n', xg, yg);
if xg==0 && yg==0  disp('NO TIES in Xs or Ys');  end;
%% NOTE:
%% If there are ties, use the tie correction for Kendall`s test
%%   from Section 8.1 page 366 in text
 
disp(' ');
disp('Theil`s test of H_0:beta=0  (same as Kendall`s test)');
disp('(NOT assuming that X(i) are increasing, so different from text)');
c=0;
for i=1:nn;  for j=i+1:nn;
  z = (y(j)-y(i))*(x(j)-x(i));
  if (z>0) c=c+1;
  elseif z<0 c=c-1;  end;  end;  end;
varC = nn*(nn-1)*(2*nn+5)/18;
z = c/sqrt(varC);
fprintf('  C=%d   Z=%6.4f   P=%6.4f (Assuming no ties)\n', ...
  c, z, normpval(z));
 
 
%% Compare with least-squares regression estimates
ymean=sum(y)/nn;  xmean=sum(x)/nn;
yc=y-ymean;    xc=x-xmean;
ssx = sum(xc.*xc);
beta_lsq = sum(yc.*xc)/ssx;
mu_lsq = ymean - beta_lsq*xmean;
resid_lsq = y - beta_lsq*x - mu_lsq;
 
disp(' ');
disp('Normal-theory test of H_0:beta=0  (Student-t test)');
mse = sum(resid_lsq.*resid_lsq)/(nn-2);
t = beta_lsq/sqrt(mse/ssx);
fprintf('  beta_hat=%6.4f   T=%6.4f   P=%6.4f  (df=%d)\n', ...
  beta_lsq, t, pvtdist(t,nn-2), nn-2);
disp('  (For normal-theory test, note huge outliers in Y_i.)');
 
disp(' ');
disp('SIMPLE REGRESSION OF Y on X  (Y = beta*X + mu)');
disp(' ');
disp('Theil`s estimate of beta is essentially the Hodges-Lehmann');
disp('  estimator of beta based on the Kendall (or Kendall tau) test.');

% Estimate beta=beta_hat = median of slopes (Y_i-Y_j)/(X_i-X_j)
% Fill array of slopes:
slopes=zeros(1,nn*nn+3);  nd=0;
for i=1:nn;  for j=i+1:nn;
  xdiff=x(j)-x(i);
  if xdiff~=0 nd=nd+1;  slopes(nd)=(y(j)-y(i))/xdiff;  end;
  end;  end;
%% DON`T COUNT unused values in slopes() before finding median
slopes=slopes(1:nd);   
beta_hat=median(slopes);
slopes=sort(slopes);
 
fprintf('\nThe nd=%d difference ratios (Y_j-Y_i)/(X_j-X_i)\n',nd);
fprintf('  range between %g (minimum) and %g (maximum)\n',...
  slopes(1), slopes(nd));
fprintf('The median is beta_hat=%6.4f, which is Theil`s estimate\n',beta_hat);
disp('  of the slope');
 
disp(' ');
disp('Given beta, mu=mu_hat is the median of the Walsh averages');
disp('  of Y_i - beta X_i.');
% Given beta, mu=mu_hat is the median of the Walsh averages
%   of Y(i)-beta_hat*X(i)
% We use the name resid(i) for Y_i - beta_hat*X_i, even though
%   they are not really residuals without the mu.
resid=zeros(1,nn);
for i=1:nn;  resid(i)=y(i)-beta_hat*x(i);  end;
wsums=zeros(1,nn*nn+3);  nw=0;
for i=1:nn;  for j=i:nn;
  nw=nw+1;  wsums(nw)=(resid(i)+resid(j))/2;  end;  end;
%% Again, REMOVE unused values before finding median
wsums=wsums(1:nw);
mu_hat=median(wsums);
fprintf('The median of nw=%d Walsh averages is %6.4f\n', nw,mu_hat);
fprintf('Thus Theil`s regression line in this case is\n');
fprintf('    Y = %6.4f + %6.3f\n', beta_hat,mu_hat);
 

% Find MS (Mean-Square) and Sum_Absolute_Value errors
%   for Theil regression
resid_theil = y - beta_hat*x - mu_hat;
err_theil_sabs = sum(abs(resid_theil))/nn;
err_theil_ms = sqrt(sum(resid_theil.*resid_theil)/nn);
 
disp(' ');
disp('Regression line errors:');
disp('  E1 is mean of absolute values of residuals');
disp('  E2 is root-mean-square of residuals');
 
fprintf('  Theil:          Y = %7.4f X + %8.3f   E1=%7.2f   E2=%7.2f\n', ...
   beta_hat, mu_hat, err_theil_sabs, err_theil_ms);
 
% Find the corresponding least-squares regression values
% beta_lsq, mu_lsq, resid_lsq computed earlier
err_lsq_sabs=sum(abs(resid_lsq))/nn;
err_lsq_ms=sqrt(sum(resid_lsq.*resid_lsq)/nn);
 
fprintf('  Least-Squares:  Y = %7.4f X + %8.3f   E1=%7.2f   E2=%7.2f\n', ...
   beta_lsq, mu_lsq, err_lsq_sabs, err_lsq_ms);
disp(' ');
disp('Rank Regression for a Multiple Regression');
disp('  Y_i = mu + Sum(j=1,p) X_{ij} beta_j + error_i');
disp('Specialized to p=1, so   Y_i = beta*X_i + mu');
disp('See Sections 9.6-9.7 in text');
 
% Are there any X- or Y-ties?
[midrx  xties] = getmidranks(x);
xg=0;
for i=1:nn;  
  if xties(i)>0 xg=i;  else break;  end;  end;
[midry  yties] = getmidranks(y);
yg=0;
for i=1:nn;  
  if yties(i)>0 yg=i;  else break;  end;  end;
fprintf('\nWithin-sample tie groups:  X: %d   Y: %d\n', xg, yg);
if xg==0 && yg==0  disp('NO TIES in Xs or Ys');  end;
 
%% Find slope and intercept of simple regression
%% (After we find the slope, the intercept will be the median
%%   of the Walsh averages of  Y_i - Sum(j=1,p) X_{ij} beta_j,
%%   so that finding the slope is the hard part.)
 
% Collect slopes and absolute-X-differences in an mmx2 matrix
%   for mm=nn*(nn-1)/2
mm=nn*(nn-1)/2;
ww=zeros(mm,2);  nw=0;
for i=1:nn;  
  for j=i+1:nn;
  xdiff=x(j)-x(i);
    if xdiff~=0  nw=nw+1;
    ww(nw,1)=(y(j)-y(i))/xdiff;
    ww(nw,2)=abs(xdiff);  
    end;
  end; 
end;
 
ww = ww(1:nw,:);    %% Trim off any unused rows
% Sort ww by slope then X-difference
ww = sortrows(ww, [1 2]);
 
disp(' ');
disp('Finding the minimum value of D(beta):');
fprintf('  nw=%d nodes ranging from  %g  to  %g\n', nw,ww(1,1),ww(nw,1)); 
 
% Compute Qsum = Sum(i=1,nn) (Rank(X_i) - (nn+1)/2)*X_i
%   =  Sum(i=1,nn) (Rank(X_i) - (nn+1)/2)*(X_i - Xbar)
% Note that midranks of X_i are already in the array midrx
midrxc = midrx - (nn+1)/2;
qsum=0;
for i=1:nn;  qsum=qsum+midrxc(i)*x(i);  end;
fprintf('  Slope for beta<%g: %g   for beta>%g: %g\n',...
  ww(1,1),-qsum, ww(nw,1),qsum);
 
disp('Finding the lowest point on the curve Y = D(beta):');
% lslope is initially the slope just before ww(1)
% The beta value at ww(i) is ww(i,1)
lslope=-qsum;
for i=1:nw;
  rslope=lslope+ww(i,2);  % Add |X_{j_2} - X_{j_1}|
  %% Define beta and end loop if the slope changes sign
  %%   or has a flat spot
  if abs(lslope)<1e-12
     beta=(ww(i,1)+ww(i+1,1))/2;  break;
  elseif lslope<0 && rslope>0
     beta=ww(i,1);  break;
  end;
  %% The options above set beta and exit the loop
  %% Otherwise update lslope and go to next value
  lslope=rslope;
  end;
fprintf('  At minimum value, lslope=%g  rslope=%g     Qsum=%g\n', ...
  lslope, rslope, qsum);
 
%% Also find D(beta)
resid=zeros(nn,1);
for i=1:nn;  resid(i)=y(i)-beta*x(i);  end;
[midr tiegr] = getmidranks(resid);
midrc = midr - (nn+1)/2;
dbeta = sum(midrc.*resid);
fprintf('  Minimum attained at  beta=%g   D(beta)=%g\n', beta, dbeta);
 
%% Set mu = median of Walsh averages of Y-beta*X values
wav=zeros(nn*nn,1);  nw=0;
for i=1:nn;  for j=i:nn;
  nw=nw+1;  wav(nw) = (resid(i)+resid(j))/2;  end;  end;
wav=wav(1:nw);    %% Trim off unused values
mu=median(wav);
fprintf ('  Intercept:  mu=%g  (median of Y_i-beta X_i Walsh averages)\n', mu);
fprintf('The median of nw=%d Walsh averages is %6.4f\n', nw,mu);
%% Find average-absolute and RMS errors
resid=y-beta*x-mu;
err_avabs = sum(abs(resid))/nn;
err_rms = sqrt(sum(resid.*resid)/nn);
 
disp(' ');
disp('Regression line and errors:');
disp('  E1 is mean of absolute values of residuals');
disp('  E2 is root-mean-square of residuals');
fprintf('  Rank-Regression:  Y = %7.4f X + %8.3f   E1=%7.2f   E2=%7.2f\n', ...
   beta, mu, err_avabs, err_rms);
  

 

