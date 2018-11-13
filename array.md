# TOC


## Array in python
* The default built-in Python type is called a list, not an array. 
*It is an ordered container of arbitrary length that can hold a heterogenous collection of objects 
* (their types do not matter and can be freely mixed). This should not be confused with the array module, 
* which offers a type closer to the C array type; the contents must be homogenous (all of the same type), 
* but the length is still dynamic.
```python
arr = []      # arr refers to an empty list
```

**Notes:**
* Under the hood Python's list is a wrapper for a real array which contains references to items. 
* Also, underlying array is created with some extra space.
* Consequences of this are:
* - random access is really cheap (arr[6653] is same to arr[0])
* - append operation is 'for free' while some extra space
* - insert operation is expensive
* COMPLEXITY: https://wiki.python.org/moin/TimeComplexity

## Array length
```
arr = [1, 2, 3, 4, 5, 6]

length = len(arr)
```

## Append and insert
```python
arr = [1, 2, 3, 4, 5, 6]

arr.insert(6, 7)
arr.append(8)
```

## Initializing array
```python
# init with values (can contain mixed types)
arr = [1, "lol"]
arr = [1, 2, 3, 4, 5, 6]

# get item by index (can be negative to access end of array)
arr[0]  # 1
arr[-1] # 6

# there is a really cool way to cut arrays in python:
result = [1, 2, 3, 4, 5, 6, 7, 8, 9][1:-2]  # result => [2, 3, 4, 5, 6, 7]
```

## Using library to initialize
* `array.array(typecode[, initializer])`
* about typecode: https://docs.python.org/3/library/array.html
```python
from array import array

myArray = array.array('i')                      # array.array(typecode)
myArray = array.array('i', [0, 1, 2])           # array.array(typecode, initializer)
myArray = array.array('i', range(5))            # array.array(typecode, initializer)
myArray = array.array('i', range(start, end))   # array.array(typecode, initializer)
```

