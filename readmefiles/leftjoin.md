# lab-33:Implement a simplified LEFT JOIN for 2 Hashmaps.



## problem domain:

Write a function that LEFT JOINs two hashmaps into a single data structure

## Approach:
The left join function iterates through the keys of the first hashmap (synonyms) and performs a constant time check for each key's existence in the second hashmap (antonyms). Based on the result, it appends the appropriate values (synonym and antonym) to the result data structure. This ensures that the left join logic is followed, returning all keys and their corresponding values from the first hashmap, along with the associated antonyms from the second hashmap if present.

## Big O notation

Time Complexity: O(n), where n is the number of key-value pairs in the first hashmap.

Space Complexity: O(n), as the result data structure contains n tuples, where n is the number of key-value pairs in the first hashmap.




## White board
![hashmap-left-join](../images/33.jpg)
## Run in terminal
![run28](../images/c33.png)

## The implementation code and tests
__Code__
[code33](../scripts//leftjoin.py)

__Test__
[test33](../tests/test_leftjoin.py)