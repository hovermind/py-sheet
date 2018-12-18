# TOC
* [Array in python](/array.md#array-in-python)
* [Initializing array](/array.md#initializing-array)
* [Accessing array element](/array.md#accessing-array-element)
* [Adding element](/array.md#adding-element)
* [Deleting element](/array.md#deleting-element)
* [Slicing array](/array.md#slicing-array)
* [Misc](/array.md#misc)

## Array in python
* a thin wrapper on C arrays
* use the arrays module only if you really need it (i.e. to interface with C code ), in all other cases stick with lists

## Initializing array
* `array.array(typecode[, initializer])`
* See [type code](https://docs.python.org/3/library/array.html#module-array)
```python
from array import array

myArray = arr.array('d', [1.1, 3.5, 4.5])
myArray = array.array('i')                      # array.array(typecode)
myArray = array.array('i', [0, 1, 2])           # array.array(typecode, initializer)
myArray = array.array('i', range(5))            # array.array(typecode, initializer)
myArray = array.array('i', range(start, end))   # array.array(typecode, initializer)
```

## Accessing array element
**index starts from 0**
```
import array as arr
a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second last element:", a[-1])
```

## Adding element
```
import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 0    
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

numbers.append(4)
numbers.extend([5, 6, 7]) 
```

## Deleting element
```
import array as arr

number = arr.array('i', [1, 2, 3, 3, 4])

del number[2] # removing third element
print(number) # Output: array('i', [1, 2, 3, 4])

del number # deleting entire array
print(number) # Error: array is not defined

numbers.remove(x)
n = numbers.pop(index)
```

## Slicing array
You can access a range of items in an array by using the slicing operator `:`
```
import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end
```

## Misc
* you can concatenate two arrays using + operator
* you can divide an array by n, and each number in the array will be divided by n

**When to use arrays?**
Lists are much more flexible than arrays. They can store elements of different data types including string. Also, lists are faster than arrays. And, if you need to do mathematical computation on arrays and matrices, you are much better off using something like NumPy library.




