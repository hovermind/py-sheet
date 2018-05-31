## Implicit casting
`int + float = float`    
Python coerces the int into a float to perform the addition, then returns a float as the result.

## Explicit casting
#### int - float
* `int(x [, base])`
* The `int()` function will truncate, not round
* The `int()` function truncates negative numbers towards 0. It’s a true truncate function, not a floor function
```
floatVal = float(5) # 5.0

intVal = int(5.5) # 5
```
#### str
```
myInt = 5
myFloat = 5.5
strInt = str(myInt)
strFloat = str(myFloat)

floatValue = float("5.5")
intValue = int("5")
```
**Note:** `int("5.5")` will be error, because `"5.5"` will be parsed to float. `int(float("5.5"))` is ok

#### complex
```
complex(real [,imag])  # Creates a complex number.
repr(x)                # Converts object x to an expression string.
eval(str)              # Evaluates a string and returns an object.
tuple(s)               # Converts s to a tuple.
list(s)                # onverts s to a list.
set(s)                 # Converts s to a set.
dict(d)                # Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s)           # Converts s to a frozen set.
chr(x)                 # Converts an integer to a character.
unichr(x)              # Converts an integer to a Unicode character.
ord(x)                 # Converts a single character to its integer value.
hex(x)                 # Converts an integer to a hexadecimal string.
oct(x)                 # Converts an integer to an octal string.
```

#### is
`==` operator is used to test if two variables are equal or not, `is` is used to test if the two variables refer to the same object.
```
[] == []            # True
[] is []            # False
{} == {}            # True
{} is {}            # False
```

#### as
`as` is used to create an alias while importing a module.
```
import math as myAlias

myAlias.cos(myAlias.pi)
```
