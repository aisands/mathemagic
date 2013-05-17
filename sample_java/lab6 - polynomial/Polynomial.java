package lab6;
/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 10/12/10
 * Polynomial.java
 * CSE 131 Lab 6
 */

import java.util.Iterator;
import java.util.LinkedList;

import lab1.ProcessorTool;
import lab5.CloningTool;
import lab5.EyeballTool;

import nip.GraphicsPanel;
import nip.NIP;

public class Polynomial {
	private LinkedList<Double> list;
	//GraphicsPanel panel;

	/**
	 * Constructs a Polynomial with no terms yet, denoted as 0). 
	 */
	public Polynomial() {
		list = new LinkedList<Double>();
	}

	
	/**
	 * 
	 * @param coeff is the coefficient of the next powered x term in the polynomial
	 * @return a new list describing the polynomial with the added term
	 */
	public Polynomial addTerm(double coeff) {
		list.add(coeff);		
		return this;  // required by lab spec
	}

	/**
	 * I am initially returning a random double so that
	 *    almost all assertEquals will fail on this method
	 *    until it is implemented.  Be sure to implement this
	 *    method recursively as specified in the lab documentation.
	 * @param x is the x value at which we are evaluating
	 * @return the evaluation of this polynomial at x
	 */
	
	
	public double evaluate(double x) {
		Iterator<Double> it = list.iterator();
		return evaluateHelper(x, it);
	}

	private double evaluateHelper(double x, Iterator<Double> it){
		if(it.hasNext()){
			return it.next() + x*evaluateHelper(x, it);
		}
		else {
			return 0;
		}
	}

	/**
	 * This method does return a new Polynomial that is the
	 *    derivative of the current one.
	 * @return a new Polynomial that is the derivative of this one
	 */
	
	public Polynomial derivative() {
		Polynomial derivative = new Polynomial();
		int exp = 0; //exponent of the x term corresponding to our place in the list during the while loop
		Iterator<Double> it = list.iterator();
		while (it.hasNext()){
			double coeff = it.next();
			if (exp > 0){
				derivative.addTerm(coeff*exp);
			}
			exp++;
		}
		return derivative;
	}

	/**
	 * Compute the sum of this and the other Polynomial, returning
	 *    a new Polynomial that represents that sum.
	 * @return a new Polynomial that is the some of this and another
	 */
	public Polynomial sum(Polynomial another){
		Iterator<Double> it1 = this.list.iterator();
		Iterator<Double> it2 = another.list.iterator();
		Polynomial sum = new Polynomial();
		int coefficient = 0;
		int size = this.list.size();
		int sizeAnother= another.list.size();
		int max;
		while (it1.hasNext() && it2.hasNext()){ //while both polynomials have another higher powered term
			sum.addTerm(it1.next()+it2.next()); //add the coefficients together
			coefficient++;
		}
		max = Math.max(size, sizeAnother);
		while (coefficient <= max-1){ //while x term corresponding to our place on the list is less than the highest powered x term
			if (max == size){ //the polynomial corresponding "this" contains the highest powered x term, add the terms of "this" to our sum
				sum.addTerm(this.list.get(coefficient));
			}
			else{
				sum.addTerm(another.list.get(coefficient)); //the polynomial corresponding to "another" contains the highest powered x term, add the terms of "another" to our sum
			}
			coefficient++;
		}
		return sum;
	}
	
	/**
	 * Creates a printout of the polynomial corresponding to "it" list
	 */
	public String toString() {
		Iterator<Double> it = list.iterator();
		int counter = 0;
		String s = "";
		if (!it.hasNext()){ //if the list is empty
			return "equal to 0";
		}
		else{
			while (it.hasNext()){
				if (counter == 0) { //for the constant term
					s = it.next()+ "";
				}
				else{
					s = s + " + " + it.next() + "x^" + counter; //for coefficients of non-trivial powers of x
				}
				counter++;
			}
			return "equal to " + s;
		}
	}





	/**
	 * This is the "equals" method that is called by
	 *    assertEquals(...) from your JUnit test code.
	 *    It must be prepared to compare this Polynomial
	 *    with any other kind of Object (obj).  Eclipse
	 *    automatically generated the code for this method,
	 *    after I told it to use the contained list as the basis
	 *    of equality testing.  I have annotated the code to show
	 *    what is going on.
	 */

	public boolean equals(Object obj) {
		// If the two objects are exactly the same object,
		//    we are required to return true.  The == operator
		//    tests whether they are exactly the same object.
		if (this == obj)
			return true;
		// "this" object cannot be null (or we would have
		//    experienced a null-pointer exception by now), but
		//    obj can be null.  We are required to say the two
		//    objects are not the same if obj is null.
		if (obj == null)
			return false;

		//  The two objects must be Polynomials (or better) to
		//     allow meaningful comparison.
		if (!(obj instanceof Polynomial))
			return false;

		// View the obj reference now as the Polynomial we know
		//   it to be.  This works even if obj is a BetterPolynomial.
		Polynomial other = (Polynomial) obj;

		//
		// If we get here, we have two Polynomial objects,
		//   this and other,
		//   and neither is null.  Eclipse generated code
		//   to make sure that the Polynomial's list references
		//   are non-null, but we can prove they are not null
		//   because the constructor sets them to some object.
		//   I cleaned up that code to make this read better.


		// A LinkedList object is programmed to compare itself
		//   against any other LinkedList object by checking
		//   that the elements in each list agree.

		return this.list.equals(other.list);
	}

	/**
	 * This is needed only for the BetterPolynomial extension.
	 * But you can also use it within this class if you find it
	 * handy.
	 * @return an iterator over the contained LinkedList's elements
	 */
	protected Iterator<Double> getIterator() {
		return list.iterator();
	}
	
//	public static void main(String[] args){
//		NIP nip = new NIP(200, 200, 3);
//		nip.setTool(new PolynomialTool()); 
//		
//	}

}
