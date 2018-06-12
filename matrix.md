## What is matrix
A matrix is a two-dimensional data structure (row x column) in which all rows (nested items) have same number of elements. In python, matrix is a nested list.    

**2-D matrix**
```
A = [[80, 75, 85],
     [75, 80, 99],
     [79, 91, 87]]
```
**Nested list but not a matrix**
```
B = [[80, 75, 85],
     [75, 80, 99],
     [79, 91]]
```
`A` is a matrix as well as nested list where as `B` is a nested list but not a matrix because 3rd item in `B` has fewer elements than other two.

## Creating matrix
```
n = 3
m = 4

a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)

[[0 0 0 0], 
 [0 0 0 0], 
 [0 0 0 0]]

# using numpy
from numpy import * 
x = range(16)
x = reshape(x,(4,4)) 
print(x)

[[0 1 2 3], 
 [4 5 6 7], 
 [8 9 10 11], 
 [12 13 14 15]]
```

## Accessing elements
Same as accessing list. Negative indexing allowed.

## Slicing
Slicing is done using colon(:) with a syntax (`start:end:increment`) but for matrix we have to do it using numpy library.
```
from numpy import *
a = array([[1, 'Hassan', 28, 'Tokyo'],
           [2, 'John', 55, 'London'],
           [3, 'Dave', 62, 'Toronto']])

print(a[0:2, [0, 1, 3]])  # [0, 1, 3] => indicates columns

[['1' 'Hassan' 'Tokyo']
 ['2' 'John' 'London']]
```

## Change or add elements
Same as list
```
a = [[1, 'Hassan', 28, 'Tokyo'],
     [2, 'John', 55, 'London'],
     [3, 'Dave', 62, 'Toronto']]

hassan_row = a[0]
print(hassan_row)   # [1, 'Hassan', 28, 'Tokyo']

hassan_row[3] = "Osaka"
print(hassan_row)   # [1, 'Hassan', 28, 'Osaka']
```
**numpy methods**    
`append()` => single row    
```
from numpy import *
a = [[1, 'Hassan', 28, 'Tokyo'],
     [2, 'John', 55, 'London'],
     [3, 'Dave', 62, 'Toronto']]

a = append(a, [[4, 'Jim', 34, 'New York']], 3)
print(a)

[[1, 'Hassan', 28, 'Tokyo'],
 [2, 'John', 55, 'London'],
 [3, 'Dave', 62, 'Toronto'],
 [4, 'Jim', 34, 'New York']]
```
`insert()` => items    
`matrix = insert(matrix, [column_index], [[], [], []], axis = 0/1)  # axis 0 => row, axis 1 => column`
```
a = [[1, 'Hassan', 28, 'Tokyo'],
     [2, 'John', 55, 'London'],
     [3, 'Dave', 62, 'Toronto'],
     [4, 'Jim', 34, 'New York']]
     
a = insert(matrix, [4], [[5], [23], [35], [10]], axis = 1)
print(a)

 [[1, 'Hassan', 28, 'Tokyo', '5'],
  [2, 'John', 55, 'London', '23'],
  [3, 'Dave', 62, 'Toronto', '35'],
  [4, 'Jim', 34, 'New York', '10']]

```
