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
