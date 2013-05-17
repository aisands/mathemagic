package lab1;
/**
 * Name:Adrienne Sands
 * Lab Section: A
 * Date: 9/7/2010
 * ImageProcessor.java
 * CSE 131 Lab 1
 */

import java.awt.Color;

import nip.*;


public class ImageProcessor {
	// Some sample methods:

	// This method cuts each color component of a pixel in half to produce the new image.
	// USED IN: example_darker
	public static int darker(int pixelComponent) {
		return pixelComponent/2;
	}

	// This method sums the color components of two pixels to produce a third.
	// Note that when the total exceeds 255, there is a strange effect.
	// USED IN: example_combine
	public static int combine(int pixelAComponent, int pixelBComponent) {
		return pixelAComponent+pixelBComponent;
	}

	// This method takes the color of each pixel and creates a new color without any green.
	// USED IN: example_purplish
	public static Color purplish(Color c) {
		int red = c.getRed();
		int blue = c.getBlue();
		return new Color(red, 0, blue);
	}

	// Now that you've seen the examples, complete the following methods.
	// The headers have been completed for you.
	//
	// NB: The 'return 0' and 'return new Color(0,0,0)' lines are simply placeholders
	// to prevent the compiler from complaining.  They should be removed or modified when
	// you add your implementation.

	//This method copies the components of a pixel without changing it.
	// USED IN: copy
	public static int copy(int pixelComponent) {
		return pixelComponent;
	}

	//This method averages the color components of two pixels.
	// USED IN: composite
	public static int composite(int a, int b) {
		return (a + b)/2;
	}

	//This method returns the negative of a pixel by inverting its color components.
	// USED IN: negative
	public static int negative(int a) {
			return 255-a;
	}

	//This method reduces the number of possible values for a given color component
	//from 256 to 2, by returning either 0 or 255 based on the original value.
	// USED IN: posterize
	public static int posterize(int a) {	
		return (a/128)*255;
	}

	//This method returns a color that is brighter than the original color.
	// USED IN: brighter
	public static Color brighter(Color c) {
		return c.brighter();
	}
	
	//This method returns a color that is some shade of gray, by making a new
	//color having equal RGB components.
	// USED IN: grayscale
	public static Color grayscale(Color c) {
			int red = c.getRed();
			int blue = c.getBlue();
			int green = c.getGreen();
			int gray= (red + blue + green)/3; 
			return new Color(gray, gray, gray);
			}

	//This method returns either black or white, based on the intensity of the
	//originally provided color.
	// USED IN: blackWhite
	public static Color blackAndWhite(Color c) {
		int red = c.getRed();
		int blue = c.getBlue();
		int green = c.getGreen();
		int RBG= (red + blue + green)/3;
		if (RBG>=128) return Color.WHITE;
		else return Color.BLACK;
	}

	//This method combines two images by choosing for each location the brighter 
	//pixel in the same location from the two source images.
	// USED IN: combineBrighter
	public static Color combineBrighter(Color c, Color d) {
		int redC = c.getRed();
		int blueC = c.getBlue();
		int greenC = c.getGreen();
		int redD = d.getRed();
		int blueD = d.getBlue();
		int greenD = d.getGreen();
		int RBGC= redC+blueC+greenC;
		int RBGD= redD+blueD+greenD;
		if (RBGC>=RBGD)return c;
		else return d;
	}
	
	//The following two methods are for the optional extension for this lab.
	
	//This method performs background subtraction by returning the color blue
	//if the two colors are close enough; otherwise, it returns the second color.
	public static Color bgSubtract(Color background, Color source) {
		int redSource = source.getRed();
		int blueSource = source.getBlue();
		int greenSource = source.getGreen();
		int redBack = background.getRed();
		int blueBack = background.getBlue();
		int greenBack = background.getGreen();
		int range=20;
		
	if ((Math.abs(redSource-redBack)<range)
			&&(Math.abs(blueSource-blueBack)<range)
			&&(Math.abs(greenBack-greenSource)<range)) {
			return Color.BLUE;}
	else return source; 
		
		
	}

	

	//This method performs background replacement by returning the color from the
	//second image if the color from the first image is blue; otherwise returns
	//the color from the first image.
	public static Color bgReplace(Color foreground, Color back) {
		if (foreground.equals(Color.BLUE)) return back;
		else return foreground;
		
	}


	/**
	 * Returns the name of this image processing class.
	 */
	public String toString() {
		return "Image Processor";
	}

	/*
	 * Java always looks for a "public static void main" method as the starting point for an application.
	 * The parameter, which you will ignore, is used for applications that take parameters from the command line.
	 * 
	 * This method creates a Ye Olde Photo Shoppe (NIP) object and then creates a new instance of the 
	 * ProcessorTool class (which uses the methods you've defined here) as the tool to be used by NIP.
	 *
	 */
	public static void main(String[] args) {
		NIP nip = new NIP(200, 300, 3, "one-bear.jpg", "brookings.jpg", "wrighton.jpg");   // create a NIP window with 3 panels, each 200x300
		nip.setTool(new ProcessorTool());  // set the current NIP tool to an instance of your ImageProcessor

		// If you do the optional extension for this assignment, uncomment the following line.
		new NIP(new ExtensionTool(), 200, 150, 3, "one-bear.jpg", "two-bears.jpg");
	}	

}
