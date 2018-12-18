# TOC
* [Python set](#Python-set)
* [Creating set](#Creating-set)
* [Accessing element](#Accessing-element)
* [Iterating](#Iterating)
* [Membership test](#Membership-test)
* [Changing elements](#Changing-elements)
* [Removing element](#Removing-element)
* [Set operations](#Set-operations)
* [Set methods](#Set-methods)
* [Frozenset](#Frozenset)

## Python set
* unordered collection of items. items can be any types (mixed)
* set itself is mutable but items must be immutable
* mathematical set operations like union, intersection, symmetric difference etc can be performed
* cannot access or change an element of set using indexing or slicing
```
# set of integers
my_set = {1, 2, 3}

# set of mixed datatypes
my_set = {1.0, "A", (4, 5, 6)}
```

## Creating set
```
my_set = {1, 2, 3}
my_set = {1.0, "Hello", (1, 2, 3)}  # tuple is allowed since immutable

my_set = {1, 2, [3, 4]}             # TypeError: unhashable type: 'list'

my_set = {1, 2, 2, 3}               # {1, 2, 3} duplicates are adjusted automatically

# creating set from list (order not maintained)
my_list = [1, 2, 3, 3, 4]
my_set = set(my_list)               # {1, 2, 3, 4}
```

**Empty set**
```
my_set = {}     # dict not set

my_set = set()  # empty set
```

## Accessing element
Set is mutable but unordered -> indexing does not work
```
my_set = {1, 3, 4, 2}

my_set[0]  # TypeError: 'set' object does not support indexing
```

## Iterating
```
for item in my_set:
    print(item)
```

## Membership test
```
my_set = set("mikan")

print('a' in my_set)      # True
print('m' not in my_set)  # False
```

## Changing elements
`add()` : add single element    
`update()` : and multiple elements (tuples, lists, strings or other sets)
```
my_set = {1,3}

my_set.add(2)                     # {1, 2, 3}
my_set.update([4, 5])             # {1, 2, 3, 4, 5}
my_set.update([4, 5], {1, 1, 6})  # {1, 2, 3, 4, 5, 6}

```

## Removing element
`discard(x)` : no error if `x` does not exist    
`remove(x)` : error if `x` does not exist    
`pop()` : removes last element (random) and returns it    
`clear()` : removes all elements
```
my_set = {1, 3, 4, 5, 6}
my_set.discard(4)            # {1, 3, 5, 6}
my_set.remove(6)             # {1, 3, 5}

print(my_set.pop())          #  random element

my_set.clear()
print(my_set)                # empty set -> set()
```

## Set operations
Union : `|` or `union()`    
Intersection : `&` or `intersection()`    
Difference : `-` or `difference()`     
Symmetric Difference : `^` or `symmetric_difference()`
```
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = A | B               # {1, 2, 3, 4, 5, 6, 7, 8}
C = A.union(B)          # {1, 2, 3, 4, 5, 6, 7, 8}

C = A & B               # {4, 5}
C = A.intersection(B)   # {4, 5}

C = A - B               # {1, 2, 3}
C = A.difference(B)     # {1, 2, 3}

C = A ^ B                      # {1, 2, 3, 6, 7, 8}
C = A.symmetric_difference(B)  # {1, 2, 3, 6, 7, 8}
```

## Set methods
* len() : Return the length (the number of items) in the set.
* max() : Return the largest item in the set.
* min() : Return the smallest item in the set.
* sorted(): Return a new sorted list from elements in the set(does not sort the set itself).
* sum() : Retrun the sum of all elements in the set.

* add() : Add an element to a set
* clear() : Remove all elements form a set
* copy(): Return a shallow copy of a set
* difference(): Return the difference of two or more sets as a new set
* difference_update() : Remove all elements of another set from this set
* discard() : Remove an element from set if it is a member. (Do nothing if the element is not in set)
* intersection(): Return the intersection of two sets as a new set
* intersection_update()	: Update the set with the intersection of itself and another
* isdisjoint(): Return True if two sets have a null intersection
* issubset(): Return True if another set contains this set
* issuperset(): Return True if this set contains another set
* pop() : Remove and return an arbitary set element. Raise KeyError if the set is empty
* remove(): Remove an element from a set. If the element is not a member, raise a KeyError
* symmetric_difference()	: Return the symmetric difference of two sets as a new set
* symmetric_difference_update() : Update a set with the symmetric difference of itself and another
* union()	: Return the union of sets in a new set
* update()#Update a set with the union of itself and others

See: [python set methods](https://www.programiz.com/python-programming/methods/set/)

## Frozenset
While tuples are immutable lists, frozensets are immutable sets. Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.    

Frozensets can be created using the function frozenset()
```
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

A.add(3)           # AttributeError: 'frozenset' object has no attribute 'add'
A.isdisjoint(B)    # False
A.difference(B)    # frozenset({1, 2})
A | B              # frozenset({1, 2, 3, 4, 5, 6})
```
