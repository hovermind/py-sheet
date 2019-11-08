## Dataclass
* `@dataclass`: is known as decorator (This decorator is really just a code generator)
* similar to kotlin data class

## Dataclass deinition

**Sample 1**
```python
from dataclasses import dataclass
from src import DataFormat


@dataclass
class Info():
    project_name: str
    data_format: DataFormat
```

**Sample 2**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)

print(p)  # Point(x=1.5, y=2.5, z=0.0)
```

**More:**
 *https://docs.python.org/3/library/dataclasses.html
* https://realpython.com/python-data-classes/
* https://stackoverflow.com/a/45426493/4802664
* https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes

## Using dataclass
```python

```

## Data class getter setter
https://stackoverflow.com/questions/51079503/python-dataclass-and-property-decorator
