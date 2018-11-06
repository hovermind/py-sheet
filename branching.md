# TOC
* [if-else](/branching.md#if-else)
* [ternary](/branching.md#ternary)
* [switch](/branching.md#switch)

## if-else
```python
if expression:
    print("foo")
elif expression:
    print("bar")
else:
    print("baz")
```

## ternary
```python
print("A") if a > b else print("B")
```

## switch
python does not have switch => use hack:
```python
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found
```
