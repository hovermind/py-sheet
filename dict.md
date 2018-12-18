# TOC
* [Python dictionary](#Python-dictionary)
* [Creating dictionary](#Creating-dictionary)
* [Accessing element](#Accessing-element)
* [Itereting](#Itereting)
* [Membership test](#Membership-test)
* [Add update element](#Add-update-element)
* [Remove element](#Remove-element)
* [Operators on dictionary](#Operators-on-dictionary)
* [Dictionary methods](#Dictionary-methods)

## Python dictionary
* unordered collection of key-value pair
* keys must be unique and immutable
```
my_dict1 = {}                                            # empty dictionary
my_dict2 = {1: 'apple', 2: 'ball'}                       # dictionary with integer keys
my_dict3 = {'name': 'John', 1: [2, 4, 3]}                # dictionary with mixed keys
```

## Creating dictionary
```
my_dict = {}

my_dict = {1: 'apple', 2: 'ball'}

my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = dict({1:'apple', 2:'ball'})

my_dict = dict([(1,'apple'), (2,'ball')])  # from list of tuples
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
    
for i in squares.keys():
    print(squares[i])

my_dict = {1 : "one", 2 : "two", 3 : "three"}
for key, val in my_dict.items():
  print(f"{key} => {val}")
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

## Remove element
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

## Operators on dictionary
```
len(my_dict)                      # returns the number of stored entries, i.e. the number of (key,value) pairs.
del my_dict[k]                    # deletes the key k together with his value
k in my_dict                      # True, if a key k exists in the dictionary my_dict
k not in my_dict                  # True, if a key k doesn't exist in the dictionary my_dict

del my_dict[k]          # delete a particular item
my_dict.clear()         # remove all items
del my_dict             # delete the dictionary itself
```

## Dictionary methods
* len(dict) : Return the length (the number of items) in the dictionary    
* sorted(dict) : eturn a new sorted list of keys in the dictionary
* clear() : Remove all items form the dictionary
* copy() : Return a shallow copy of the dictionary
* fromkeys(seq[, v]) : Return a new dictionary with keys from seq and value equal to v (defaults to None)
* get(key[,d]) : Return the value of key. If key doesnot exit, return d (defaults to None)
* items() : Return a new view of the dictionary's items (key, value)
* keys() : Return a new view of the dictionary's keys
* pop(key[,d]) : Remove the item with key and return its value or d if key is not found
* popitem() : Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty
* setdefault(key[,d]) : If key is in the dictionary, return its value. If not, insert key with a value of d and return d
* update([other]) : Update the dictionary with the key/value pairs from other, overwriting existing keys
* values() : Return a new view of the dictionary's values
## See : [python dictionary methods](https://www.programiz.com/python-programming/methods/dictionary/)
