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
* A negative index accesses items from the end of the list. The last item of any non-empty list is always `a_list[-1]`
* If the negative index is confusing to you, think of it this way: `a_list[-n] == a_list[len(a_list) - n]`
```
myList = [2, 4, 6]
four = myList[1]

nestedlist = ["Happy", [1, 3, 5]]
y = nestedList[0][4]  # first element is string & slicing string
five = nestedList[1][2]

myList = [2, 4, 6]
six = myList[-1]
```

## Slicing list
* returned value is a new list containing all the items of the list, in order, starting with the first slice index, up to but not including the second slice index
* you can think of it this way: reading the list from left to right, the first slice index specifies the first item you want, and the second slice index specifies the first item you don’t want. The return value is everything in between
* if the left slice index is 0, you can leave it out, and 0 is implied
* similarly, if the right slice index is the length of the list, you can leave it out
* if both slice indices are left out, all items of the list are included. But this is not the same as the original a_list variable. It is a new list that happens to have all the same items. `a_list[:]` is shorthand for making a complete copy of a list.
```
myList = [1, 2, 3, 4, 5, 6, 7, 8]

sliced = myList[2:5]  # 3rd to 5th
sliced = myList[:-5]  # first to 3rd (last element is -1, count backward)
sliced = myList[4:]   # 5th to rest
sliced = myList[0:4]  # first to 3rd (don't use [:4] becase explicit is better than implicit)
```

## Adding items to list
* `+` : concatinates & creates new list (two-step process, can consume a lot of memory when you’re dealing with large lists)
* `append()`: method adds a single item to the end of the list.
* `extend()`: appends items of given list to original list
* `insert()`: inserts a single item at specified index (items after given index have their positions bumped up to make room)
```
tempList = [1, 2]

myList = tempList + [3, 4]  # [1, 2, 3, 4]

myList.append(5)            # [1, 2, 3, 4, 5]

myList.extend([6, 7])       # [1, 2, 3, 4, 5, 6, 7]

myList.insert(0, 8)         # [8, 1, 2, 3, 4, 5, 6, 7]

```

## Altering list item
```
myList = [0, 0, 0, 0, 5]

myList[0] = 1            # [1, 0, 0, 0, 5]

myList[1:4] = [2, 3, 4]  # [1, 2, 3, 4, 5]

```

## Removing item
* `del`: removes single/range of items. All items after the deleted item shift their positional index to “fill the gap”
* `remove()`: takes a value and removes the first occurrence of that value from the list (positions will be shifted)
* `remove()` will raise an exception if you try to remove a value that isn’t in the list
* `pop()/pop(index)`: removes item at index or last item(no argument) & returns removed value (positions will be shifted)
* `pop()` on an empty list raises an exception.
```
myList = [1, 0, 3, 4, 5, 6, 7]
del [1]     # [1, 3, 4 , 5, 6, 7]
del [0:2]   # [5, 6, 7]
del myList  # deleted entire list

myList = [1, 2, 0, 3, 4, 5]
myList.remove(0)    # [1, 2, 3, 4, 5]
two = myList.pop(1) # [1, 3, 4, 5]
five = myList.pop() # [1, 3, 4]
myList.clear()      # clear
```
