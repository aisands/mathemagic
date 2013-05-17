package lab0;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.geom.GeneralPath;
import javax.swing.*;
import nip.Image;

/**
 * A robot image that turns and moves under program control, typically using the
 * methods turnLeft(degrees), turnRight(degrees), and forward(pixels).
 * @author Kenneth J. Goldman
 * Created: July 24, 2007
 * Modified: July 28, 2009
 */

public class Robot extends Image implements ActionListener {
	private static final long serialVersionUID = 1L; // The version number for this class.
	String imageFile; // The name of the file containing the image of the robot.
	Timer timer = new Timer(50, this); // A timer that "ticks" 20 times per second (every 50 milliseconds) for robot animation.
	static final int PIXELS_PER_STEP = 4; // The number of pixels to move forward at each time step (constant).
	Point destination; // The current destination of the robot, or null if the robot is not moving.
	double px, py;  // The current position of the robot, in pixels.
	double dx, dy;  // The change in x and y per move.
	static int degreesPerMove = 3;  // The number of degrees to turn at each time step (variable, may be negative).
	double heading = 0; // in degrees
	double newheading = 0;
	GeneralPath path = new GeneralPath(); // The "trail" that the robot leaves behind itself.


    /**
     * Creates a robot with the given image, centered at the given location, and with the given width and height.
     * @param imageFile the file containing the image of the robot (ideally an animated gif)
     * @param x the x-coordinate for the center of the robot
     * @param y the y-coordinate for the center of the robot 
     * @param width the width of the robot (in pixels)
     * @param height the height of the robot (in pixels)
     */	
	public Robot(String imageFile, int x, int y, int width, int height) {
		super(width, height);
		setOpaque(false);
		super.setCenter(x, y);
		resetPath();
		path.moveTo(getCenterX(), getCenterY());
		setImageFile(imageFile);	
		timer.start();  // Start the timer to repain the animated gif and to handle robot motion.
	}
	
	/**
	 * Turns the robot to the right by the given number of degrees.
	 * @param degrees the amount by which the robot should turn.
	 */
	public synchronized void turnRight(int degrees) {
		if (Math.abs(degrees) > 0) {
			degreesPerMove = degrees/Math.abs(degrees) * Math.abs(degreesPerMove);
			newheading = (heading + degrees + 360) % 360;
			// Now, wait until the robot is finished turning.
			while (heading != newheading)
				try {
					wait();
				} catch (InterruptedException e) {
				}
		}	
	}

	/**
	 * Turns the robot to the left by the given number of degrees.
	 * @param degrees the amount by which the robot should turn.
	 */
	public void turnLeft(int degrees) {
		turnRight(-degrees);
	}
	
	/**
	 * Moves the robot forward the given distance.
	 * @param distance the number of pixels by which the robot should move forward.
	 */
	public void forward(int distance) {
		double radians = ((heading+270)%360) / 180 * Math.PI;
		double sin = Math.sin(radians);
	    double cos = Math.cos(radians);
	    if (sin == 0) {
	    	if (cos > 0)
	    		glideTo(getCenterX() + distance, getCenterY());
	    	else
	    		glideTo(getCenterX() - distance, getCenterY());
	    } else if (cos == 0) {
	    	if (sin > 0)
	    		glideTo(getCenterX(), getCenterY() + distance);
	    	else
	    		glideTo(getCenterX(), getCenterY() - distance);
	    } else
	    	glideTo(getCenterX() + (int) (cos*distance), getCenterY() + (int) (sin*distance));
	}
	
	/**
	 * Centers the robot at given coordinates.  This is an instantaneous move, without
	 * any animation.  This change in position does not leave a trail behind the robot.
	 * For animated motion, use either the "forward" or "glideTo" method.
	 */
	@Override
	public void setCenter(int x, int y) {
		super.setCenter(x,y);
		path.moveTo(x,y);
	}

	/**
	 * Centers the robot instantly at given coordinates, leaving a trail behind the robot,
	 * but without performing any animation.
	 * For animated motion, use either the "forward" or "glideTo" method.
	 */
    public void moveTo(int x, int y) {
    	super.setCenter(x,y);
    	path.lineTo(x, y);
    	repaint();
    }
    
    /**
     * Smoothly moves the robot to the given coordinates, without regard to the
     * robot's current orientation. 
     * @param x the x-coordinate of the destination
     * @param y the y-coordinate of the destination
     */
    public synchronized void glideTo(double x, double y) {
    	//First, set up the amount of motion for each "tick" of the timer.
    	destination = new Point((int) x,(int) y);
    	px = getCenterX();
    	py = getCenterY();
		dx = destination.x - px;
		dy = destination.y - py;
		double distance = Math.sqrt(dx*dx + dy*dy);
		double steps = distance / PIXELS_PER_STEP;
		dx = dx / steps;
		dy = dy / steps;
		// Now, wait for the robot to arrive at its destination.
    	while (destination != null) {
    		try {
				wait();
			} catch (InterruptedException e) {}
		}
    }
    
    /**
     * Clears away the "trail" that has been drawn behind the robot.
     */
    public void resetPath() {
    	path.reset();
    	path.moveTo(getCenterX(), getCenterY());
    	if (getParent() != null)
    		getParent().repaint();
    }

	/**
	 * Gets the name of the image file.
	 * @return the imageFile
	 */
	public String getImageFile() {
		return imageFile;
	}

	/**
	 * Sets the name of the image file.
	 * @param imageFile the imageFile to set
	 */
	public void setImageFile(String imageFile) {
		this.imageFile = imageFile;
	}
	
	
	/**
	 * The paint method not only paints the image, but also paints the "trail" that
	 * the robot leaves behind it.
	 */
	@Override
	public void paint(Graphics g) {
		loadImage(imageFile);
		super.paint(g);
		if (getParent() != null) {
			((Graphics2D) getParent().getGraphics()).draw(path);
		}
	}

	/**
	 * This method is called at each "tick" of the timer.  If the robot is moving or turning,
	 * this method performs one step of the move.  It also repaints the image to show the
	 * next frame of the animation.
	 */
	public synchronized void actionPerformed(ActionEvent arg0) {
		repaint();
		if (destination != null) {
			double distx = destination.x - getCenterX();
			double disty = destination.y - getCenterY();
			double dist = (int) Math.sqrt(distx*distx + disty*disty);
			if (dist > PIXELS_PER_STEP) {
				px = px + dx;
				py = py + dy;
				moveTo((int) px, (int) py);
				repaint();
			} else {
				moveTo(destination.x, destination.y);
				repaint();
				destination = null;
			}
		} else if (newheading != heading) {
			if (Math.abs(newheading - ((heading + degreesPerMove) + 360)%360) <= Math.abs(degreesPerMove))
				heading = newheading;
			else
				heading = (heading + degreesPerMove + 360) % 360;
			this.setRotation(heading);
			repaint();
		} else {
			notify();
		}
	}

}
