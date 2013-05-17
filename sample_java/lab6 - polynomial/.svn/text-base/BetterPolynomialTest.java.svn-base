package lab6;

import static org.junit.Assert.*;
import org.junit.Test;

public class BetterPolynomialTest {
	@Test
	public void testProduct(){
		BetterPolynomial p =  new BetterPolynomial();
		BetterPolynomial q =  new BetterPolynomial();
		BetterPolynomial r =  new BetterPolynomial();
		BetterPolynomial s = new BetterPolynomial();
		BetterPolynomial t = new BetterPolynomial();
	
		p.addTerm(1).addTerm(2).addTerm(1);
		q.addTerm(-1).addTerm(1).addTerm(2);
		
		s= p.product(q);
		BetterPolynomial u = t.product(q);
		
		r.addTerm(-1).addTerm(-1).addTerm(3).addTerm(5).addTerm(2);
		assertEquals(u, new BetterPolynomial());
		assertEquals(r, s);
		assertEquals(p.product(p), new BetterPolynomial().addTerm(1).addTerm(4).addTerm(6).addTerm(4).addTerm(1));
		
		
	}

}
