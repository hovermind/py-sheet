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

## Accessing element
`dict['key']` : `KeyError` if key does not exist    
`dict.get('key')` : returns `None` if key does not exist
```
my_dict = {'name':'Jack', 'age': 26}

print(my_dict['name'])       # jack
print(my_dict.get('age'))    # 26
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
