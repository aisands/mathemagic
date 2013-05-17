package lab2;
import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Name:Adrienne Sands
 * Lab Section: A
 * Date:9/14/10
 * Email:adrienne.i.sands@gmail.com
 * RecursionTest.java
 * CSE 131 Lab 2
 */

public class RecursionTest {

	    // Example:
		@Test
		public void testFactorial() {
			assertEquals(1, Recursion.factorial(0));
			assertEquals(24, Recursion.factorial(4));
		}
		
		@Test
		public void testAddition() {
		   assertEquals(1, 1+0);
		   assertEquals(131, 2*60 + 11);
		}
		
		@Test
		public void testsumDownBy2() {
			   assertEquals(16, Recursion.sumDownBy2(7));
			   assertEquals(20, Recursion.sumDownBy2(8));
		}
		@Test
		public void testharmonicSum() {
				assertEquals(2.45, Recursion.harmonicSum(6), 0.001);
				assertEquals(2.829, Recursion.harmonicSum(9), 0.001);
		}
		@Test
		public void testgeometricSum() {
				assertEquals(1.875, Recursion.geometricSum(3), 0.0001);
				assertEquals(1.96875, Recursion.geometricSum(5), 0.00001);
		}
	
		@Test
		public void testmult(){
				assertEquals(21, Recursion.mult(3,7));
				assertEquals(63, Recursion.mult(9,7));
				assertEquals(26, Recursion.mult(-13,-2));
				assertEquals(14, Recursion.mult(-2,-7));
				assertEquals(0, Recursion.mult(0,23));
				assertEquals(-16, Recursion.mult(8,-2));
				assertEquals(-27, Recursion.mult(-3, 9));
				
		}
		
		@Test
		public void testexpt(){
				assertEquals(9, Recursion.expt(3,2));
				assertEquals(1, Recursion.expt(5,0));
				assertEquals(32, Recursion.expt(2,5));
		}
		
		@Test
		public void testlcm(){
				//Let the last parameter be the greater positive integer;
				assertEquals(15, Recursion.lcm(3,5));
				assertEquals(24, Recursion.lcm(6,8));
				assertEquals(24, Recursion.lcm(8,6));
				
		}
		
		@Test
		public void testloanLength(){
				assertEquals(5, Recursion.loanLength(1000, 0.1, 250));
				assertEquals(1, Recursion.loanLength(1000, 0.1, 1050));
				assertEquals(0, Recursion.loanLength(0, 0.9, 50));
				
		}
}		

