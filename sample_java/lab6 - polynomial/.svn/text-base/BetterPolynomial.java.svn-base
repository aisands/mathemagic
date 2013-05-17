package lab6;

import java.util.Iterator;

public class BetterPolynomial extends Polynomial {
	
	// DO NOT redefine the LinkedList here!
	// DO NOT change the access of the LinkedList in Polynomial!
	// It is available privately in Polynomial, but
	//   you do not have direct access to it here.
	// You are therefore forced to compute the product
	//   using methods you already have available from
	//   Polynomial, but NOT access to the list contained therein
	
	/**
	 * Java generates the following constructor automatically,
	 * but I'll put it in here in case you worry about it being
	 * missing.  A BetterPolynomial is made by having Polynomial
	 * do its usual work. Nothing extra is needed for the extension.
	 */
	public BetterPolynomial() {
		super();
	}
	
	
	/**
	 * Copies a Polynomial as a BetterPolynomial. The better
	 *   one can do everything a Polynomial can, as well as perform
	 *   the product method.
	 * @param p A Polynomial
	 */
	public BetterPolynomial(Polynomial p) {
		super();
		Iterator<Double> i = p.getIterator();
		while (i.hasNext()) {
			double d = i.next();
			addTerm(d);
		}
	}

	
	public BetterPolynomial product(BetterPolynomial another) {
		Iterator<Double> it1 = this.getIterator();
		Polynomial holder = new BetterPolynomial();
		BetterPolynomial temp = new BetterPolynomial();	
		int exp = 0;
			while (it1.hasNext()) {
				Double term1 = it1.next();
				Iterator<Double> it2 = another.getIterator();
				
				for(int i = 0; i < exp; i++){
					temp.addTerm(0);
				}
				
				while (it2.hasNext()){
					Double term2 = it2.next();
					temp.addTerm(term1*term2);
				}
				
				holder = holder.sum(temp);
				temp = new BetterPolynomial();
				
				exp++;
			}
			
		return new BetterPolynomial(holder);
	}

}
