# TOC
* [Type inference](/type_related.md#type-inference)
* [Type alias](/type_related.md#type-alias)
* [GetType](/type_related.md#gettype)
* [Type capacity](/type_related.md#type-capacity)

## Type inference
In Python, every value has a datatype, but you don’t need to declare the datatype of variables. 
How does that work? Based on each variable’s original assignment, Python figures out what type it is and keeps tracks of that internally.


## Type alias
Type aliases are defined by simple variable assignments:
```python
Url = str

# using Url (str) alias in retry function
def retry(url: Url, retry_count: int) -> None: ...
```

## GetType
* You can use the `type()` function to check the type of any value or variable. As you might expect, 1 is an int
* Similarly, you can use the `isinstance()` function to check whether a value or variable is of a given type

## Type capacity
