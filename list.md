* `[ , , ]` zero-based
* odered collection of items (retain their original order)
* can have any number of items and items can be of different types (python keeps track of the datatype internally)
* lists are mutable (value of elements of a list can be altered)
```
myList = [0, 1, 2, 3]
```

**Notes:**    
* A list can be used like a zero-based array
* A negative index accesses items from the end of the list counting backwards. The last item of any non-empty list is always `a_list[-1]`
* If the negative index is confusing to you, think of it this way: `a_list[-n] == a_list[len(a_list) - n]`

## Creating list
```
myList = [] # empty list

myList = [1, 2, 3] # list of integers

myList = [1, "Hello", 3.4] # list with mixed datatypes

myNestedList = [[], []] # nested/multidimentional list
```
