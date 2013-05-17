package lab4;

import static org.junit.Assert.*;

import org.junit.Test;

public class Point3DTest {

	@Test
	public void testPoint3D() {
		Point3D p = new Point3D(4, -2, 6);
		Point3D q = new Point3D (-6, 13, 7);

		//To test Constructor
		comparePoints(new Point3D(4, -2, 6), p);
		comparePoints(q, new Point3D(-6, 13, 7));
	}

	@Test
	public void testGetXGetYGetZ() {
		Point3D p = new Point3D(5.0, 6.0, 7.0);

		//To test Accessors
		assertEquals(5.0, p.getX(), 0.01);
		assertEquals(6.0, p.getY(), 0.01);
		assertEquals(7.0, p.getZ(), 0.01);
	}


	@Test
	public void testPlus() {
		Point3D p = new Point3D (4.0, -2.0, 6.0);
		Vector3D q = new Vector3D(-6.0, 13.0, 8.0);
		Point3D pPlusQ = new Point3D (-2.0, 11.0, 14.0);

		//To test Vector addition
		comparePoints(pPlusQ, p.plus(q));
	}


	@Test
	public void testMinus() {
		Point3D p = new Point3D (5.0, 6.0, -3.0);
		Vector3D pMinusP = p.minus(p);
		Point3D q = new Point3D (-12.0, 10.0, -2.0);

		//To test subtraction of a point from itself
		compareVectors(pMinusP, new Vector3D(0,0,0));	
		//To test subtraction of point q from another point p
		compareVectors(p.minus(q), new Vector3D(17.0, -4.0, -1.0));
	}

	@Test
	public void testDistance() {
		Point3D p = new Point3D (3.0, 3.0, 4.0);
		Point3D q = new Point3D (-3.0, -5.0, 4.0);
		assertEquals(10.0, p.distance(q), 0.01);
		assertEquals(10.0, q.distance(p), 0.01);
		
		//For the TA to visually check the toString() method
		System.out.println("TA check p:      " + p);
		System.out.println("TA check q:      " + q);
	}

	public void comparePoints(Point3D one, Point3D two) {
		compareDoubles(one.getX(), two.getX());
		compareDoubles(one.getY(), two.getY());
		compareDoubles(one.getZ(), two.getZ());
	}

	public void compareVectors(Vector3D one, Vector3D two) {
		compareDoubles(one.getVectorX(), two.getVectorX());
		compareDoubles(one.getVectorY(), two.getVectorY());
		compareDoubles(one.getVectorZ(), two.getVectorZ());
	}

	public void compareDoubles(double one, double other) {
		assertEquals(one, other, 0.01);
	}
}

