package lab8;

import static org.junit.Assert.*;

import org.junit.Test;

import static lab8.ListItem.*;


public class ListItemTest {

	private ListItem l2 = 
		new ListItem(3, 
				new ListItem(5,
						new ListItem(9,
								new ListItem(3,
										new ListItem(2,
												new ListItem(4,null)
										)
								)
						)
				)
		);

	private ListItem l3 =
		new ListItem(6,
				new ListItem(7,
						new ListItem(6,
								new ListItem(9, null)
						)
				)
		);

	private ListItem l6 =
		new ListItem(3,
				new ListItem(2,
						new ListItem(6,
								new ListItem(9, null)
						)
				)
		);

	private ListItem allOdd =
		new ListItem(1,
				new ListItem(3,
						new ListItem(7,
								new ListItem(5, null)
						)
				)
		);

	@Test
	public void testDuplicate() {
		ListItem l2dup = l2.duplicate();
		//
		// Make sure the list returned by duplicate() is indeed a copy
		//   and not the original, throughout
		//
		ListItem l2at    = l2;
		ListItem l2dupat = l2dup;
		while (l2at != null && l2dupat != null) {
			assertFalse("you must copy the list", l2at == l2dupat);
			l2at    = l2at.next;
			l2dupat = l2dupat.next;
		}
		//
		// But they should look the same
		//
		assertEquals(l2.toString(), l2dup.toString());
	}

	@Test
	public void testLength() {
		assertEquals(6, l2.length());
		assertEquals(4, l3.length());
		assertEquals(6, l2.duplicate().length());
		assertEquals(4, l3.duplicate().length());
	}

	@Test
	public void testStretch() {
		//
		// Example from web page
		//
		assertEquals("6 6 7 7 6 6 9 9", l3.stretch(2).toString());
		//
		// Stretch a lot of times and make sure each resulting length is right
		//
		for (int i=1; i < 100; ++i) {
			assertEquals(l3.length()*i, l3.stretch(i).length());
		}
		//
		// Stretch of 1 should return same string
		//
		assertEquals(l3.toString(), l3.stretch(1).toString());
	}

	@Test
	public void testFind() {
		assertEquals("6 7 6 9", l3.find(6).toString());
		assertEquals("7 6 9", l3.find(7).toString());
		assertEquals(null, l3.find(131));
	}

	@Test
	public void testMax() {
		assertEquals(9, l2.max());
		assertEquals(-44, new ListItem(-44, null).max());
	}

	@Test
	public void testEvenElements() {
		assertEquals("2 6", evenElements(l6).toString());
		assertEquals(null, evenElements(allOdd));
		assertEquals(null, evenElements(null));
	}

	@Test
	public void testPairwiseSum(){
		assertEquals("4 5 13 14", pairwiseSum(l6, allOdd).toString());
		assertEquals("6 4 12 18", pairwiseSum(l6, l6).toString());
		assertEquals("9 9 12 18", pairwiseSum(l6, l3).toString());
	}

	@Test
	public void testSmallElements(){
		assertEquals(null, smallElements(l3, 2));
		assertEquals("2", smallElements(l6, 2).toString());
		assertEquals("1", smallElements(allOdd, 1).toString());
		assertEquals(allOdd.toString(), smallElements(allOdd, 7).toString());
		assertEquals(null,smallElements(l2, 1));
	}

	@Test
	public void testScale(){
		assertEquals("1 3 7 5", allOdd.toString());
		scale(allOdd, 1);
		assertEquals("1 3 7 5", allOdd.toString());
		scale(allOdd, 3);
		assertEquals("3 9 21 15", allOdd.toString());
		assertEquals("3 5 9 3 2 4", l2.toString());
		scale(l2, 0);
		assertEquals("0 0 0 0 0 0", l2.toString());
	}

	@Test
	public void testInsertAfter(){
		assertEquals("1 3 7 5", allOdd.toString());
		insertAfter(allOdd, 4, 5);
		assertEquals("1 3 7 5 4", allOdd.toString());
		assertEquals("3 5 9 3 2 4", l2.toString());
		insertAfter(l2, 0, 7);
		assertEquals("3 5 9 3 2 4", l2.toString());
		insertAfter(l2, 0, 3);
		assertEquals("3 0 5 9 3 0 2 4", l2.toString());
	}

	@Test
	public void testReverse(){
		assertEquals("4 2 3 9 5 3", l2.reverseLoop().toString());
		assertEquals("4 2 3 9 5 3", l2.reverseRecurse().toString());
		assertEquals("9 6 7 6", l3.reverseLoop().toString());
		assertEquals("9 6 7 6", l3.reverseRecurse().toString());
		assertEquals(l3.length(), l3.reverseLoop().length());
		assertEquals(l3.length(), l3.reverseRecurse().length());
	}
}
