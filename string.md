# TOC
* [String](/string.md#string)
* [String interpolation](/string.md#string-interpolation)
* [Escape sequence](/string.md#escape-sequence)
* [Split](/string.md#split)
* [Join](/string.md#join)
* [Concatenation](/string.md#concatenation)
* [Format specifier](/string.md#format-specifier)
* [String template](/string.md#string-template)
* [Iterating and membership test](/string.md#iterating-and-membership-test)
* [Accessing characters in a string](/string.md#accessing-characters-in-a-string)
* [Change or delete a string](/string.md#change-or-delete-a-string)

## String
* A sequence of Unicode character & immutable
* Uses single quotes `'` double quotes `"` to denote literal strings
* Multi-line strings can be denoted using triple quotes, `'''` or `"""`
* slicing operator [ ] can be used with string (list/array of chars)
```python
hooman = 'hooman'
hovermind = "hovermind"
```

## String interpolation
```python
hooman = "hooman"
hovermind = "hovermind"

print(f"Hello {hooman}!")

print("Hello {hooman}!, I am {hovermind}\n".format_map(locals()))
```

## Escape sequence
* escape sequence: `\` or `'''`
```python
# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")
```

**Raw  string :** use r or R in front of string
```python
print(r"This is \x61 \ngood example")   # This is \x61 \ngood example
```

## Split
`string.split('delimeter' [, maxsplit = n])`
```python
test = "1, 2, 3"
splitted = test.split(',')                     # ['1', '2', '3']
split_one = test.split(',',  maxsplit = 1)     # ['1', '2, 3']
```

## Join
`string.join(iterable)` (list/set/dict/string). list/set items & dict keys must be string (for dict, keys will be used)
```python
my_list = ["1", "2", "3"]
my_set = {'1', '2', '3'}

separator = "|"

final_str = separator.join(my_list)   # "1|2|3"
final_str = separator.join(my_set)    # "1|2|3"

my_dict = {"1": "one", "2":"two"}
final_str = separator.join(my_dict)    # "1|2"
```

## Concatenation
```python
h = "hello"
w = "world"
hw = h + w

h3 = h * 3                      # hello hello hello

# two string literals together
hw = 'Hello ''World!            # 'Hello World!'

# using parentheses
hw = ('Hello '
             'World')           # 'Hello World'
```

## Format specifier
same as C# -> `:` 
```python
testNum = 123456789
testFloat = 7141.6247234
PI = 3.1416247234

print(f"Hex: {testNum : x}")
print(f"Hex with notation: {testNum :#x} \n")

print(f"Binary: {testNum : b}")
print(f"Binary with notation: {testNum :#b} \n")

print(f"Octal:{testNum : o}")
print(f"Octal with notation: {testNum :#o} \n")

# separator
print(f"Comma separated: {testNum :,}")
print(f"PI precision to 4th place: {PI :.5}")

# date formatting
import datetime
test_date = datetime.datetime(2017, 10, 2, 16, 30, 00)
print(f"{test_date :%Y-%m-%d %H:%M:%S}")
```

## String template
```python
from string import Template

strTemplate = Template('$who likes $what')

strFinal = strTemplate.substitute(who = "Hassan", what = "programming")
print(f"{strFinal}")   # Hassan likes programming

substituterDict = dict(who = "hovermind", what = "game")
strFinal = strTemplate.substitute(substituterDict)
print(f"{strFinal}")   # hovermind likes game
```
`safe_substitute(d)` : if a value missing it will print $subs as it is
```
from string import Template

strTemplate = Template('$who likes $what')

substituterDict = dict(who = "hovermind")
strFinal = strTemplate.safe_substitute(substituterDict)
print("{strFinal}")   # hovermind likes $what
```

## Iterating and membership test
```python
hw = 'Hello World'

count = 0
for letter in hw:
    if(letter == 'l'):
        count += 1
        
print(count,'letters found')

'a' in 'program'       # True
'at' not in 'battle'   # False
```

## Accessing characters in a string
List of chars. We can access individual characters using indexing and a range of characters using slicing. Negative indexing also possible.
```python
hooman = 'hooman'
m = hooman[3]
n = hooman[-1]
man = hooman[3:6]
```

## Change or delete a string
Strings are immutable that means elements of a string cannot be changed. String variable can be re-assigned.
```python
hooman = "hooman"
hooman[1] = 'u'        # TypeError: 'str' object does not support item assignment
del hooman[1]          # TypeError: 'str' object doesn't support item deletion

hooman = "hoowoman"
del hooman
```

## See: [python string methods](https://www.programiz.com/python-programming/methods/string)
