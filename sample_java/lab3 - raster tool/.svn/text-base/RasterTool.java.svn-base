package lab3;
import nip.*;
import java.awt.Color;

/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 9/27/2010
 * Email: adrienne.i.sands@gmail.com
 * RasterTool.java CSE 131 Lab 3
 */

public class RasterTool extends Tool {

	public void flipHoriz(Image source, Image target) {
		for (int x = 0; x < source.getWidth(); x++) {
			for (int y = 0; y < source.getHeight(); y++) {
				target.setPixel(x, y, source.getPixel(source.getWidth() - 1 - x, y));
			}
		}
	}

	public void flipVert(Image source, Image target) {
		for (int x = 0; x < source.getWidth(); x++) {
			for (int y = 0; y < source.getHeight(); y++) {
				target.setPixel(x, y, source.getPixel(x, source.getHeight() - 1 - y));
			}
		}
	}

	public void flipLeft(Image source, Image target){
		for(int x = 0; x < source.getWidth()/2; x++) {
			for (int y = 0; y < (source.getHeight()); y++){
				target.setPixel(x, y, source.getPixel(x,y));
			}
		}	
		for (int x = (source.getWidth())/2; x <source.getWidth(); x++ ) {
			for (int y = 0; y < (source.getHeight()); y++) {
				target.setPixel(x, y, source.getPixel(source.getWidth() - 1- x, y));

			}
		}
	}

	public void flipBottom(Image source, Image target) {
		for (int x = 0; x < source.getWidth(); x++) {
			for (int y = 0; y < (source.getHeight())/2; y++) {
				target.setPixel(x, y, source.getPixel(x, source.getHeight() - 1- y));
			}
		}
		for (int x= 0; x < source.getWidth(); x++) {
			for (int y = source.getWidth()/2; y < source.getHeight(); y++){
				target.setPixel(x, y, source.getPixel(x, y));
			}
		}
	}

	public void gradient(Image image){
		for (double x = 0; x < image.getWidth(); x++){
			for (double y = 0; y < image.getHeight(); y++){
				int xpixel= (int)((x/image.getWidth())*255);
				int ypixel = (int) ((y/image.getHeight())*255); 				
				Color newColor = new Color (xpixel, ypixel, 128);
				image.setPixel((int)x, (int)y, newColor);
			}
		}
	}

	public void pixelComparison(Image source, Image target){
		for (double x = 1; x < source.getWidth()-1; x++){
			for (double y = 1; y < source.getHeight()-1; y++){

				int threshhold = 50;
				Color base = source.getPixelColor((int)x, (int) y);
				int baseRed= base.getRed();
				int baseBlue= base.getBlue();
				int baseGreen = base.getGreen();

				Color left = source.getPixelColor((int)x-1, (int)y);
				int leftRed= left.getRed();
				int leftBlue= left.getBlue();
				int leftGreen = left.getGreen();

				Color right = source.getPixelColor((int)x+1, (int)y);
				int rightRed= right.getRed();
				int rightBlue= right.getBlue();
				int rightGreen = right.getGreen();

				Color above = source.getPixelColor((int)x, (int)y+1);
				int aboveRed= above.getRed();
				int aboveBlue= above.getBlue();
				int aboveGreen = above.getGreen();

				Color below = source.getPixelColor((int)x, (int)y-1);
				int belowRed= below.getRed();
				int belowBlue= below.getBlue();
				int belowGreen = below.getGreen();

				if ((Math.abs(baseRed-leftRed)> threshhold)|| (Math.abs(baseRed-rightRed)> threshhold) || 
						(Math.abs(baseRed-aboveRed)> threshhold)||(Math.abs(baseRed-belowRed)> threshhold)){
					base = Color.BLACK; 
				}
				if ((Math.abs(baseBlue-leftBlue)> threshhold)|| (Math.abs(baseBlue-rightBlue)> threshhold) || 
						(Math.abs(baseBlue-aboveBlue)> threshhold)||(Math.abs(baseRed-belowBlue)> threshhold)){
					base = Color.BLACK;
				}
				if ((Math.abs(baseGreen-leftGreen)> threshhold)|| (Math.abs(baseGreen-rightGreen)> threshhold) || 
						(Math.abs(baseGreen-aboveGreen)> threshhold)||(Math.abs(baseGreen-belowGreen)> threshhold)){
					base = Color.BLACK;
				}
				else base = Color.WHITE;

				target.setPixel((int)x,(int)y, base);
			}
		}	
	}


	public void filter (Image source, Image target) {
		for (int x = 1; x < (source.getWidth() - 1); x++) {
			for (int y = 1; y < (source.getHeight() - 1); y++) {
				Color [][] color = {
						{ source.getPixelColor(x-1, y-1), source.getPixelColor(x, y-1), source.getPixelColor(x+1, y-1) },
						{ source.getPixelColor(x-1,y), source.getPixelColor(x,y), source.getPixelColor(x+1,y) },
						{ source.getPixelColor(x-1,y+1), source.getPixelColor(x,y+1), source.getPixelColor(x+1,y+1) }
				};

				target.setPixel(x, y, helpFilter(color));
			}
		}
	}
	public Color helpFilter(Color [][] color) {
		double[][] coefs = { // 3x3 array of filter coefficients
				{ .0625, .125, .0625 },
				{ .125, .25, .125 },
				{ .0625, .125, .0625 }
		};

		double red = 0;
		for (int i = 0; i < coefs.length ; i++){
			for (int j = 0; j < coefs.length; j++){
				red = red + color[i][j].getRed()*coefs[i][j];
			}
		}
		double blue = 0;
		for (int i= 0; i < coefs.length; i++){
			for (int j = 0; j <=2; j++){
				blue = (blue + color[i][j].getBlue()*coefs[i][j]);
			}
		}
		double green = 0;
		for (int i= 0; i < coefs.length; i++){
			for (int j = 0; j < coefs.length; j++){
				green = (green + color[i][j].getGreen()*coefs[i][j]);
			}
		}

		if (red > 255)
			red = 255;
		if (blue > 255)
			blue = 255;
		if (green > 255)
			green = 255;

		Color newColor = new Color((int)red, (int)blue,(int) green);
		return newColor;
	}


	public String[] getEventNames() {
		String[] s = { 
				"Flip Horizontally",
				"Flip Vertically",
				"Flip Left Half Horizontally",
				"Flip Bottom Half Vertically",
				"Color Gradient",
				"Edge Detection",
				"Filter"
				};
		return s;
	}

	// Don't forget to tell your tool here how it should respond when a menu
	// item is clicked!
	public void actionNameCalled(String name) {
		if (name.equals("Flip Horizontally"))
			flipHoriz(nip.getPrimarySourceImage(), nip.getTargetImage());
		if (name.equals("Flip Vertically"))
			flipVert(nip.getPrimarySourceImage(), nip.getTargetImage());
		if (name.equals("Flip Left Half Horizontally"))
			flipLeft(nip.getPrimarySourceImage(), nip.getTargetImage());
		if (name.equals("Flip Bottom Half Vertically"))
			flipBottom(nip.getPrimarySourceImage(), nip.getTargetImage());
		if (name.equals("Color Gradient"))
			gradient(nip.getPrimarySourceImage());
		if (name.equals("Edge Detection"))
			pixelComparison(nip.getPrimarySourceImage(), nip.getTargetImage());
		if (name.equals("Filter"))
			filter(nip.getPrimarySourceImage(), nip.getTargetImage());
	}

	public String toString() {
		return "raster";
	}

	public static void main(String args[]) {
		new NIP(new RasterTool(), 200, 300, 3, "", "brookings.jpg", "two-bears.jpg");
	}

}
