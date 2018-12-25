# TOC
* [Class in python](#Class-in-python)
* [Constructor](#Constructor)
* [Access modifier](#Access-modifier)
* [Creating new object instance](#Creating-new-object-instance)
* [Class variable vs instance variable](#Class-variable-vs-instance-variable)
* [Function vs method](#Function-vs-method)
* [Class method](#Class-method)
* [Inheritance](#Inheritance)
* [Multiple inheritance](#Multiple-inheritance)

## Class in python
* a class creates a new local namespace where all its attributes are defined. Attributes may be data or functions. There are also special attributes in it that begins with double underscores (`__`). For example, `__doc__` gives us the docstring of that class.
* the method function is declared with an explicit first argument representing the object
* all member functions are virtual
* allows multiple inheritance (can inherit multiple base classes)
* built-in types can be used as base classes for extension by the user

**Class Definition Syntax**
```
class ClassName:
	'''This is a docstring'''
	
    <statements>
```

**Note:**   
As soon as we define a class, a new class object is created with the same name. This class object allows us to access the different attributes
```
class MyClass:
	'''This is a docstring'''
	
	a = 10
	def func(self):
		print('Hello')

print(MyClass.a)          # Output: 10
print(MyClass.func)       # Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.__doc__)    # Output: 'This is my second class'
```

## Constructor
Special function: `__init__()`
```
class ComplexNumber:
	'''This is a docstring'''
	
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print(f"{self.real}, {self.imag}")

# Create a new ComplexNumber object
c1 = ComplexNumber(2, 3)

# print
print(c1.getData())     # Output: 2 + 3j
```

## Access modifier
* nothing in Python makes it possible to enforce data hiding — it is all based upon convention.
* `Private` instance variables that cannot be accessed except from inside an object don’t exist in Python. 
However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). 
It should be considered an implementation detail and subject to change without notice.
* See: [Hack - private variables in python](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Creating new object instance
We can create new object instances (while ss soon as we define a class, a new class object is created with the same name - called class object):
```
ob = MyClass()
```

Any function object that is a class attribute defines a method for objects of that class.
This means to say, since MyClass.func is a function object (attribute of class), ob.func will be a method object.
```
print(MyClass.func)    # Output: <function MyClass.func at 0x000000000335B0D0>

print(ob.func)    # Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
```

## Class variable vs instance variable
Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:
```
class Dog:
	'''This is a docstring'''

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
```

## Function vs method
```
# Function: defined outside the class
def f1(self, x, y):
    return x+y

class C:
	'''This is a docstring'''
	
	# Method - function inside a class
    def g(self):
        return 'hello world'
```

## Class method
whenever an object calls its method, the object itself is passed as the first argument. In definition of method, the first parameter is named as `self` (can be whatever you want).
While calling the method, the aurgument for `self` is omitted (but obejct reference will be passed behind the scene)
```
class MyClass:
	'''This is a docstring'''
	
	a = 10
	def func(self, name):
		print(f"Hello {name}!")

ob = MyClass()
ob.func()
```

**Note:**    
a method is an object and can be stored away and called at a later time
```
class MyClass:
    '''A simple example class'''
	
    i = 10

    def f(self):
        print('hello world')

		
mf = MyClass.f

if MyClass.i > 10:
	mf()
```

## Inheritance
```
class DerivedClassName(BaseClassName):
	'''This is a docstring'''
	
    <statements>
	
class DerivedClassName(modName.BaseClassName):
	'''This is a docstring'''
	
    <statements>
```

Python has two built-in functions that work with inheritance:
* `isinstance()` : to check an instance’s type. `isinstance(obj, int)` will be True only if obj.__class__ is int or some class derived from int. 
* `issubclass()` : to check class inheritance. `issubclass(bool, int)` is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

## Multiple inheritance
Multiple Inheritance
Python supports a form of multiple inheritance
```
class DerivedClassName(Base1, Base2, Base3):
	'''This is a docstring'''
	
    <statements>
```

**Note:**   
the search for attributes inherited from a parent class works as: depth-first, left-to-right
i.e. if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
**Do not use multiple inheritance (personal opinion)**

