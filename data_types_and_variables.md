## Variable
* other languages have variables, python has names
* there is no keyword to declare variables in python
* True, False and None are uppercase, all other keywords in lowercase
* python is case sensitive

```
x = 2
name = "hassan"

name: str
name: str = "hassan"
x: int = 222
primes: List[int] = []
stats: Dict[str, int] = {}

foo = None    # ~ perl undef
```
**Note**    
It acts like dynamically typed, but it is statically typed behind the scene.Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

## Data types
* **Numbers** can be integers (1 and 2), floats (1.1 and 1.2), fractions (1/2 and 2/3), or even complex numbers
* **Booleans** are either True or False
* **Strings** are sequences of Unicode characters, e.g. an html document
* **Bytes** and **byte arrays** (e.g. a jpeg image file)
* **Lists** are ordered sequences of values
* **Tuples** are ordered, immutable sequences of values
* **Sets** are unordered bags of values
* **Dictionaries** are unordered bags of key-value pairs

## Numbers
* Integers are signed can be of any length, it is only limited by the memory available
* A floating point number is accurate up to 15 decimal places
* There’s no type declaration to distinguish int and float. Python apart them by the presence or absence of a decimal point
* Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part
```
a = 10      // Signed Integer
a = 3.1416  // (.) Floating point real values
a = 1 + 2j  // (J) Contains integer in the range 0 to 255.
```

## Boolean
* Python booleans are truth-like/false-like
* Expressions can also evaluate to a boolean value
* Different datatypes have different rules about which values are true or false in a boolean context (i.e. if statement)
* Python has two constants, cleverly named True and False
* Don't treat True as 1, False as 0
```
x = 10
if x > 5:
    ... ...
```

## str
* Python uses single quotes `'` double quotes `"` and triple quotes `"""` to denote literal strings
* Multi-line strings can be denoted using triple quotes, `'''` or `"""`
```
message = "hello world"

name: str
name = "hassan"

name: str = "hassan"
```

See:    
* [tuple](#)     
* [list](#)
* [set](#)
* [dict](#)
