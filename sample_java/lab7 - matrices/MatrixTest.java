package lab7;

import static org.junit.Assert.*;

import org.junit.Test;


/**
 * This JUnit test class is designed to help you finish Lab 7.
 * I (RKC) have tested it, but it may have errors.  Any errors found will
 * be posted on the course web page for this lab.
 * 
 * I also may post other tests, and if you develop JUnit tests for this
 * lab, please send them to me, and I will post those as well, crediting you
 * for the work.
 * 
 * Your Matrix code is required to operate correctly, whether or not this
 *   test file has errors.  So please pay attention to course announcements
 *   in case errors are found in this test.
 * @author cytron
 *
 */
public class MatrixTest {

	double[][] values = new double[][] { 
			{ 1, 2, 3},
			{ 4, 5, 6}
	};

	Matrix m1 = new Matrix(
			values
	);

	Matrix m1too = new Matrix(
			new double[][] { 
					{ 1, 2, 3},
					{ 4, 5, 6}
			}
	);


	Matrix m1Plusm1 = new Matrix(
			new double[][] { 
					{ 2, 4, 6},
					{ 8, 10, 12}
			}
	);

	Matrix prod = new Matrix(
			new double[][] {
					{14, 32},
					{32, 77}
			}
	);

	Matrix addedRow = new Matrix (
			new double[][] {
					{1, 2, 3},
					{5, 7, 9}

			}
	);


	@Test
	public void init() {
		assertEquals(m1, m1);
		assertEquals(m1too, m1too);
		assertEquals("Implement arraysAreEqual", m1, m1too);
		assertEquals(m1too, m1);

		double save = values[1][1];
		values[1][1] = 0; // Matrix should have copied this array, so this assignment should have no effect

		assertEquals("Matrix constructor failed to copy the array", m1, m1too);

		assertFalse(m1.equals(m1Plusm1));
		assertFalse(m1Plusm1.equals(m1too));
		values[1][1] = save;
	}

	@Test
	public void testarith() {
		Matrix sum = m1.plus(m1too);
		assertEquals(sum, m1Plusm1);   // sum = m1 + m1too;
		assertEquals(m1, m1too);       // m1 and m1too should be unchanged
		assertEquals(prod, m1.times(m1.transpose()));
	}

	@Test
	public void testScale() {
		Matrix m1copy = new Matrix(values);
		m1copy.scaleRow(0, 2);
		m1copy.scaleRow(1, 2);
		assertEquals(m1copy, m1Plusm1);
	}

	@Test
	public void testAddRow() {
		Matrix m1copy = new Matrix(values);
		m1copy.addRows(0, 1);
		assertEquals(m1copy, addedRow);
	}

	/*
	 * The following tries to add a 2x3 matrix to its transpose,
	 * which should throw an error.  The test case expects the error.
	 */
	@Test (expected=IllegalArgumentException.class)
	public void badPlus() {
		m1.plus(m1.transpose());
	}

	/**
	 * The following multiplies a 2x3 matrix by itself, which should
	 * throw an error.  Remember:  the number of columns of the first matrix
	 * should equal the number of rows in the second matrix.
	 */
	@Test (expected=IllegalArgumentException.class)
	public void badTimes() {
		m1.times(m1);
	}

	/**
	 * Trying to scale a row that is out-of-bounds, which should throw
	 * an error.
	 */
	@Test (expected=IllegalArgumentException.class)
	public void badScale() {
		m1.scaleRow(values.length, 1.0);
	}

	@Test
	public void transpose() {
		Matrix trans = m1.transpose();
		assertFalse(m1.equals(trans));
		assertEquals(m1, m1.transpose().transpose());
	}

	@Test
	public void print() {
		System.out.println("m1: " + m1);
		System.out.println("m1 transpose " + m1.transpose());
		System.out.println("m1 x m1.transpose() " + m1.times(m1.transpose()));
	}

}
