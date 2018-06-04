* Tuples are immutable, which means their values at the indices cannot be changed, unless there is a value swap
* The array index range is from 0 to size minus 1. Negative indices start at the end of the array and work backwards
* Tuples can be combined using the addition operator
* When declaring a tuple, the parentheses are optional

## Creating tuple
```
# empty tuple
my_tuple = ()

# tuple having integers
my_tuple = (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
```
## Tuple with one element
Creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.
```
my_tuple = ("hello",)  # not ("hello")
```

## Accessing tuple elements
```
tuple_name = (item1, item2, item3)
val = tuple_name[index]  #accessing item at index

cities = ("Toronto", "Tokyo", "London", "Sydney")
tokyo = cities[1]

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])  # 's'
print(n_tuple[1][1])  # 4

my_tuple = ('p','e','r','m','i','t')
print(my_tuple[-1])  # 't'
```

## Iterating through a tuple
```
for name in ('John','Kate'):
     print("Hello",name) 
```

## Tuple membership test
```
my_tuple = ('a','p','p','l','e',)
print('a' in my_tuple)  # True
print('g' not in my_tuple)  # True
```

## Unpacking tuple
```
my_tuple = (3, 4.6, "dog")

a, b, c = my_tuple
print(a)  # 3
print(b)  # 4.6
print(c)  # "dog"
```

## Slicing
```
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[1:4])  # elements 2nd to 4th ('r', 'o', 'g')
print(my_tuple[:-7])  # ('p', 'r')
print(my_tuple[7:])   # ('i', 'z')
```

## Changing tuple
tuples are immutable
```
my_tuple = (4, 2, 3, [6, 5])  
my_tuple[1] = 9  # TypeError: 'tuple' object does not support item assignment
```
If the element is itself a mutable datatype like list, its nested items can be changed
```
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9  # (4, 2, 3, [9, 5])
```
concatenation: +    
repeat the elements in a tuple for a given number of times: *
```
print((1, 2, 3) + (4, 5, 6))  # (1, 2, 3, 4, 5, 6)

print(("Repeat",) * 3)  # ('Repeat', 'Repeat', 'Repeat')
```
**Both + and * operations result into a new tuple**

## Deleting a Tuple
cannot delete or remove items from a tuple but deleting a tuple entirely is possible
```
my_tuple = (1, 2, 3, 4)
del my_tuple
my_tuple  # NameError: name 'my_tuple' is not defined
```
## Tuple methods
`count(x)` :	Return the number of items that is equal to x    
`index(x)` :	Return index of first item that is equal to x
```
my_tuple = ('a','p','p','l','e',)
print(my_tuple.count('p'))  # 2
print(my_tuple.index('l'))  # 3
```
