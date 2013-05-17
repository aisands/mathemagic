package lab9;

public class ListItem<E extends Comparable<E>> {
	
	E element;
	ListItem<E> next;

	/**
	 * Creates a single list item.
	 * @param number the value to be held in the item
	 * @param next a reference to the next item in the list
	 */
	ListItem(E element, ListItem<E> next) {
		this.element = element;
		this.next   = next;
	}

	/**
	 * Return a copy of this list using recursion.  No
	 * credit if you use any iteration!  All existing lists should remain
	 * intact -- this method must not mutate anything.
	 * @return duplicated list
	 */
	public ListItem<E> duplicate() {
		ListItem<E> duplicate;
		if (next != null){ //if there is a next term
			duplicate = new ListItem<E>(element, next.duplicate());
		}
		else duplicate = new ListItem<E> (element, null);
		return duplicate;


	}

	/**
	 * Recursively compute the number of elements in the list. No
	 * credit if you use any iteration!  All existing lists should remain
	 * intact.
	 * @return length
	 */
	public int length() { //assumes the list has at least one ListItem in it
		if (this.next==null){//if there is only one item in the list
			return 1;
		}
		else return 1 + this.next.length();
	}

	/**
	 * Return a new list, like duplicate(), but every element
	 * appears n times instead of once.  See the web page for details.
	 * You must do this method iteratively.  No credit
	 * if you use any recursion!
	 * @param n a positive (never 0) number specifying how many times to copy each element
	 * @return
	 */

	public ListItem<E> stretch(int n) { //assumes n is positive
		ListItem<E> oldPointer = this; //originally points to the first item of the old list
		ListItem<E> head = new ListItem<E> (this.element, this.next); //first item in the new list
		ListItem<E> newPointer = head; //originally points to the first item of the new list

		while (oldPointer!=null){ //while we aren't at the end of the original list
			for (int i=0; i<n; i++){
				newPointer.next= new ListItem<E>(oldPointer.element, oldPointer.next);
				newPointer = newPointer.next;
			}
			oldPointer = oldPointer.next;
		} 
		return head.next;
	}

	/**
	 * Return the first ListItem, looking from "this" forward,
	 * that contains the specified number.  No lists should be
	 * modified as a result of this call.  You may do this recursively
	 * or iteratively, as you like.
	 * @param n
	 * @return
	 */

	public ListItem<E> find(E element) {
		if (this.element == element){ //if n is the first number, return this;
			return this;
		}
		else if (this.next!= null){ //if the list is more than one item long
			if (this.next.element == element){ //and n is the item immediately after this, return next
				return this.next;
			}
			else{ return this.next.find(element); //else recurse
			}
		}
		else return null;//else the item is not in the list
	}

	/**
	 * Return the maximum number contained in the list
	 * from this point forward.  No lists should be modified
	 * as a result of this call.  You may do this method recursively
	 * or iteratively,as you like.
	 * @return
	 */

	public E max() {
		if (this.next == null || this.element.compareTo(this.next.max())>0){
			return this.element;
		}
		else return this.next.max();
	}

	/**
	 * Returns a copy of the list beginning at ls, but containing
	 * only elements that are even.
	 * @param ls
	 * @return
	 */
	public static ListItem<Integer> evenElements(ListItem<Integer> ls) {
		if (ls == null){
			return null;
		}
		else {
			if (ls.element % 2 == 0){
				return new ListItem<Integer> (ls.element, ListItem.evenElements(ls.next));
			}
			else {
				return ListItem.evenElements(ls.next);
			}
		}
	}


	/**
	 * Returns a string representation of the values reachable from
	 * this list item.  Values appear in the same order as the occur in
	 * the linked structure.  Leave this method alone so our testing will work
	 * properly.
	 */
	public String toString() {
		if (next == null)
			return ("" + element);
		else
			return (element + " " + next); // calls next.toString() implicitly
	}
}


