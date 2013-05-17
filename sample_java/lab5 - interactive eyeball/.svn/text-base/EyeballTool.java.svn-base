package lab5;
/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 10/10/10
 * EyeballTool.java
 * CSE 131 Lab 5
 * Purpose of class: to make the eyeball from Eyeball.java respond to mouse actions
 */

import java.awt.event.MouseEvent;

import nip.*;
import lab4.*;

public class EyeballTool extends Tool {

	private Eyeball eyeball;
	private GraphicsPanel panel;

	/**
	 * creates and defines the panel
	 */
	public EyeballTool(GraphicsPanel panel) {
		this.panel = panel;

	}	

	/**
	 * reacts to pressing the mouse by creating a new eyeball
	 */
	public void mousePressed(MouseEvent me) {
		eyeball = new Eyeball (panel, me.getX(), me.getY());
	}

	/**
	 * reacts to dragging the mouse by moving the center of the eyeball
	 */
	public void mouseDragged(MouseEvent me){
		eyeball.moveTo(me.getX(), me.getY());

	}

	public String toString() {
		return "Eyeballs";
	}

	/**
	 * We won't be using the menu to do anything for this lab
	 */
	public void actionNameCalled(String name) {		
	}

	/**
	 * No menu items needed
	 */
	public String[] getEventNames() {
		return new String[0];
	}
}
