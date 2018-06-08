* `try...except` blocks to handle exceptions
* `raise` statement to generate them
```
if size < 0:
    raise ValueError('number must be non-negative')
```
Exceptions are implemented as classes, and this raise statement is actually creating an instance of the class 
and passing the string 'message' to its initialization method
