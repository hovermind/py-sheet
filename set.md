* unordered collection of items. items can be any types (mixed)
* set itself is mutable but items must be immutable
* mathematical set operations like union, intersection, symmetric difference etc can be performed
* cannot access or change an element of set using indexing or slicing

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
See: [Python set methods](https://www.programiz.com/python-programming/methods/set/)
