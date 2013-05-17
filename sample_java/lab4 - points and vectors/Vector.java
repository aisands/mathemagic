package lab4;

/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 9/28/10
 * Vector.java
 * CSE 131 Lab 4
 * Purpose of class: represents set magnitudes and directions in the R^2 plane
 */

public class Vector {
	private final double deltaX; 
	private final double deltaY;

	//creates a vector with the given x and y components
	public Vector(double deltaX, double deltaY) {
		super();
		this.deltaX = deltaX;
		this.deltaY = deltaY;
	}

	//returns the x component of a given vector
	public double getDeltaX() {
		return deltaX;
	}

	//returns the y component of a given vector
	public double getDeltaY(){
		return deltaY;
	}

	//calculates the length of a vector
	public double magnitude(){
		return Math.sqrt(Math.pow(deltaX,2)+Math.pow(deltaY,2));
	}

	//reflects the vector over the y-axis
	public Vector deflectX(){
		return new Vector(-1*this.deltaX, this.deltaY);
	}

	//reflects the vector over the x-axis
	public Vector deflectY(){
		return new Vector(this.deltaX,-1*this.deltaY);
	}

	/** Adds the components of two vectors
	 * @param vector: the vector to be added to the vector on which the method is executed
	 * @return: the new vector 
	 */
	public Vector plus(Vector vector){
		double dxAdd= vector.deltaX;
		double dyAdd= vector.deltaY;
		return new Vector(this.deltaX+ dxAdd, this.deltaY+ dyAdd);
	}

	/**Subtracts the components of two vectors
	 * @param vector: the vector to be subtracted from the vector on which the method is executed
	 * @return: the new vector
	 */
	public Vector minus(Vector vector){
		double minusX =(vector.deflectX()).getDeltaX();
		double minusY =(vector.deflectY()).getDeltaY();
		return this.plus(new Vector(minusX, minusY));
	}	

	/**Creates a new vector in the same direction but with multiplied magnitude
	 * @param factor: the number multiplied by the x and y components to create the new scaled vector
	 * @return: the scaled vector
	 */
	public Vector scale(double factor) {
		double dxScaled = this.getDeltaX()*factor;
		double dyScaled = this.getDeltaY()*factor;
		return new Vector (dxScaled, dyScaled);

	}
	/**Creates a new vector in the same direction but with a specified magnitude
	 * @param magnitude: the specified length of the new vector
	 * @return: the rescaled vector
	 */

	public Vector rescale(double magnitude){
		double vectorMagnitude = this.magnitude();
		double factorRescale = magnitude/vectorMagnitude;
		if (vectorMagnitude == 0){
			return new Vector (magnitude, 0);
		}
		else {
			return this.scale(factorRescale);
		}

	}

	public String toString() {	
		return "[" + deltaX + " " + deltaY + "]";
	}
}