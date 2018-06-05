* A sequence of Unicode character & immutable
* Uses single quotes `'` double quotes `"` to denote literal strings
* Multi-line strings can be denoted using triple quotes, `'''` or `"""`
* slicing operator [ ] can be used with string (list/array of chars)
```
hooman = 'hooman'
hovermind = "hovermind"
```

## String interpolation
```
hooman = "hooman"
hovermind = "hovermind"

print(f"Hello {hooman}!")

print("Hello {hooman}!, I am {hovermind}\n".format_map(locals()))
```

## Accessing characters in a string
List of chars. We can access individual characters using indexing and a range of characters using slicing. Negative indexing also possible.
```
hooman = 'hooman'
m = hooman[3]
n = hooman[-1]
man = hooman[3:6]
```

## change or delete a string
Strings are immutable that means elements of a string cannot be changed. String variable can be re-assigned.
```
hooman = "hooman"
hooman[1] = 'u'        # TypeError: 'str' object does not support item assignment
del hooman[1]          # TypeError: 'str' object doesn't support item deletion

hooman = "hoowoman"
del hooman
```
