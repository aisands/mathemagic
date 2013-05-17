package lab4;
import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 9/28/10
 * PointTest.java
 * CSE 131 Lab 4
 * Purpose: to test the methods created in Point.java
 */


public class PointTest {
	
	@Test
	public void testPoint() {
		Point p = new Point(4, -2);
		Point q = new Point (-6, 13);
		
		//To test Constructor
		comparePoints(new Point(4, -2), p);
		comparePoints(q, new Point(-6, 13));
	}

	@Test
	public void testGetXandGetY() {
		Point p = new Point(5.0, 6.0);
		
		//To test Accessors
		assertEquals(5.0, p.getX(), 0.01);
		assertEquals(6.0, p.getY(), 0.01);
	}

	@Test
	public void testVectorAdd() {
		Point p = new Point (4.0, -2.0);
		Vector q = new Vector (-6.0, 13.0);
		Point pPlusQ = new Point (-2.0, 11.0);
		
		//To test Vector addition
		comparePoints(pPlusQ, p.plus(q));
	}
	
	@Test
	public void testPointSubtract(){
		Point p = new Point (5.0, 6.0);
		Vector pMinusP = p.minus(p);
		Point q = new Point (-12.0, 10.0);
		
		//To test subtraction of a point from itself
		compareVectors(pMinusP, new Vector(0,0));	
		//To test subtraction of point q from another point p
		compareVectors(p.minus(q), new Vector(17.0, -4.0));
	}
	

	@Test
	public void testDistance() {
		Point p = new Point (3.0, 3.0);
		Point q = new Point (-3.0, -5.0);
		assertEquals(10.0, p.distance(q), 0.01);
		assertEquals(10.0, q.distance(p), 0.01);
		
		//For the TA to visually check the toString() method
		System.out.println("TA check p:      " + p);
		System.out.println("TA check q:      " + q);
	}

	public void comparePoints(Point one, Point two) {
		compareDoubles(one.getX(), two.getX());
		compareDoubles(one.getY(), two.getY());
	}
	
	public void compareVectors(Vector one, Vector two) {
		compareDoubles(one.getDeltaX(), two.getDeltaX());
		compareDoubles(one.getDeltaY(), two.getDeltaY());
	}

	public void compareDoubles(double one, double other) {
		assertEquals(one, other, 0.01);
	}

}
