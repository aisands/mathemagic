package lab7;

/**
 * 
 * @author Adrienne Sands
 * @version 1.0
 * CSE131 Lab 7
 * Date: 12/13/10
 */
public class Matrix {

	private double[][] values;

	/**
	 * The Matrix is based on the supplied two-dimensional array of values.
	 * Be sure to make your own copy of the values, so that changes to the
	 *    array outside of this class do not affect your work.
	 * @param values
	 */
	public Matrix(double[][] in) {
		values = new double[in.length][in[0].length];
		for (int i=0; i< in.length; i++){ 			//iterates through each cell of the matrix
			for (int j=0; j< in[0].length; j++){	//copies each cell to the new matrix values
				values [i][j]= in[i][j];
			}
		}
	}

	/**
	 * You must complete this method, or the equals(Object) test will always
	 *   return false. 
	 * Arrays one and two are considered
	 * equal if and only if:
	 *   1) They have the same shape (number of rows and columns agree)
	 *   2) The contents of the two arrays are the same, element by element
	 * @param one
	 * @param two
	 * @return true iff the arrays have the same shape and contents
	 */
	private static boolean arraysAreEqual(double[][] one, double[][] two) {
		if (one.length!=two.length){ //first condition
			return false;
		}
		else  {
			for (int i=0; i< one.length; i++){ 			//second condition
				for (int j=0; j< one[0].length; j++){	//iterates through the list and compares each element of the two arrays
					if (one[i][j]!= two[i][j]){
						return false;
					}
				}
			}
			return true;
		}
	}

	/**
	 * This was generated initially by eclipse, but
	 *   eclipse does not know how to compare two-dimensional arrays.
	 *   We therefore call arraysAreEequal to do that job.
	 */
	public boolean equals(Object obj) {
		// If this and obj are the same object, they must be equal
		if (this == obj)
			return true;
		// If obj is null ("this" cannot be null), then they are not equal
		if (obj == null)
			return false;
		// If the two objects are not the same type, they are not equal
		if (getClass() != obj.getClass())
			return false;
		//
		// If we get here, we have two objects of the same type.
		// Calling your helper method to determine the arrays' equality.
		Matrix other = (Matrix) obj;
		return arraysAreEqual(this.values, other.values);
	}

	public Matrix plus(Matrix other) {
		if (sameSize(this.values, other.values)){
			double[][]sum = new double[values.length][values[0].length];
			for (int i=0; i<values.length; i++){
				for(int j=0; j<values[0].length; j++){
					sum[i][j]= this.values[i][j]+other.values[i][j];
				}
			}
			Matrix summed = new Matrix(sum);
			return summed;
		}
		else throw new IllegalArgumentException();
	}

	public static boolean sameSize(double[][]one, double[][]two){
		if (one.length!=two.length){
			return false;
		}
		else{
			for (int i=0; i<one.length; i++){
				if (one[i].length!=two[i].length){
					return false;
				}
			}
			return true;
		}
	}

	/**
	 * Returns a **new Matrix** that is the product of this and the other one.
	 * Does not change this Matrix at all.
	 * @param other
	 * @return
	 */
	public Matrix times(Matrix other) {
		double[][] product = new double[this.values.length][other.values.length];
		if (this.values.length== other.values[0].length){
			for (int i= 0; i<values.length; i++){
				for (int j= 0; j<other.values[0].length; j++){
					product[i][j]= dot(this.values[i], timesHelper(j, other));

				}
			}
			Matrix productMatrix = new Matrix(product);
			return productMatrix;
		}
		else throw new IllegalArgumentException();
	}

	private double[] timesHelper(int j, Matrix other){
		double[] timesHelper = new double[other.values.length];
		if(j < other.values[0].length){
			for (int k = 0; k < other.values.length; k++){
				timesHelper[k] = other.values[k][j];
			}
			return timesHelper;
		}
		else
			throw new IllegalArgumentException();
	}

private double dot(double[] one, double[] two){
	double dotProduct = 0;
	if (one.length==two.length){
		for (int i=0; i< one.length; i++){
			dotProduct = dotProduct + one[i] * two[i];
		}
		return dotProduct;
	}
	else throw new IllegalArgumentException();
}

/**
 * Returns a **new Matrix** that is the transpose of this one.
 * Does not change this Matrix at all.
 * @return
 */
public Matrix transpose() {
	double[][] transpose = new double [values[0].length][values.length];
	for(int i = 0; i < transpose.length; i++){
		for (int j = 0; j < transpose[0].length; j++){
			transpose[i][j] = values[j][i];
		}
	}
	Matrix transposed = new Matrix (transpose);
	return transposed;
}

/**
 * Modifies this Matrix by scaling row i by the supplied factor.
 * @param i the row to scale, where 0 is the top row
 * @param factor the amount by which to scale each element of row i
 */
public void scaleRow(int i, double factor) {
	if (i < values.length){
		for (int n = 0; n < values[i].length; n++){
			values[i][n] = values [i][n] * factor;
		}
	}
	else
		throw new IllegalArgumentException();

}

/**
 * Modifies this matrix by adding row i to row j.  Row 0 is the top row.
 * @param i
 * @param j
 */
public void addRows(int i, int j) {
	if (values[i].length == values[j].length){ //if the rows are of the same length
		for (int n = 0; n < values[i].length; n++){ //for every column in that row
			values[j][n] = values [i][n] + values[j][n];
		}
	}
	else
		throw new IllegalArgumentException();

}

/**
 * My Columbus Day gift to you.  This returns a String representation of
 * the Matrix.  The contents of each row is separated by a tab (\t)
 * so that columns (kind of) line up.  Each row is separated by a
 * newline (\n) so that the output looks like a matrix.  The output
 * of this method should <i>not</i> be used to compare matrices for
 * equality:  use the .equals(Object) method instead!
 */
public String toString() {
	String ans = "";
	for (int i=0; i < values.length; ++i) {
		ans = ans + "\n";
		// Loop below assumes all rows have the same number of columns
		for (int j=0; j < values[0].length; ++j) {
			ans = ans + values[i][j] + "\t";
		}
	}
	return ans;
}

}
