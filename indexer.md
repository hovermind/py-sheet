## Indexer
**Indexer in python:** `__getitem__`   

Implementing getitem in a class allows its instances to use the [] (indexer) operator
```
class Foo(object):
    def __init__(self):
        self.bar = {
            'name':'Hassan',
            'country':'Bangladesh'
        }

    def __getitem__(self, i):
        return self.bar[i]

foo = Foo()

foo['name']     # Output: 'Hassan'
foo['number']   # Output: 'Bangladesh'
```
