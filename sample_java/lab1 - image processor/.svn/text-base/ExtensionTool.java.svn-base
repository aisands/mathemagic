package lab1;

import java.awt.Color;

import nip.*;


public class ExtensionTool extends Tool {
	
	public String[] getEventNames() {
		String[] s = {"Subtract Background", "Replace Background"};
		return s;
	}
	
	public void actionNameCalled(String name) {
		if (name == "Subtract Background") backgroundSubtraction();
		else if (name == "Replace Background") backgroundReplacement();
		else;
	}
	
	public void backgroundSubtraction() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getSecondarySourceImage();
		Image i2 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old0 = i0.getPixelColor(x, y);
				Color old1 = i1.getPixelColor(x, y);
				i2.setPixel(x, y, ImageProcessor.bgSubtract(old0, old1));
			}
		}
	}
	
	public void backgroundReplacement() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getSecondarySourceImage();
		Image i2 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old0 = i0.getPixelColor(x, y);
				Color old1 = i1.getPixelColor(x, y);
				i2.setPixel(x, y, ImageProcessor.bgReplace(old0, old1));
			}
		}
	}
	
	public String toString() {
		return "lab1 extension";
	}
}
