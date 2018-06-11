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
