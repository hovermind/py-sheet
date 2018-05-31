## implicit casting
`int + float = float`    
Python coerces the int into a float to perform the addition, then returns a float as the result.

## Explicit casting
#### int - float
* `int(x [, base])`
* The `int()` function will truncate, not round
* The `int()` function truncates negative numbers towards 0. It’s a true truncate function, not a floor function
```
floatVal = float(5) # 5.0

intVal = int(5.5) # 5
```
#### str
```
myInt = 5
myFloat = 5.5
strInt = str(myInt)
strFloat = str(myFloat)

floatValue = float("5.5")
intValue = int("5")
```
**Note:** `int("5.5")` will be error, because `"5.5"` will be parsed to float. `int(float("5.5"))` is ok

