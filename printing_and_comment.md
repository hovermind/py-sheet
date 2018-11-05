# TOC
* [Print function](/printing_and_comment.md#print-function)
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

## Comment
* single line: `# this is single line commenct`
* multi-line:
```python
''' This is 
    Multi-line comment 
    in python
'''
```

