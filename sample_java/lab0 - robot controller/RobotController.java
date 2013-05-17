package lab0;
/**
 * Your name:Adrienne Sands
 * Lab Section: A
 * Date: 9/2/10
 * RobotController.java
 * CSE 131 Lab 0
 */

import java.awt.event.MouseEvent;

import nip.*;


/**
 * This program guides a robot through a maze otherwise known as the School of Engineering and Applied Science.
 */
public class RobotController extends Tool implements Runnable {
	Robot robot;  // A variable referring to the robot to be controlled.
	/**
	 * YOUR ASSIGNMENT:
	 * Modify the "run" method below to guide the robot from the lab (Sever 201/202) to your instructor's office (Bryan 515).
	 * The trail that the robot leaves behind it should only go through doorways, hallways, and stairways
	 *  (no fair crashing through walls until you've tried this for 20 minutes!).
	 * Remember that programs execute sequentially, so be sure to put your instructions in the order that you want them to be
	 * carried out.
	 * 
	 * In Java, when you call a method on on object, you first refer to the target (the object that should execute the method).
	 * This is followed by a dot (.), which is then followed by the name of the method and the parameter list.
	 * Finally, each statement ends with a semicolon.
	 * 
	 * in this case, the target object will be the robot.  You will call three different methods of the robot guide it:
	 *     forward - moves the robot forward by a given number of pixels
	 *     turnLeft - turns the robot left by the given number of degrees
	 *     turnRight - turns the robot right by the given number of degrees. 
	 * 
	 * The "run" method is the only method that you need to modify for this lab assignment.
	 * The first two statements have been provided for you.  The robot will need to turn and move about a dozen times.
	 * Tip: If you point the mouse cursor on the map in the running program, and let it
	 *   sit there for a second, popup-text will show you the (x,y) coordinates to
	 *   help you plan the robot's motion.  Note that the origin (x=0, y=0) is the upper left corner and y increases down the page.
	 */
	public void run() {	
		robot.forward(40);  // Tell the robot to move forward 40 pixels.
		robot.turnLeft(45);  // Tell the robot to turn left by 45 degrees.
		robot.forward(40);
		robot.turnRight(45);
		robot.forward(150); 
		robot.turnLeft(90);
		robot.forward(375);
		robot.turnRight(90);
		robot.forward(240);
		robot.turnRight(90);
		robot.forward(6);
		
		
		// Add your program statements here to guide the robot.  You do not need to put a comment by each statement.
	} 
	
	//
	// You are not expected to understand what is below here!
	// The code below sets up the robot and gets things underway.
	// For now, please accept that as given and you will understand more
	//   about this by the end of the semester.
	//
	
	// First create the robot, then add it to the display, and finally start your "run"method.
	public void guideRobot(GraphicsPanel panel) {
		robot = new Robot("robot.gif", 514, 565, 40, 40);    // Create a 40x40 robot at pixel position (x=514, y=565).
		panel.add(robot);		// Add the robot to the graphics panel.
		new Thread(this).start();  // Starts the "run" method.
	}
	
	// Whenever the mouse moves, display the (x,y) coordinates for reference as popup text.
	public void mouseMoved(GraphicsPanel p, int x, int y) {
		p.setToolTipText("("+ x + "," + y + ")");
	}
	
	// The name of this tool is "RobotController."
	public String toString() {
		return "RobotController";
	}
	
	public String[] getEventNames() {
		String[] s = {"robot"};
		return s;
	}
	
	public void actionNameCalled(String name) {
		if (name == "robot") tool.guideRobot(nip.getTargetPanel());
		else System.out.println("no match!");
	}
	
	GraphicsPanel panel;
	/**
	 * When a RobotController is instantiated, we need access
	 *   to the panel so we can display mouse coordinates.
	 * @param panel -- the panel you see when running this program
	 */
	public RobotController(GraphicsPanel panel) {
		this.panel = panel;
	}

	public void mousePressed(MouseEvent arg) {
		mouseMoved(arg);
	}
	
	public void mouseReleased(MouseEvent arg) {
		mouseMoved(arg);
	}
	public void mouseMoved(MouseEvent arg) {
		mouseMoved(panel, arg.getX(), arg.getY());
	}

	private static RobotController tool;
	private static NIP nip;
	//A Java program always starts at the "main" method.
	public static void main(String[] args) {  // The parameters to the main method are for command-line arguments (ignore this).
		nip = new NIP(700,700, 1, "maprkc.jpg"); // Create a 700x700 panel with the image from the given file.
		tool = new RobotController(nip.getGraphicsPanel(0));  // Create a RobotController object, an instance of this class.
		nip.setTool(tool);  // Tell NIP to add and select the RobotController tool, so it will add the guideRobot method to its menu.
	}	

} 

