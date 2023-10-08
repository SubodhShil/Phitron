> # Class

Class is a blueprint to create various objects. 

A class contains two main properties: 
1. Attributes: Variables 
2. Behaviour: Function or methods

## ```self``` keyword in class methods
The '**self**' keyword is a mendatory argument (you can use other indentifier) to have in a class method, it refers the current object or instance of the class. 

> ⚠️ In the context of the class method's ```self``` argument, there's no need to explicitly provide a value at its position; the object will be automatically passed to the self argument. Therefore, if a method only has the 'self' argument and no other arguments, there's no need to manually pass anything to it.

Suppose have a class ClassA which contains a method methodA defined as:
```python 
class ClassA:
    def methodA(self, arg1, arg2):
        # codes here
```
and ```objectA``` is an instance of this class.

Now when ```objectA.methodA(arg1, arg2)``` is called, python internally converts it into:

```ClassA.methodA(objectA, arg1, arg2)```  

The **```self```** variable refers to the object itself.

## Constructor

Constructor is a special type of method that invoke itself automatically without any explicit mention.

Constructor doesn't differs from object to object, it stays same for all the objects. So, we should use a constructor to attain similar kind of functionality in all the objects. 

```python 
class myClass:
    def __init__(self, parameter1, parameter2, ...):
        # Initialize attributes or do other 'mendatory for all object' works here
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        # ...

    # Other methods and attributes of the class
```

## Class attributes vs instance attributes
Class attributes shared and accessible to all it's objects whereas an instance attribute is only accessible to a particular object.

### ```__repr__``` method
__repr__ is a special method that used for representing object details. By using it, you can print the object and see the details like attributes of the object.

