package lab9;

/**
 * A simple interface for a Map ADT.
 * Read this file carefully, but do NOT modify this file.
 * @author Kenneth J. Goldman
 * @version 1.0
 */
public interface Map<K,V> {

	/**
	 * Puts the given key into the map and associates with it the given value.
     * If the key is already in the mapping, its associated value
     * is replaced by the given one. 
     * (No duplicate keys are allowed.)
	 * @param key - the key to be put into the map
	 * @param value - the value to be associated with the key
	 */
	public void put(K key, V value);
  
	/**
	 * Gets the value associated with the given key.
     * If the key is not in the map,
     * a NoSuchElementException is thrown.
	 * @param key - the key to look up
	 * @return the value associated with the given key
	 */
	public V get(K key);

	/**
	 * Determines if a given key is in the map.
	 * @param key
	 * @return true if the given key is a key in the map
	 */
	public boolean contains(K key);
	
	/**
	 * Removes the given key from the map.
	 * If the key is not in the map, this method does not
	 * modify the map and returns false.
	 * @param domainElt
	 * @return true if the given key was removed.
	 */
	public boolean remove(K key);


	/**
	 * Returns a nicely formatted String representation of the Mapping.
     * For testing purposes in this lab, this string should reflect
     * the internal representatin of the mapping.
     */
	public String toString();
}
