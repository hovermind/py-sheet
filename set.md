* unordered collection of items. items can be any types (mixed)
* set itself is mutable but items must be immutable
* mathematical set operations like union, intersection, symmetric difference etc can be performed

## Creating set
```
my_set = {1, 2, 3}
my_set = {1.0, "Hello", (1, 2, 3)}  # tuple is allowed since immutable
my_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'

my_set = {1, 2, 2, 3}  # {1, 2, 3} duplicates are adjusted automatically

# creating set from list (order not maintained)
my_list = [1, 2, 3, 3, 4]
my_set = set(my_list)  # {1, 2, 3, 4}
```
**Empty set**
```
my_set = {}  # dict not set

my_set = set()  # empty set
```
