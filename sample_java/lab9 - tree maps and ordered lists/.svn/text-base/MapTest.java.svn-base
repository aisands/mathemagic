package lab9;

import static org.junit.Assert.*;
import java.util.NoSuchElementException;
import org.junit.Test;

public abstract class MapTest {
	
	public abstract Map<String,Integer> createMap();
	
	@Test
	public void testAllMethods() {
		Map<String,Integer> m = createMap();
	    m.put("meow",2);
	    assertEquals(2, (int) m.get("meow"));
	    m.put("bow wow",8);
	    assertEquals(2, (int) m.get("meow"));
	    assertEquals(8, (int) m.get("bow wow"));
	    System.out.println("--- cats and dogs:\n"+ m.toString());

	    m.put("oink",5);
	    m.put("quack",4);
	    m.put("baa",5);
	    System.out.println("\n--- after adding pigs, ducks, and sheep:\n"+ m.toString());

	    m.put("arf",12);
	    m.put("neigh", 2);
	    m.put("moo",7);
	    System.out.println("\n--- after adding little dogs, horses, and cows:\n"+ m.toString());

	    assertEquals(2, (int) m.get("meow"));
	    assertEquals(4, (int) m.get("quack"));
	    assertEquals(5, (int) m.get("baa"));
	    assertEquals(7, (int) m.get("moo"));
	    assertEquals(5, (int) m.get("oink"));
	    assertEquals(8, (int) m.get("bow wow"));
	    assertEquals(12, (int) m.get("arf"));
	    assertEquals(2, (int) m.get("neigh"));

	    m.put("oink", m.get("oink")-1);
	    assertEquals(4, (int) m.get("oink"));

	    assertEquals(true, m.contains("baa"));
	    m.remove("baa");
	    System.out.println("\n--- after removing sheep:\n"+ m.toString());
	    assertEquals(false, m.contains("baa"));
	    try {
	    	   m.get("baa");
	    	   fail("Should get a NoSuchElementException");
	    } catch (NoSuchElementException nsee) {
	    		// do nothing because we expect m.get("baa") to throw this exception
	    }

	    m.remove("meow");
	    m.remove("moo");
	    System.out.println("\n--- after removing cats and cows:\n"+ m.toString());
	  }
	

}
