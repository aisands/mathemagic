package lab4;
/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 9/28/10
 * Point.java
 * CSE 131 Lab 4
 * Purpose of class: represents coordinates in the R^2 plane, defined by the points (x,y)
 */

public class Point {
	private double x;
	private double y;
	
	//specifies a point with coordinates (x, y)
	public Point(double x, double y){
		super();
		this.x = x; 
		this.y = y;
	}
	
	public double getX(){
		return x;
	}
	
	public double getY(){
		return y;
	}
	
	/**Adds a vector to a point
	 * @param vector: vector whose x and y components are added to the point (x, y)
	 * @return: new point which differs from the old point by the x and y components of the vector
	 */
	
	public Point plus(Vector vector){
		double dx = vector.getDeltaX();
		double dy = vector.getDeltaY();
		return new Point(x+dx, y+dy);
	}
	/**Subtracts two points
	 * REQUIRES: both points in the same plane, in this case R^2
	 * @param point: point whose x and y components are subtracted from the old point
	 * @return: vector whose components are the differences between the points' x and y components
	 */
	
	public Vector minus(Point point){
		double xSubtracted = this.getX()-point.getX();
		double ySubtracted = this.getY()-point.getY();
		return new Vector (xSubtracted, ySubtracted);
	}
	
	/**Calculates the distance between two points
	 * @param p: endpoint used to calculate the distance from a starting point
	 * @return: distance between start and end points
	 */
	
	public double distance(Point p){
		return (this.minus(p)).magnitude(); //creates a vector between the two points and measures its magnitude
	}
		
	public String toString(){
		return "(" +x + ", " +y +")";
	}
}
