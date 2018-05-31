## Literals
#### no literal suffix
```
name = "hassan"       # string literal
id = 222              # int literal
isOk = True           # boolean literal
```
#### literal prefix
* 0b - binary
* 0o - octal
* 0x - hex
```
binVal = 0b11011110
hexVal = 0xDE
octVal = 0o336
```

## Constant
There is no const keyword to declare constant in python. just declare it & don't reassign: `PI = 3.1426`

**hack:** `const.py`
```
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
**Use in your class:**
```
class MyConst(__Const):
    PI = 3.1416

print(MyConst.PI) # will print 3.1416

MyConst.PI = 3.14 # will raise TypeError
```

