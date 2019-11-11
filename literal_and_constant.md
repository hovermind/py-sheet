# TOC
* [Literals](/literal_and_constant.md#literals)
* [Constant](/literal_and_constant.md#constant)

## Literals
* no literal suffix
* literal prefix:
    * 0b or 0B - binary
    * 0o or 0O - octal
    * 0x or 0X - hex
```python
name = "hassan"       # string literal
id = 222              # int literal
isOk = True           # boolean literal

binVal = 0b11011110
hexVal = 0xDE
octVal = 0o336
```

## Constant
There is no const keyword to declare constant in python. just declare it & don't reassign: `PI = 3.1426`

**hack:** `const.py`
```python
class __MetaConst(type):
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError

class __Const(object, metaclass = __MetaConst):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError
```
##### Use in your class:
```python
class MyConst(__Const):
    PI = 3.1416

print(MyConst.PI) # will print 3.1416

MyConst.PI = 3.14 # will raise TypeError
```

As of Python 3.8, there's a typing.Final variable annotation that will tell static type checkers (like mypy) that your variable shouldn't be reassigned. This is the closest equivalent to Java's final. However, it does not actually prevent reassignment:
```python
from typing import Final

a: Final = 1

# Executes fine, but mypy will report an error if you run mypy on this:
a = 2
```
See: https://stackoverflow.com/a/2682752
