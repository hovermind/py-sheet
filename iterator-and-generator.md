## [Iterator](https://docs.python.org/3/tutorial/classes.html#iterators) and [Generator](https://docs.python.org/3/tutorial/classes.html#generators)
**Iterator**
```
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

**Generator**   
Generators are a simple and powerful tool for creating iterators. 
What makes generators so compact is that the __iter__() and __next__() methods are created automatically.
```
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```
Anything that can be done with generators can also be done with class-based iterators as described above
