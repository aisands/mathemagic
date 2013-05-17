package lab5;
/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 10/5/10
 * Eyeball.java
 * CSE 131 Lab 5
 * Purpose of class: to create a roving eyeball
 */

import java.awt.Color;

import lab4.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;

import javax.swing.Timer;

import nip.*;

public class Eyeball implements MouseMotionListener, ActionListener {
	public static final int PUPIL_SIZE = 10;
	public static final int PUPIL_DISTANCE = 14;
	public static final int OUTLINE_SIZE = 40;
	public static final int PIXELS_PER_TICK = 20;
	private int x, y;
	private Ellipse outline, pupil;
	private Timer timer = new Timer(50, this);
	

	/**
	 * Creates the outline and pupil of each eyeball
	 * @param panel where the eyeball will be created
	 * @param x the x coordinate of the eyeball's center
	 * @param y the y coordinate of the eyeball's center
	 */
	public Eyeball(GraphicsPanel panel, int x, int y) {
		this.x = x;
		this.y = y;
		// Creates an ellipse (pupil) at (x,y) with a radius of PUPIL_SIZE
		pupil = new Ellipse(x, y, PUPIL_SIZE ,PUPIL_SIZE);
		pupil.setFilled(true);
		pupil.setFillColor(Color.BLACK);
		panel.add(pupil); 


		//Creates an ellipse (outline) at (x,y) with a radius OUTLINE_SIZE
		outline = new Ellipse (x, y, OUTLINE_SIZE, OUTLINE_SIZE);
		outline.setLineColor(Color.BLACK);
		outline.setFilled(true);
		outline.setFillColor(Color.WHITE);
		panel.add(outline);

		this.moveTo(x, y);

		//Adds the eyeball as a MouseMotionListener for mouse events on the panel
		panel.addMouseMotionListener(this);
		timer.start();
	}

	public double getX(){
		return x;
	}

	public double getY(){
		return y;
	}
	/**
	 * Moves the eyeball to a new location (x,y)	
	 * @param x the x coordinate of the new center
	 * @param y the y coordinate of the new center
	 */
	public void moveTo(int x, int y){
		outline.setCenter(x, y);
		pupil.setCenter(x, y);
	}


	/** 
	 * Makes the eyeball look toward a certain point p while keeping the pupil in the outline
	 * @param newX the x coordinate of p
	 * @param newY the y coordinate of p
	 */
	public void lookAt(int newX, int newY){

		int outlineX =outline.getCenterX();
		int outlineY = outline.getCenterY();

		Point center = new Point(outlineX, outlineY);
		Point mouse = new Point (newX, newY);

		Vector difference = mouse.minus(center); //vector representing distance between center and the mouse's location
		if (difference.magnitude() > PUPIL_DISTANCE){ //mouse outside the eyeball
			Vector newDifference = difference.rescale(PUPIL_DISTANCE);//re-scales the distance between the center and the mouse to stay inside the outline
			Point desiredPupilCenter = center.plus(newDifference);//centers the pupil at this distance
			double pupilCenterX = desiredPupilCenter.getX();
			double pupilCenterY = desiredPupilCenter.getY();
			pupil.setCenter((int)pupilCenterX, (int)pupilCenterY);
		}

		else {
			pupil.setCenter((int)newX, (int)newY); //mouse inside the eyeball
		}
	}

	/**
	 * Reacts to the mouse moving
	 */
	public void mouseMoved(MouseEvent e) {
		lookAt(e.getX(), e.getY());

	}

	public String toString(){
		return "The eye is centered at (" + x + " ," + y + "). The pupil has a radius of "
		+ PUPIL_SIZE + "with a maximum distance of "+ PUPIL_DISTANCE + "between the " +
		"center of the pupil and the center of the eyeball";
	}

	// You will modify the following method only if you
	// complete the animation Extension of this project.
	public void actionPerformed(ActionEvent arg0) {
//		this.lookAt(newX, newY);
	}

	//  Do nothing here
	public void mouseDragged(MouseEvent e) {

	}

}
