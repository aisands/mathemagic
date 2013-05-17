package lab9;

import java.util.NoSuchElementException;

/**
 * Implements a Map as a binary search tree of (key,value) pairs.
 * CSE131 Lab 9
 * @author
 * @version 1.0
 * Date: 11/14/10
 */
public class TreeMap<K extends Comparable<K>,V> implements Map<K,V> {
	TreeNode<Mapping<K,V>> head;

	public TreeMap(){
		this.head= null;
	}

	public void put(K key, V value) {
		TreeNode<Mapping<K,V>> parent = this.findParent(key);
		Mapping<K,V> map = new Mapping<K,V>(key,value);
		TreeNode<Mapping<K,V>> newNode = new TreeNode<Mapping<K, V>>(map, parent, null, null);

		if (parent == null){
			this.head = newNode;
		}
		else{
			if (map.key.compareTo(parent.element.key)< 0){
				parent.leftChild = newNode;
			}
			else if (map.key.compareTo(parent.element.key)==0){
				parent.element.value = value;
			}
			else {
				parent.rightChild = newNode;
			}
		}
	}



	public V get(K key) {
		TreeNode<Mapping<K,V>> parent = this.findParent(key);

		if (key.compareTo(parent.element.key)< 0 && !parent.leftChild.deleted){
			return parent.leftChild.element.value;
		}
		else if (key.compareTo(parent.element.key)==0 && !parent.deleted){
			return parent.element.value;
		}
		else if (key.compareTo(parent.element.key)>0&& !parent.rightChild.deleted) {
			return parent.rightChild.element.value;
		}
		else throw new NoSuchElementException();
	}


	public boolean contains(K key) {
		try{
			this.get(key);
			return true;
		}
		catch (Exception e){
			return false;
		}
	}

//	public void delete(K key){
//		if (contains(key)){ //the key is in the treemap
//			TreeNode<Mapping<K,V>> parent = findParent(key);
//			TreeNode<Mapping<K,V>> node = parent;
//
//	
//			if (key.compareTo(parent.leftChild.element.key)==0){ //if the node is the parent's left child
//				node = parent.leftChild;
//			}
//			else if (key.compareTo(parent.rightChild.element.key)==0){ //if the node is the parent's right child
//				node= parent.rightChild;
//			}
//			
//			//
//			
//						
//			if ((node.leftChild== null)&&(node.rightChild==null)){//if the node is a leaf with no children
//				node = null;
//			}
//			
//			if ((node.leftChild== null && node.rightChild!=null)){ //if the node has a rightChild
//				parent.rightChild = node.leftChild;
//			}
//			
//			if ((node.rightChild== null && node.leftChild!= null)){ //if the node has a leftChild
//				parent.leftChild = node.rightChild;
//			}
//			
//			else{ //the node has 2 children
//				
//			}
//				
//			
//		}
//			else throw new IllegalArgumentException(); //the key is not in the treemap, can't be deleted
//		}

		public boolean remove(K key) {
			if (this.contains(key)){
				TreeNode<Mapping<K,V>> parent = findParent(key);
				if (key.compareTo(parent.leftChild.element.key)==0){
					parent.leftChild.deleted = true;
				}
				else {
					parent.rightChild.deleted = true;
				}
				return true;
			}
			else return false;
		}

		public String toString() {
			if (this.head!=null){
				return this.head.toString();
			}
			else return "";
		}

		private TreeNode<Mapping<K,V>> findParent(K key){ 
			TreeNode<Mapping<K,V>> traverser = head;
			TreeNode<Mapping<K,V>> parent = traverser;
			while (traverser!= null){
				if (key.compareTo(traverser.element.key)<0){
					parent = traverser;
					traverser=traverser.leftChild;
				}
				else if (key.compareTo(traverser.element.key)==0){
					return parent;
				}
				else {
					parent= traverser;
					traverser=traverser.rightChild;
				}
			}				
			return parent;
		}
	}
