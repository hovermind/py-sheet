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
