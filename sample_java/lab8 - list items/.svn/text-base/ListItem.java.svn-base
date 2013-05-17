package lab8;

/**
 * Holds a number in a linked list structure.
 * 
 * @author
 * @version 1.0
 * CSE131 Lab 8
 * Date: 10/29/10
 */

public class ListItem {
	int number;
	ListItem next;

	/**
	 * Creates a single list item.
	 * @param number the value to be held in the item
	 * @param next a reference to the next item in the list
	 */
	ListItem(int number, ListItem next) {
		this.number = number;
		this.next   = next;
	}

	/**
	 * Return a copy of this list using recursion.  No
	 * credit if you use any iteration!  All existing lists should remain
	 * intact -- this method must not mutate anything.
	 * @return duplicated list
	 */
	public ListItem duplicate() {
		ListItem duplicate;
		if (next != null){ //if there is a next term
			duplicate = new ListItem(number, next.duplicate());
		}
		else duplicate = new ListItem (number, null);
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

	public ListItem stretch(int n) { //assumes n is positive
		ListItem oldPointer = this; //originally points to the first item of the old list
		ListItem head = new ListItem (this.number, this.next); //first item in the new list
		ListItem newPointer = head; //originally points to the first item of the new list

		while (oldPointer!=null){ //while we aren't at the end of the original list
			for (int i=0; i<n; i++){
				newPointer.next= new ListItem(oldPointer.number, oldPointer.next);
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

	public ListItem find(int n) {
		if (this.number == n){ //if n is the first number, return this;
			return this;
		}
		else if (this.next!= null){ //if the list is more than one item long
			if (this.next.number == n){ //and n is the item immediately after this, return next
				return this.next;
			}
			else{ return this.next.find(n); //else recurse
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

	public int max() {
		if (this.next == null || this.number> this.next.max()){
			return this.number;
		}
		else return this.next.max();
	}

	/**
	 * Returns a copy of the list beginning at ls, but containing
	 * only elements that are even.
	 * @param ls
	 * @return
	 */
	public static ListItem evenElements(ListItem ls) {
		if (ls == null){
			return null;
		}
		else {
			if (ls.number % 2 == 0){
				return new ListItem (ls.number, ListItem.evenElements(ls.next));
			}
			else {
				return ListItem.evenElements(ls.next);
			}
		}
	}

	/**
	 * Return the pairwise Sum of ls1 and ls2
	 * @param ls1
	 * @param ls2
	 * @return
	 */
	public static ListItem pairwiseSum(ListItem ls1, ListItem ls2){
		if (ls1.next == null)
			return new ListItem(ls1.number + ls2.number, ls1.next);
		else
			return new ListItem(ls1.number + ls2.number, pairwiseSum(ls1.next, ls2.next));
	}
	
	
	/**
	 * Return a list excluding any number that is bigger than number n
	 * @param ls
	 * @param n
	 * @return
	 */
	public static ListItem smallElements(ListItem ls, int n){
		ListItem temp = ls.duplicate();
		ListItem ans, end;
		while(temp != null && temp.number > n){
			temp = temp.next;
		}
		if(temp != null){
			ans = new ListItem(temp.number, null);
			end = ans;
			temp = temp.next;
			while (temp != null){
				if(temp.number <= n){
					end.next = new ListItem(temp.number, null);
					end = end.next;
				}
				temp = temp.next;
			}
			return ans;
		}
		else
			return null;
	}
	
	/**
	 * Multiply n to all the numbers in the list
	 * @param ls
	 * @param n
	 * @return
	 */
	public static void scale (ListItem ls, int n){
		while(ls.next != null){
			ls.number = ls.number * n;
			ls = ls.next;
		}
		ls.number = ls.number * n;
	}

	
	/**
	 * Put a number i after each j in the list
	 * @param ls
	 * @param i
	 * @param j
	 */
	public static void insertAfter(ListItem ls, int i, int j){
		while (ls.next != null){
			if (ls.number == j){
				ls.next = new ListItem(i, ls.next);
				ls = ls.next;
			}
			ls = ls.next;
		}
		if (ls.number == j){
			ls.next = new ListItem(i, ls.next);
			ls = ls.next;
		}
	}
	
	
	/**
	 * Return the List in reverse order
	 * @return
	 */
	
	public ListItem assemble(ListItem add, ListItem list){
		ListItem store = add.next;
		add.next = list;
		list = add;
		if(store != null){
			list = assemble(store, list);
		}
		return list;
	}
	
	public ListItem reverseRecurse(){
		ListItem list = this.duplicate();
		return assemble(list, null);
	}
	
	
	/**
	 * Return the List in reverse order
	 * @return
	 */

	public ListItem reverseLoop() throws IllegalArgumentException{
		if (this == null){
			throw new IllegalArgumentException("Null List Can't be Reversed");
		}
		else{
			ListItem temp = this.duplicate();
			ListItem focus = null;
			ListItem other = null;
			while(temp != null){
				focus = new ListItem (temp.number, other);
				other = focus;
				temp = temp.next;
			}
			return focus;
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
				return ("" + number);
			else
				return (number + " " + next); // calls next.toString() implicitly
		}

	}
