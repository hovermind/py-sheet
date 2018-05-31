* `[ , , ]` zero-based
* odered collection of items (retain their original order)
* can have any number of items and items can be of different types (python keeps track of the datatype internally)
* lists are mutable (value of elements of a list can be altered)
* A list can be used like a zero-based array
```
myList = [0, 1, 2, 3]
```

## Creating list
```
myList = [] # empty list

myList = [1, 2, 3] # list of integers

myList = [1, "Hello", 3.4] # list with mixed datatypes

myNestedList = [[], []] # nested/multidimentional list
```

## Accessing list item
* A negative index accesses items from the end of the list counting backwards. The last item of any non-empty list is always `a_list[-1]`
* If the negative index is confusing to you, think of it this way: `a_list[-n] == a_list[len(a_list) - n]`
```
myList = [2, 4, 6]
four = myList[1]

nestedlist = ["Happy", [1, 3, 5]]
y = nestedList[0][4]  // first element is string & slicing string
five = nestedList[1][2]

myList = [2, 4, 6]
six = myList[-1]
```
