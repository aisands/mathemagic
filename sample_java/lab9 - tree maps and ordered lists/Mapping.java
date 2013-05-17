package lab9;

public class Mapping<K extends Comparable<K>, V> implements Comparable<Mapping<K,V>>{
	K key;
	V value;
	
	public Mapping(K key, V value){
		this.key= key;
		this.value = value;
	}
	
	public int compareTo(Mapping<K, V> mapping) {
		return this.key.compareTo(mapping.key);
	}
	
	public String toString(){
		return "(" + key + "," + value + ")";
	}
}
