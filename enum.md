## Python enum
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
* member values can be anything: `int`, `str`
* even though we use the class syntax to create Enums, Enums are not normal Python classes
* two enum members with the same name is invalid, but two members can have same value (to ensure unique enumeration values: `from enum import Enum, unique`)
* info about enum with `repr `
```python
print(repr(Color.RED))    # Color.RED: 1
```

[Alternative syntax](https://stackoverflow.com/a/1695250/4802664)
```python
from enum import Enum 

Animal = Enum('Animal', 'cat dog')

Animal.cat       # returns <Animal.ant: 1>
Animal['cat']    # returns <Animal.cat: 1> (string lookup)
Animal.cat.name  # returns 'cat' (inverse lookup)
```

## Using automatic values
```python
from enum import Enum, auto
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

list(Color)    # [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
```

## Accessing enum member
* by name: `Color['RED']`
* by value: `Color(1)`

## Enum member name and value
```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# member name
print(Color.RED.name)    # RED

# member value
print(Color.RED.value)    # 1
```

## Iterating over enum members
```python
class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3
	
for shake in Shake:
    print(shake)

# output
# Shake.VANILLA
# Shake.CHOCOLATE
# Shake.COOKIES
# Shake.MINT
```

**See:** [Python enum details](https://docs.python.org/3/library/enum.html)
