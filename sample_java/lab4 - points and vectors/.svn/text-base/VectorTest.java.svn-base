package lab4;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class VectorTest {
	@Test
	public void arith() {
		Vector v = new Vector(2, 3);
		Vector VplusV = v.plus(v);
		Vector VminusV = v.minus(v);

		compareVectors(new Vector(4, 6), VplusV);
		compareVectors(new Vector(0, 0), VminusV);
	}

	public void compareVectors(Vector one, Vector two) {
		compareDoubles(one.getDeltaX(), two.getDeltaX());
		compareDoubles(one.getDeltaY(), two.getDeltaY());
	}

	public void compareDoubles(double one, double other) {
		assertEquals(one, other, 0.01);
	}
}