package lab2;
import java.awt.Color;
import java.util.ArrayList;
import java.util.Random;

/**
 * A ColorPalette is created to hold a collection of a given number of colors.
 * The colors are generated randomly.  Each color has an index in the range 0 to n-1, where n is
 * the number of colors.  Methods are provided to determine the index of a given color,
 * and to get the color for a particular index.
 * 
 * You should NOT need to modify this file, and it does not need to be included in your lab packet.
 * 
 * @author Kenneth J. Goldman<BR>
 * Created Sep 22, 2005
 */

public class ColorPalette {
	ArrayList<Color> palette = new ArrayList<Color>();
	static Random random = new Random();
	
	/**
	 * Creates a color palette with the given number of colors
	 * @param numColors the number of colors to create
	 */
	public ColorPalette(int numColors) {
		for (int i = 0; i < numColors; i++)
			palette.add(randomColor());
	}
	
	/**
	 * Returns the number of colors in this palette.
	 * @return the size of the palette
	 */
	public int size() {
		return palette.size();
	}
	
	/**
	 * Finds the color number corresponding to a color
	 * @param c the color for which the color number is desired
	 * @return the number of the given color
	 */
	public int indexOfColor(Color c) {
		int i = palette.indexOf(c);
		if (i < 0)
			throw new IllegalArgumentException("Color " + c + " is not in the color palette.");
		return i;
	}
	
	/**
	 * Finds the color with a given color number.
	 * @param index the color number
	 * @return the color with the given index
	 */
	public Color colorAtIndex(int index) {
		if (index < 0 || index >= size())
			throw new IllegalArgumentException("Index " + index + " is out of range.");
		return palette.get(index);
	}
	
	/**
	 * Creates a random color
	 * @return a color with red, green, and blue values chosen at random
	 */
	public static Color randomColor() {
		Color c = new Color(random.nextInt(256),random.nextInt(256),random.nextInt(256));
		return c;
	}
}

