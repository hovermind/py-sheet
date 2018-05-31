## Print function
```
print("Total score for {} is {}".format(name, score))

print("Total score for {0} is {1}".format(name, score))

print("Total score for {n} is {s}".format(n = name, s = score))

print("Total score for", name, "is", score)

# If you don't want spaces to be inserted automatically
print("Total score for ", name, " is ", score, sep='')
```

## Interpolation
```
name = "hassan"
score = 82 # out of 100

print(f'Total score for {name} is {score}')
```
