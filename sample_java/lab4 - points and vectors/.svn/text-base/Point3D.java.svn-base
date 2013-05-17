package lab4;

public class Point3D {
private double x, y, z;
	
	Point3D(double x, double y, double z){
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	public double getZ() {
		return z;
	}
	
	/**Adds a vector to a point
	 * @param vector: vector whose x,y, and z components are added to the point (x, y, z)
	 * @return: new point which differs from the old point by the x, y, z components of the vector
	 */
	
	public Point3D plus(Vector3D vector){
		double dx = vector.getVectorX();
		double dy = vector.getVectorY();
		double dz = vector.getVectorZ();
		return new Point3D(x+dx, y+dy, z+dz);
	}
	/**Subtracts two points
	 * REQUIRES: both points in the same plane, in this case R^3
	 * @param point: point whose x and y components are subtracted from the old point
	 * @return: vector whose components are the differences between the points' x, y, z components
	 */
	
	public Vector3D minus(Point3D point){
		double xSubtracted = this.getX()-point.getX();
		double ySubtracted = this.getY()-point.getY();
		double zSubtracted = this.getZ()-point.getZ();
		return new Vector3D (xSubtracted, ySubtracted, zSubtracted);
	}
	
	/**Calculates the distance between two points
	 * @param p: endpoint used to calculate the distance from a starting point
	 * @return: distance between start and end points
	 */
	
	public double distance(Point3D p){
		return (this.minus(p)).magnitude(); //creates a vector between the two points and measures its magnitude
	}

	@Override
	public String toString() {
		return "(" +x + ", " + y + ", " +z + ")";
	}
	

}
