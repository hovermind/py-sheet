### Python doesn't have a formal Interface contract
**There's not much practical difference between abstruct base class (ABC) and interface. In Python, we can use an abstract base class to define and enforce an interface**
```python
# version 3.4
class AbstractGreeting(metaclass = ABCMeta):
    @abstractmethod
    def greeting(self, name):
        pass

class EnglishGreeting(AbstractGreeting):
    def greeting(self, name):
        return 'Hello, %s' % name

class JapaneseGreeting(AbstractGreeting):
    def greeting(self):
        return 'こんにちは、%sさん' % 'John'

print(EnglishGreeting().greeting('John'))    # Hello, John
print(JapaneseGreeting().greeting())         # こんにちは、Johnさん
```
