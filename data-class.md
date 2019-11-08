## Dataclass
* `@dataclass`: is known as decorator (This decorator is really just a code generator)
* similar to kotlin data class
* `@dataclass` generates all the boiler plate codes and some extra code behind the scene (you have to do it manually for normal class)
**Links:**
* https://blog.florimond.dev/reconciling-dataclasses-and-properties-in-python
* https://docs.python.org/3/library/dataclasses.html
* https://realpython.com/python-data-classes/
* https://stackoverflow.com/a/45426493/4802664
* https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes

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

## Using dataclass
```python
# with arguments
info = Info("project_1", DataFormat.A)
info = Info(project_name: "project_1", data_format: DataFormat.A)

# without arguments
into = Info()
into.project_name = "project_1"
into.data_format = DataFormat.A
```

## Post init
* Dataclasses generate the __init__() method for you — and that's great. They even provide a __post_init__() hook method in case you want to do some more initialization (see Post-init processing)
* since we have no control over `__init__`, (auto generated), `__post_init__` is given and `__post_init__` will be called by `__init__`
```python
from dataclasses import dataclass
from src import DataFormat


@dataclass
class Info():
    project_name: str
    data_format: DataFormat
    
    def __post_init__(self):
        # this will be called by __init__ (at the end of __init__)
```

**if you use `InitVar` (`foo: InitVar[int]`), that field will be passed to `__post_init__` as an argument**
```python
from dataclasses import dataclass
from src import DataFormat


@dataclass
class Info():
    foo: InitVar[int]
    project_name: str
    data_format: DataFormat
    
    def __post_init__(self, foo: int):
        # this will be called by __init__ (at the end of __init__)
```

## Data class getter setter
https://stackoverflow.com/questions/51079503/python-dataclass-and-property-decorator
