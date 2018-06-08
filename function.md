* use `def` keyword
* doesn’t define a return datatype but aways returns a value (return statement or `None` if no return statement)
* no datatypes for arguments
* defualt value for arguments & named arguments are same as C# (named argument is last or all arguments are named)
* the docstring is available at runtime as an attribute of the function (IDE shows as tooltip)
```
def my_func(name, gender = "M"):
  '''
  Prints a person's name with Mr/Mrs depending on gender

  Keyword arguments:
  name -- name of the person
  gender -- gender of the person

  Returns: string
  '''

  prefix = ""
  if gender == "M":
    prefix = "Mr"
  else:
    prefix = "Mrs"
  return f"{prefix} {name}"
```

## Calling function
```
def my_func(name, gender = "M"):
  ...
  
my_func("Hassan")                       # valid, gender is "M"
my_func("Hassan", "M")                  # valid, all are positional arguments
my_func("Hassan", gneder = "M")         # valid, named argument at last
my_func(name = "Hassan", gneder = "M")  # valid, all arguments are named
my_func(name = "Hassan", "M")           # invalid, named argument can not precede positional argument
```

## Meta
Everything in Python is an object (in the sense that it can be assigned to a variable or passed as an argument to a function), and everything can have attributes and methods. Strings are objects. Lists are objects. Functions are objects. Classes are objects. Class instances are objects. Even modules are objects (you can pass an entire module as an argument to a function)   

A function, like everything else in Python, is an object. All functions have a built-in attribute __doc__, which returns the docstring defined in the function’s source code.
```
>>> print(my_module.my_func.__doc__)


Prints a person's name with Mr/Mrs depending on gender

Keyword arguments:
name -- name of the person
gender -- gender of the person

Return
```
In Python, functions are first-class objects. You can pass a function as an argument to another function.
