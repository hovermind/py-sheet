# TOC
* [Try-catch](#)
* [Raising exception](#)
* [Catching import error](#)

## Try-catch
* `try...except` blocks to handle exceptions
* `raise` statement to generate them
```python
try:
   # code
except ExceptionClass:
   # code
```

## Raising exception
```python
if size < 0:
    raise ValueError('number must be non-negative')
```

Exceptions are implemented as classes, and this raise statement is actually creating an instance of the class 
and passing the string 'message' to its initialization method

#### Exception class example:
* `ImportError`
* `ValueError`
* `NameError` (using undefined variable)

## Catching import error
```python
try:
  import chardet
except ImportError:
  chardet = None

if chardet:
  # do something
else:
  # continue anyway
```

#### When two modules implement a common api
```python
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
```
