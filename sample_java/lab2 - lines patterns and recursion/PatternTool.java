package lab2;
/**
 * Name:Adrienne Sands
 * Lab Section: A
 * Date:9/14/10
 * Email:adrienne.i.sands@gmail.com
 * PatternTool.java
 * CSE 131 Lab 2
 */


import java.awt.Color;
import java.util.Random;

import nip.*;

public class PatternTool extends Tool{
	static Random random = new Random();  // A random number generator, used to create colors.
	private final int MIN_SIZE = 100;
	private final int THRESHHOLD = 2;

	//Recursive flower main  method.
	public void makeFlower() {
		GraphicsPanel panel = nip.getTargetPanel();
		Color color = randomColor();
		Ellipse base = new Ellipse(0, 0, panel.getWidth(), panel.getHeight(), color, true);
		base.setFillColor(color);
		makeFlowerHelper(base);
		panel.add(base);

		//The above 'panel' instance variable is what you'll add your ellipses to.
	}

	public void makeFlowerHelper(Ellipse base) {
		int width = base.getWidth();
		int height = base.getHeight();
		int newWidth = (width/2);
		int newHeight = (height/2);
		
		int x = base.getX();
		int y = base.getY();
		int left = newWidth/2; //first horizontal boundary
		int top = newHeight/2; //first vertical boundary
		int right = x+newWidth; //second horizontal boundary
		int bottom = y+newHeight; //second vertical boundary
		if (width<=MIN_SIZE || height<=MIN_SIZE) {
			//do nothing
		}
		else {
			draw(x+left, y, newWidth, newHeight, randomColor());
			draw(x+left, bottom, newWidth, newHeight, randomColor());
			draw(x, y+top, newWidth, newHeight, randomColor());
			draw(right, y+top, newWidth, newHeight, randomColor());
			draw(x+left, y+top, newWidth, newHeight, randomColor());
		}
	}

	public void draw(int x, int y, int width, int height, Color color) {
		GraphicsPanel panel = nip.getTargetPanel();
		Ellipse shape = new Ellipse(x, y, width, height, color, true);
		shape.setFillColor(color);
		makeFlowerHelper(shape);
		panel.add(shape);
	}

	//Add any helper methods for the recursive flower here.
	//TODO

	//Persian recursion main method.
	public void makePersian() {
		Image target = nip.getTargetImage();
		ColorPalette palette = new ColorPalette(18);
		Color first = palette.colorAtIndex(0);
		target.fillRegion(0, 0, target.getWidth(), target.getHeight(), first);
		persianPattern(0, 0, target.getWidth(), target.getHeight(), target, palette);
	}

	public void persianPattern(int x, int y, int width, int height, Image img, ColorPalette palette) {
		int c1 = palette.indexOfColor(img.getPixelColor(x,y));
		int c2 = palette.indexOfColor(img.getPixelColor(x+width-1 , y));
		int c3 = palette.indexOfColor(img.getPixelColor(x+width-1,y+height-1));
		int c4 = palette.indexOfColor(img.getPixelColor(x,y+height-1));

		if(width>THRESHHOLD && height>THRESHHOLD) {
			int newIndex = (247*(c1+c2+c3+c4+5)%18);
			Color lineColor = palette.colorAtIndex(newIndex);
			img.fillRegion(x, (y+(height/2)-1), width, THRESHHOLD, lineColor);
			img.fillRegion((x+(width/2)-1), y, THRESHHOLD, height, lineColor);
			persianPattern(x, y, (width/2), (height/2), img, palette);
			persianPattern(x+(width/2), y+(height/2), (width/2), (height/2), img, palette);
			persianPattern(x, y+(height/2), (width/2), (height/2), img, palette);
			persianPattern(x+(width/2), y, (width/2), (height/2), img, palette);
		}
		else {
			//do nothing
		}
	}

	// For the "flower" pattern, you can call the following method to generate random
	// colors.  However, for the "Persian recursion" pattern, you should use
	// an instance of the provided ColorPalette class to create a set of colors for your rug.
	static Color randomColor() {
		return new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256), 175);
	}

	// This method will appear in the NIP menu, in case you want to clear the display during testing.
	public void clear() {
		nip.getTargetPanel().clear();
		Image img = nip.getTargetImage();
		img.fillRegion(0, 0, img.getWidth(), img.getHeight(), Color.WHITE);
	}

	@Override
	public void actionNameCalled(String name) {
		if (name == "Flower") makeFlower();
		else if (name == "Persian") makePersian();
		else if (name == "Clear") clear();
		else return;
	}

	@Override
	public String[] getEventNames() {
		String[] s = {"Flower", "Persian", "Clear"};
		return s;
	}

	public String toString() {
		return "patterns";
	}

	public static void main(String args[]) {
		new NIP(new PatternTool(), 512, 512, 1);
	}

}
