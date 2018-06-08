* `try...except` blocks to handle exceptions
* `raise` statement to generate them
```
try:

   # code
   
except ExceptionClass:

   # code
   
# raising exception
if size < 0:
    raise ValueError('number must be non-negative')
```
Exceptions are implemented as classes, and this raise statement is actually creating an instance of the class 
and passing the string 'message' to its initialization method

Exception class example:
* `ImportError`
* `ValueError`
* `NameError` (using undefined variable)

## Catching import error
```
try:
  import chardet
except ImportError:
  chardet = None

if chardet:
  # do something
else:
  # continue anyway
```
When two modules implement a common api
```
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
```
