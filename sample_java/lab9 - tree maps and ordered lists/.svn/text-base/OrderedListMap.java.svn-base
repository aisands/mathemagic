package lab9;

import java.util.NoSuchElementException;

/**
 * Implements a Map as an ordered list of (key,value) pairs.
 * CSE131 Lab 9
 * @author
 * @version 1.0
 * Date: 11/16/10
 */

public class OrderedListMap<K extends Comparable<K>,V> implements Map<K,V> {
	ListItem<Mapping<K,V>> head;

	public OrderedListMap(){
		this.head = new ListItem<Mapping<K,V>>(new Mapping<K,V>(null, null), null); //head that points to null
	}

	public void put(K key, V value) {
		ListItem<Mapping<K,V>> predecessor = this.findPredecessor(key);
		try{
			if (key.compareTo(predecessor.next.element.key)==0){
				predecessor.next.element.value = value;
			}
			else{
				Mapping <K,V> pairing = new Mapping<K,V> (key,value);
				predecessor.next = new ListItem<Mapping<K,V>>(pairing, predecessor.next);
			}
		}
		catch(NullPointerException e){
			Mapping <K,V> pairing = new Mapping<K,V> (key,value);
			predecessor.next = new ListItem<Mapping<K,V>>(pairing, predecessor.next);
		}
	}

	public V get(K key) { //returns the value at a specific key
		ListItem <Mapping<K,V>> predecessor = this.findPredecessor((key));

		if (predecessor.next.element.key.compareTo(key)==0 || predecessor.element.key.compareTo(key) == 0){
			return predecessor.next.element.value; //return its value
		}
		else throw new NoSuchElementException();
	}

	public boolean contains(K key) {
		try {
			if (this.get(key)!=null){
				return true;
			}
			else return false;
		}
		catch (Exception e){
			return false;
		}
	}

	public boolean remove(K key) {
		ListItem<Mapping<K,V>> predecessor = this.findPredecessor(key);
		if (predecessor.next.element.key.compareTo(key)==0){ //if an element with that key exists
			predecessor.next = predecessor.next.next;
			return true;
		}
		else {
			return false;
		}
	}

	public String toString() {
		return head.next.toString();
	}



	public boolean isEmpty(){
		return (head.next == null);
	}

	private ListItem<Mapping<K,V>> findPredecessor(K key){ //list goes from small to large values
		ListItem<Mapping<K,V>> previousPointer = head;
		ListItem<Mapping<K,V>> currentPointer = head.next;

		while (currentPointer!= null){ //while we aren't at the end of the list
			if (key.compareTo(currentPointer.element.key)<=0){ //if the key is less than or equal to the key at currentPointer
				return previousPointer;
			}
			else { //if the key is greater than the key at currentPointer, continue to traverse the list
				previousPointer = currentPointer;
				currentPointer = currentPointer.next;
			}
		}
		return previousPointer; //previousPointer is the head if the list is empty (and currentPointer = null)
	}
}
