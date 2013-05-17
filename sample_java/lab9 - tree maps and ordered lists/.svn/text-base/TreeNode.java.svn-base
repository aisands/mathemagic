package lab9;

public class TreeNode<E extends Comparable<E>> implements Comparable<TreeNode<E>> {
	E element;
	TreeNode<E> parent;
	TreeNode<E> leftChild;
	TreeNode<E> rightChild;
	boolean deleted;

	public TreeNode(E element, TreeNode<E> parent, TreeNode<E> leftChild, TreeNode<E> rightChild){
		this.element = element;
		this.parent = parent;
		this.leftChild = leftChild;
		this.rightChild = rightChild;
		this.deleted = false;
	}	

	public E getElement() {
		return element;
	}

	public TreeNode<E> getParent() {
		return parent;
	} 

	public TreeNode<E> getLeftChild() {
		return leftChild;
	}

	public TreeNode<E> getRightChild() {
		return rightChild;
	}

	public void setElement(E element) {
		this.element = element;
	}

	public void setParent(TreeNode<E> parent) {
		this.parent = parent;
	}

	public void setLeftChild(TreeNode<E> leftChild) {
		this.leftChild = leftChild;
	}

	public void setRightChild(TreeNode<E> rightChild) {
		this.rightChild = rightChild;
	}

	public int compareTo(TreeNode<E> node){
		return this.element.compareTo(node.element);
	}

	public String toString(){
		return toStringHelper(this, 0, "");
	}

	private String spaceMaker(int numTabs){
		String result = "";
		for (int i=0; i<numTabs; i++){
			result += "\t";
		}
		return result;
	}

	private String toStringHelper(TreeNode<E> node, int numTabs, String ultimate){
		if (node!= null){
			ultimate = toStringHelper(node.rightChild, numTabs+1, ultimate);
			ultimate += spaceMaker(numTabs)+ node.element + "\n";
			ultimate = toStringHelper(node.leftChild, numTabs+1, ultimate);
		}
		return ultimate;
	}	
}
