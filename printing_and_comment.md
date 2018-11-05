# TOC
* [Print function](/printing_and_comment.md#print-function)
* [Printing interpolated string](/printing_and_comment.md#printing-interpolated-string)
* [Comment](/printing_and_comment.md#comment)

## Print function
```python
print("Total score for {} is {}".format(name, score))

print("Total score for {0} is {1}".format(name, score))

print("Total score for {n} is {s}".format(n = name, s = score))

print("Total score for", name, "is", score)

# If you don't want spaces to be inserted automatically
print("Total score for ", name, " is ", score, sep='')
```

## Printing interpolated string
```python
hooman = "hooman"
hovermind = "hovermind"

print(f"Hello {hooman}!")

print("Hello {hooman}!, I am {hovermind}\n".format_map(locals()))
```

## Comment
* single line: `# this is single line commenct`
* multi-line:
```python
''' This is 
    Multi-line comment 
    in python
'''
```

