﻿# Merging Two Packages

Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function `get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`. Your function should return a tuple `(i, j)` of the indices of the item weights, ordered such that `i > j`. If such a pair doesn’t exist, return an empty tuple.

Your solution should run in linear time.

Example:
```
input: arr = [4, 6, 10, 15, 16], limit = 21
output: (3, 1)   # since these are the indices of weights 6 and 15 whose sum equals 21
```

## Hints
 
* A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. Can we use a hash table in order to implement a solution with a better runtime?
* Think about what we can store in the hash table in order to help us to solve this problem more efficiently. 
* What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key? 
* If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!

## run unit tests

*  https://docs.python.org/3/library/unittest.html#command-line-interface