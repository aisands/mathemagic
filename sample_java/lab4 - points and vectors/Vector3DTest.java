package lab4;

import static org.junit.Assert.*;

import org.junit.Test;

public class Vector3DTest {

	@Test
	public void init() {
		Vector3D v = new Vector3D(5, -3, 6);
		assertEquals(5.0,  v.getVectorX(), .01);
		assertEquals(-3.0, v.getVectorY(), .01);
		assertEquals(6.0, v.getVectorZ(), 0.01);
	}

	@Test
	public void arith() {
		Vector3D v = new Vector3D(5, -3, 6);
		Vector3D vPlusV = v.plus(v);
		//
		// Make sure the old vector did not change
		//
		compareVectors(new Vector3D(5, -3, 6), v);
		//
		// Make sure the new vector is right
		//
		compareVectors(new Vector3D(10, -6, 12), vPlusV);
		compareDoubles(10, vPlusV.getVectorX());
		compareDoubles(-6, vPlusV.getVectorY());
		compareDoubles(12, vPlusV.getVectorZ());
		
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
	public void compareVectors(Vector3D one, Vector3D two) {
		compareDoubles(one.getVectorX(), two.getVectorX());
		compareDoubles(one.getVectorY(), two.getVectorY());
		compareDoubles(one.getVectorZ(), two.getVectorZ());
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
		Vector3D v = new Vector3D(5, -3, 6);
		Vector3D bigger = v.scale(1.5);
		Vector3D smaller = v.scale(0.75);
		compareDoubles( 7.5,   gx(bigger));
		compareDoubles(-4.5,   gy(bigger));
		compareDoubles(9, 	   gz(bigger));
		compareDoubles( 3.75,  gx(smaller));
		compareDoubles( 2.25,  gy(smaller.deflectY()));
		compareDoubles(-2.25,  gy(smaller.deflectX()));
		compareDoubles(4.5,    gz(smaller));
	}

	/**
	 * Why did I write this method?
	 * @param v a vector
	 * @return v's x component
	 */
	public double gx(Vector3D v) {
		return v.getVectorX();
	}

	/**
	 * Why did I write this method?
	 * @param v a vector
	 * @return v's y component
	 */
	public double gy(Vector3D v) {
		return v.getVectorY();
	}
	
	public double gz(Vector3D v){
		return v.getVectorZ();
	}
	
	@Test
	public void rescale() {
		Vector3D v = new Vector3D(2, 4, Math.sqrt(5));
		compareDoubles(5, v.magnitude());
		compareDoubles(4.0, gx(v.rescale(10)));
		compareDoubles(8.0, gy(v.rescale(10)));
	}



}