package lab4;
import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Official CSE131 Lab 4 Vector JUnit test.  
 *   Demo this to get credit DO NOT CHANGE THIS FILE!!! 
 *       (we are watching you) 
 * @author cytron
 *
 */
public class DemoVectorTest {
	@Test
	public void init() {
		Vector v = new Vector(5, -3);
		assertEquals(5.0,  v.getDeltaX(), .01);
		assertEquals(-3.0, v.getDeltaY(), .01);
	}

	@Test
	public void arith() {
		Vector v = new Vector(5, -3);
		Vector vPlusV = v.plus(v);
		//
		// Make sure the old vector did not change
		//
		compareVectors(new Vector(5, -3), v);
		//
		// Make sure the new vector is right
		//
		compareVectors(new Vector(10, -6), vPlusV);
		compareDoubles(10, vPlusV.getDeltaX());
		compareDoubles(-6, vPlusV.getDeltaY());
		//
		// Test toString visually
		System.out.println("TA check v:      " + v);
		System.out.println("TA check vplusV: " + vPlusV);
	}

	/**
	 * Compare two Vectors JUnit-style, failing if they do not
	 * agree on their x and y deltas.
	 * @param one
	 * @param two
	 */
	public void compareVectors(Vector one, Vector two) {
		compareDoubles(one.getDeltaX(), two.getDeltaX());
		compareDoubles(one.getDeltaY(), two.getDeltaY());
	}


	/**
	 * Why did I write this method?
	 * @param one    one of two doubles to compare
	 * @param other  other of two doubles to compare
	 */
	public void compareDoubles(double one, double other) {
		assertEquals(one, other, 0.01);
	}



	@Test
	public void scale() {
		Vector v = new Vector(5, -3);
		Vector bigger = v.scale(1.5);
		Vector smaller = v.scale(0.75);
		compareDoubles( 7.5,   gx(bigger));
		compareDoubles(-4.5,   gy(bigger));
		compareDoubles( 3.75,  gx(smaller));
		compareDoubles( 2.25,  gy(smaller.deflectY()));
		compareDoubles(-2.25,  gy(smaller.deflectX()));
	}

	/**
	 * Why did I write this method?
	 * @param v a vector
	 * @return v's x component
	 */
	public double gx(Vector v) {
		return v.getDeltaX();
	}

	/**
	 * Why did I write this method?
	 * @param v a vector
	 * @return v's y component
	 */
	public double gy(Vector v) {
		return v.getDeltaY();
	}
	
	@Test
	public void rescale() {
		Vector v = new Vector(3, 4);
		compareDoubles(5.0, v.magnitude());
		compareDoubles(6.0, gx(v.rescale(10)));
		compareDoubles(8.0, gy(v.rescale(10)));
	}

	@Test
	public void specialCases() {
		Vector v = new Vector(0, 0);
		Vector r = v.rescale(5);
		compareDoubles(0, v.magnitude());
		compareDoubles(5, r.magnitude());
		compareDoubles(5, gx(r));
		compareDoubles(0, gy(r));
	}

}
