package lab1;

import java.awt.Color;

import nip.*;


public class ProcessorTool extends Tool {
	
	public String[] getEventNames() {
		String[] s = {"Example: Darker", "Example: Combine", "Example: Purplish",
				"Copy", "Composite", "Negative", "Posterize", "Brighter",
				"Grayscale", "Black and White", "Combine Brighter"};
		return s;
	}
	
	public void actionNameCalled(String name) {
		if (name == "Example: Darker") example_darker();
		else if (name == "Example: Combine") example_combine();
		else if (name == "Example: Purplish") example_purplish();
		else if (name == "Copy") copy();
		else if (name == "Composite") composite();
		else if (name == "Negative") negative();
		else if (name == "Posterize") posterize();
		else if (name == "Brighter") brighter();
		else if (name == "Grayscale") grayscale();
		else if (name == "Black and White") blackWhite();
		else if (name == "Combine Brighter") combineBrighter();
		else System.out.println("no match!");
	}
	
	public void example_darker() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				Color newC = new Color(ImageProcessor.darker(old.getRed()),
						ImageProcessor.darker(old.getGreen()),
						ImageProcessor.darker(old.getBlue()));
				i1.setPixel(x, y, newC);
			}
		}
	}
	
	public void example_combine() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getSecondarySourceImage();
		Image i2 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old0 = i0.getPixelColor(x, y);
				Color old1 = i1.getPixelColor(x, y);
				Color newC = new Color(ImageProcessor.combine(old0.getRed(), old1.getRed()) % 256,
						ImageProcessor.combine(old0.getGreen(), old1.getGreen()) % 256,
						ImageProcessor.combine(old0.getBlue(), old1.getBlue()) % 256);
				i2.setPixel(x, y, newC);
			}
		}
	}
	
	public void example_purplish() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				i1.setPixel(x, y, ImageProcessor.purplish(old));
			}
		}
	}
	
	public void copy() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				Color newC = new Color(ImageProcessor.copy(old.getRed()),
						ImageProcessor.copy(old.getGreen()),
						ImageProcessor.copy(old.getBlue()));
				i1.setPixel(x, y, newC);
			}
		}
	}
	
	public void composite() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getSecondarySourceImage();
		Image i2 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old0 = i0.getPixelColor(x, y);
				Color old1 = i1.getPixelColor(x, y);
				Color newC = new Color(ImageProcessor.composite(old0.getRed(), old1.getRed()),
						ImageProcessor.composite(old0.getGreen(), old1.getGreen()),
						ImageProcessor.composite(old0.getBlue(), old1.getBlue()));
				i2.setPixel(x, y, newC);
			}
		}
	}
	
	public void negative() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				Color newC = new Color(ImageProcessor.negative(old.getRed()),
						ImageProcessor.negative(old.getGreen()),
						ImageProcessor.negative(old.getBlue()));
				i1.setPixel(x, y, newC);
			}
		}
	}
	
	public void posterize() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				Color newC = new Color(ImageProcessor.posterize(old.getRed()),
						ImageProcessor.posterize(old.getGreen()),
						ImageProcessor.posterize(old.getBlue()));
				i1.setPixel(x, y, newC);
			}
		}
	}
	
	public void brighter() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				i1.setPixel(x, y, ImageProcessor.brighter(old));
			}
		}
	}
	
	public void grayscale() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				i1.setPixel(x, y, ImageProcessor.grayscale(old));
			}
		}
	}
	
	public void blackWhite() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old = i0.getPixelColor(x, y);
				i1.setPixel(x, y, ImageProcessor.blackAndWhite(old));
			}
		}
	}
	
	public void combineBrighter() {
		Image i0 = nip.getPrimarySourceImage();
		Image i1 = nip.getSecondarySourceImage();
		Image i2 = nip.getTargetImage();
		for (int x = 0; x < i0.getWidth(); x++) {
			for (int y = 0; y < i0.getHeight(); y++) {
				Color old0 = i0.getPixelColor(x, y);
				Color old1 = i1.getPixelColor(x, y);
				i2.setPixel(x, y, ImageProcessor.combineBrighter(old0, old1));
			}
		}
	}
	
	public String toString() {
		return "lab1";
	}
}
