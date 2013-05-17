package lab4;

public class Vector3D {
	private double vectorX, vectorY, vectorZ;

	public Vector3D(double vectorX, double vectorY, double vectorZ) {
		super();
		this.vectorX = vectorX;
		this.vectorY = vectorY;
		this.vectorZ = vectorZ;
	}

	public double getVectorX() {
		return vectorX;
	}

	public double getVectorY() {
		return vectorY;
	}

	public double getVectorZ() {
		return vectorZ;
	}

	public double magnitude(){
		return Math.sqrt(Math.pow(vectorX, 2)+ Math.pow(vectorY, 2)+ Math.pow(vectorZ, 2));
	}

	public Vector3D deflectX(){
		return new Vector3D(-1*this.vectorX, this.vectorY, this.vectorZ);
	}

	public Vector3D deflectY(){
		return new Vector3D(this.vectorX,-1*this.vectorY, this.vectorZ);
	}

	public Vector3D deflectZ(){
		return new Vector3D(this.vectorX, this.vectorY, 1*this.vectorZ);
	}

	/** Adds the components of two vectors
	 * @param vector: the vector to be added to the vector on which the method is executed
	 * @return: the new vector 
	 */
	public Vector3D plus(Vector3D victor){
		double dxAdd= victor.getVectorX()+this.vectorX;
		double dyAdd= victor.getVectorY()+this.vectorY;
		double dzAdd= victor.getVectorZ()+this.vectorZ;
		return new Vector3D(dxAdd, dyAdd, dzAdd);
	}

	/**Subtracts the components of two vectors
	 * @param vector: the vector to be subtracted from the vector on which the method is executed
	 * @return: the new vector
	 */
	public Vector3D minus(Vector3D vector){
		double minusX =(vector.deflectX()).getVectorX();
		double minusY =(vector.deflectY()).getVectorY();
		double minusZ = (vector.deflectZ()).getVectorZ();
		return this.plus(new Vector3D(minusX, minusY, minusZ));
	}	

	/**Creates a new vector in the same direction but with multiplied magnitude
	 * @param factor: the number multiplied by the x and y components to create the new scaled vector
	 * @return: the scaled vector
	 */
	public Vector3D scale(double factor) {
		double dxScaled = this.getVectorX()*factor;
		double dyScaled = this.getVectorY()*factor;
		double dzScaled = this.getVectorZ()*factor;
		return new Vector3D(dxScaled, dyScaled, dzScaled);
	}

	/**Creates a new vector in the same direction but with a specified magnitude
	 * @param magnitude: the specified length of the new vector
	 * @return: the rescaled vector
	 */

	public Vector3D rescale(double magnitude){
		double vectorMagnitude = this.magnitude();

		if (vectorMagnitude == 0){
			return new Vector3D (0, 0, 0);
		}

		else if (this.getVectorX()== 0 && this.getVectorY()==0 || this.getVectorZ()==0) {
			return new Vector3D(magnitude, 0 ,0);

		}
		else {
			double factorRescale = magnitude/vectorMagnitude;
			return this.scale(factorRescale);
		}

	}
	@Override
	public String toString() {
		return "Vector3D [vectorX=" + vectorX + ", vectorY=" + vectorY
		+ ", vectorZ=" + vectorZ + "]";

	}
}
