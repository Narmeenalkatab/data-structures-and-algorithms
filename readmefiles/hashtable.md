# Implementation: Hash Tables

## problem
Implement a Hashtable Class with the following methods:
*set
*get
*key
*hash
*has


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach taken in this implementation is to use a hash table with separate chaining to handle collisions.


The __init__ method initializes the hash table with a fixed size of 100 and creates an array of None values to store the data.

The hash method calculates the hash value of a given key using a simple hash function, which sums up the ASCII values of each character in the key and then takes the modulo of the table size.

The set method inserts a new key-value pair into the hash table. If there is a collision (i.e., another key already hashed to the same index), it uses separate chaining to store the new pair in a linked list at that index.

The get method retrieves the value associated with a given key from the hash table.

The has method checks if a given key exists in the hash table.

The keys method returns a list of all the keys present in the hash table.The __init__ method initializes the hash table with a fixed size of 100 and creates an array of None values to store the data.

The hash method calculates the hash value of a given key using a simple hash function, which sums up the ASCII values of each character in the key and then takes the modulo of the table size.

The set method inserts a new key-value pair into the hash table. If there is a collision (i.e., another key already hashed to the same index), it uses separate chaining to store the new pair in a linked list at that index.

The get method retrieves the value associated with a given key from the hash table.

The has method checks if a given key exists in the hash table.

The keys method returns a list of all the keys present in the hash table.





**Big O**

The approach taken in this implementation is to use a hash table with separate chaining to handle collisions. Separate chaining means that when there is a collision (i.e., multiple keys hash to the same index), a linked list is used to store the key-value pairs at that index.

The __init__ method initializes the hash table with a fixed size of 100 and creates an array of None values to store the data.

The hash method calculates the hash value of a given key using a simple hash function, which sums up the ASCII values of each character in the key and then takes the modulo of the table size.

The set method inserts a new key-value pair into the hash table. If there is a collision (i.e., another key already hashed to the same index), it uses separate chaining to store the new pair in a linked list at that index.

The get method retrieves the value associated with a given key from the hash table.

The has method checks if a given key exists in the hash table.

The keys method returns a list of all the keys present in the hash table.

The Big O time complexity for this implementation is as follows:

hash method: O(k), where k is the length of the input key.
set method: O(k + m), where k is the length of the input key, and m is the average number of collisions (i.e., elements in the linked list at the hashed index).
get method: O(k + m), where k is the length of the input key, and m is the average number of collisions (i.e., elements in the linked list at the hashed index).
has method: O(k + m), where k is the length of the input key, and m is the average number of collisions (i.e., elements in the linked list at the hashed index).
keys method: O(n), where n is the number of elements (key-value pairs) in the hash table.


 Space complexity is O(n + t), where n is the number of elements


## Solution
<!-- Show how to run your code, and examples of it in action -->
pytest test_hashtable.py


[code](../scripts/hashtable.py)

[Test](../tests/test_hashtable.py)