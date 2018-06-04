* unordered collection of key-value pair
* keys must be unique and immutable

## Creating dictionary
```
my_dict = {}

my_dict = {1: 'apple', 2: 'ball'}

my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = dict({1:'apple', 2:'ball'})

my_dict = dict([(1,'apple'), (2,'ball')])
```
Dictionary Comprehension
```
squares = {x: x*x for x in range(6)}                    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# above is equivalent to below
squares = {}
for x in range(6):
   squares[x] = x*x
   
odd_squares = {x: x*x for x in range(11) if x%2 == 1}  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

## Accessing element
`dict['key']` : `KeyError` if key does not exist    
`dict.get('key')` : returns `None` if key does not exist
```
my_dict = {'name':'Jack', 'age': 26}

print(my_dict['name'])       # jack
print(my_dict.get('age'))    # 26
```

## Itereting
Using for loop, we can iterate though each key in a dictionary
```
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
```

## Membership test
For keys only, not for values
```
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in squares)     # True

print(2 not in squares) # True

print(49 in squares)    # False (membership tests for key only not value)
```

## Add update element
```
my_dict = {'name':'Jack', 'age': 26}

my_dict['age'] = 27                 # {'name':'Jack', 'age': 27}

my_dict['address'] = 'Downtown'     # {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
```

## Remove delete element
`pop(key)` : removes & returns    
`popitem()` : random element    
`clear()` : removes all items    
`del ` : single element or entire dict
```
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

sixteen = squares.pop(4)    # 16

squares.popitem()           # an arbitrary item

squares.clear()

del squares[5]  
del squares
```

## Methods
`len(dict)` : Return the length (the number of items) in the dictionary    
`sorted(dict)` : eturn a new sorted list of keys in the dictionary    
## See : [python dictionary methods](https://www.programiz.com/python-programming/methods/dictionary/)
