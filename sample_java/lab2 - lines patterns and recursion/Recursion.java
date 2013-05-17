package lab2;
/**
 * Name:Adrienne Sands
 * Lab Section: A
 * Date:9/14/10
 * Email:adrienne.i.sands@gmail.com
 * Recursion.java
 * CSE 131 Lab 2
 */

public class Recursion {
	
	// Example:
	static int factorial(int k) {
		if (k == 0)
			return 1;
		else
			return k * factorial(k-1);
	}
	
	static int sumDownBy2(int n) {
		if (n <= 0)
			return 0;
		else 
			return n + sumDownBy2(n-2);
	}	
	
	static double harmonicSum(double d) {
		if (d <= 0)
			return 0;
		else
			return (1/d) + harmonicSum (d-1);
	
	}
	static double geometricSum (double k){
		if (k < 0)
			return 0;
		else 
			return 1/Math.pow(2,k) + geometricSum (k-1);
	}
	static int mult(int j, int k){
		//case where either integer = 0
		if ((j==0)||(k==0))
			return 0;
		
		//case where k positive, j greater or negative
		if (((0<k)&&(k<j))||((j<0) && (0<k)))
			return j + mult(j, k-1);
		
		//case where j positive, k greater or negative
		if (((0<j)&&((j<k)))||((k<0) && (0<j)))
			return k + mult (j-1, k);
		
		//case where j<k<0 (both negative)
		if ((j<k)&&(k<0))
			return -j + mult (j, k+1);
		
		//case where k<j<0 (both negative)
		if ((k<j)&&(j<0))
			return -k + mult (j+1, k);
		else return 0;
				
	}
	
	static int expt(int n, int k) {
		if (k <= 0)
			return 1;
		else
			return n* expt(n, k-1);
	}
	
	static int lcm (int j, int k) {
		if (j>k) return lcmhelper (j,k,j);
		else return lcmhelper(j,k,k);
	}
	
	static int lcmhelper(int j, int k, int extra) {
		
		if ((j<=0)||((k<=0))) return 1;
		if (k>j) return lcmhelper(k, j, extra); 
		else if ((extra % k)==0)
				return extra;
		else return lcmhelper(j, k, extra + j);		
		
	}
	
	static int loanLength(double principal, double annualintrate, int payment){
		int startermonth = 0;
		return loanLengthHelper(principal, annualintrate, payment, startermonth);
				}			
	
	static int loanLengthHelper(double principal, double annualintrate, int payment, int month){
		double intrate= annualintrate/12;
		double remainder = (principal*(1+intrate)-payment);
		long rounded = Math.round(principal);
		if (principal== 0)
			return 0;
		System.out.println("Month " + month + ": " + rounded);
		if (remainder<=0) return month +1;
		else return loanLengthHelper(remainder, annualintrate, payment, month+1);
	}
	}

	
	
			
			
	
	
	
		
		

	
