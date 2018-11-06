# TOC
* [for](/looping.md#for)
* [foreach](/looping.md#foreach)
* [iterating over range](/looping.md#iterating-over-range)
* [while](/looping.md#while)
* [Else with for and while](/looping.md#else-with-for-and-while)

## for
```python
for element in sequence:
    # A sequence can be a list, set, or range
```

## foreach
* for can iterate over anything that provides iterator (`HasNext() + Next()`)
```python
fruits = ['banana', 'apple',  'mango']

for element in fruits:
   print (element)
```

## iterating over range
* start & step have default values(start = 0, step = 1), so can be omitted
* range(n) => n is finish, start = 0, step = 1
* range(x, n) => x is start, n is finish, step = 1
* range(x, n, s) => x is start, n is finish & s is step
```python
for element in range(start, finish, step):
   print (element)
   
for x in range(3, 8, 2):
    print(x)              # prints out 3,5,7
    
for x in range(3, 6):
    print(x)              # prints out 3,4,5
    
for x in range(5):
    print(x)              # prints : 0,1,2,3,4

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print (fruits[index])
```  

## while
```python
while boolean_expression: 
    # statements to execute
```

## Else with for and while
* else with for & while (unique in python)
* "for" or "while" statement fails then code part in "else" is executed. 
* If break statement is executed inside for loop then the "else" part is skipped. 
* Note that "else" part is executed even if there is a continue statement.
```python
# termination by limit
count = 0 
for count in range(5):
    print(count++)
else:
    print("count value reached 5")
    
# termination by break
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("loop is terminated because reached to limit")

# termination by limit
count = 0 
while(count < 5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
```

