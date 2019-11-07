#### Python does not have c-like structure.

# TOC
* [Class as structure](#Class-as-structure)
* [Named tuple as structure](#Named-tuple-as-structure)
* [Improved NamedTuple](#Improved-NamedTuple)
* [Data Classes](#Data-Classes)

## Class as structure
An empty class definition can ack like structure:
```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

## Named tuple as structure
```python
from collections import namedtuple

MyStruct = namedtuple("MyStruct", "field1 field2 field3")

my_struct = MyStruct(field1="foo", field2="bar", field3="baz")
```

**Note:** Tuple is immutable

## Improved NamedTuple
Since Python 3.6 it became quite simple and beautiful as long as you can live with immutability
```python
from typing import NamedTuple

class MyStruct(NamedTuple):
    foo: str
    bar int
    baz: list
    qux: User

my_item = MyStruct('foo', 0, ['baz'], User('peter'))

print(my_item)    # MyStruct(foo='foo', bar=0, baz=['baz'], qux=User(name='peter'))
```

## Data Classes
With the introduction of Data Classes in Python 3.7 we get very close to structure. 
The following example is similar to the NamedTuple, but the resulting object is mutable and it allows for default values

**See:** [Data Class](/data-class.md)
