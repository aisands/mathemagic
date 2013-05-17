package lab2;
/**
 * Name:Adrienne Sands
 * Lab Section: A
 * Date:9/14/10
 * Email:adrienne.i.sands@gmail.com
 * LineTool.java
 * CSE 131 Lab 2
 */


import java.awt.Color;
import java.awt.Point;
import java.awt.event.MouseEvent;

import nip.*;

public class LineTool extends Tool{
	Point start = new Point(0,0);
	Point end = new Point(0,0);
	Line temporaryLine = new Line(0, 0, 0, 0);
	boolean dashed = false;
	int dashLength = 5;

	// Complete this method to draw a line recursively by coloring pixels in the image.
	// When you color the pixels, use Color.RED as the color value so your line will be red.
//	private void drawLine(Image image, double x1, double y1, double x2, double y2) {
//		if (x1 != x2 && y1 != y2){
//			//calculate slope
//			double dy = y2-y1;
//			double dx = x2-x1;
//			double factor = 1000;
//			
//			//color first pixel
//			image.setPixel((int)x1, (int)y1, Color.RED);
//			drawLine(image,x1+(dx/factor),y1+(dy/factor),x2,y2);
//		}
//	}
	
	private void drawLine(Image image, double x1, double y1, double x2, double y2){
		double xMid = (x1+x2)/2;
		double yMid = (y1+y2)/2;
		double threshold = 0.5;
		
		//threshold chosen since the points get infinitely close to one another
		
		if((Math.abs(x1-xMid)<threshold) && (Math.abs(y1-yMid)<threshold))return;
		if((Math.abs(x2-xMid)<threshold) && (Math.abs(y2-yMid)<threshold))return;	
		else{ 
			image.setPixel((int)x1, (int)y1, Color.RED);
			image.setPixel((int)x2, (int)y2, Color.RED);
			image.setPixel((int)xMid, (int)yMid, Color.RED);
			drawLine(image, x1, y1, xMid, yMid);
			drawLine(image, xMid, yMid, x2, y2);
		}
		
	}

	// Complete this method to draw a dashed line recursively by coloring pixels in the image.
	// The last parameter is the desired (approximate) length of the dashes and spaces.
	// Hint: At some recursive calls, you may make a call to your drawLine method.
	private void drawDashedLine(Image image, double x1, double y1, double x2, double y2, int dashLength) {
		double distance = Math.sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1));
		double xMid = (x1+x2)/2;
		double yMid = (y1+y2)/2;
		if ((int)distance<=2*dashLength) {
			drawLine(image, xMid,yMid,x2,y2);
			} 
		else {
			drawDashedLine(image,x1,y1,xMid,yMid, dashLength);
			drawDashedLine(image,x2,y2,xMid,yMid, dashLength);
			} 
		}		
	
	
	
	@Override
	public void actionNameCalled(String name) {
		if (name == "Toggle Dash On/Off") toggleDashed();
		else if (name == "Set Dash Length...") setDashLength();
		else if (name == "Clear") clear();
		else return;
	}

	@Override
	public String[] getEventNames() {
		String[] s = {"Toggle Dash On/Off", "Set Dash Length...", "Clear"};
		return s;
	}

	// This method will appear in the NIP menu, in case you want to clear the display during testing.
	public void clear() {
		Image img = nip.getTargetImage();
		img.fillRegion(0, 0, img.getWidth(), img.getHeight(), Color.WHITE);
		nip.setStatusText("panel cleared");
	}

	public void toggleDashed() {
		dashed = !dashed;
		nip.setStatusText("Dashed lines = " + dashed + " || Dash length = " + dashLength);
	}

	public void setDashLength() {
		dashLength = Dialog.getInteger("Enter new dash length:");
		if (dashLength <= 0) dashLength = 1;
		if (dashLength > 100) dashLength = 100;
		nip.setStatusText("Dashed lines = " + dashed + " || Dash length = " + dashLength);
	}
	
	@Override
	public void mousePressed(MouseEvent e) {
		GraphicsPanel panel = (GraphicsPanel)(e.getSource());
		int x, y;
		start.x = x = e.getX();
		start.y = y = e.getY();
		temporaryLine.setCorners(x,y,x,y);
		panel.add(temporaryLine);
	}
	
	@Override
	public void mouseDragged(MouseEvent e) {
		GraphicsPanel panel = (GraphicsPanel)(e.getSource());
		int x = e.getX();
		int y = e.getY();
		if (panel.getBounds().contains(x,y)) {
			end.x = x;
			end.y = y;
			temporaryLine.setCorners(start.x, start.y, end.x, end.y);
		}
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		GraphicsPanel panel = (GraphicsPanel)e.getSource();
		panel.remove(temporaryLine);
		if (dashed)
			drawDashedLine(panel.getMainImage(), start.x, start.y, end.x, end.y, dashLength);
		else
			drawLine(panel.getMainImage(), start.x, start.y, end.x, end.y);
	}

	public String toString() {
		return "lines";
	}

	public static void main(String args[]) {
		new NIP(new LineTool(), 256, 256, 1);
	}

}
