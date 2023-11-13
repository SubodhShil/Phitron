## Overload
Overload is to use multiple methods with the same name, but different parameter signatures within the same class.

## Override
Overriding is to use a class method in a different way by changing is actual definition or implementation

## Static and class method 
Both static and class methods are allowed to be invoked without creating any specific class object or instance.

However, class method can have access to variables that declared within the class. But class method can't invoke or call any regular class method, until the method is classmethod or static method itself. Where on the other side, static method can't access or invoke anything from a class where it declared.

## **getter** and **setter**

1. Getter and setter are used for providing values in private properties.
2. A getter without any setter is a read-only attribute.
3. Without a getter, one can't create a getter.

### @property
The "**@property**" decorator let us access a method in an attribute variable like fashion.

```python
class demoClass:

    @property
    def demo(self):
        return f"This is demo"

demoObject = demoClass()
print(demoObject.demo) 
```
## Wrapper function

### Inner function
Function is a first class object in Python. That means functions can be passed like regular variables or data structures. We can pass function as a parameter in another function.

```python
def hola(pass_func):
    return pass_func

def message(msg):
    return msg

print(message('message says hola'))
```

```python
def f1():
    print("I'm from f1")

def f2(f):
    f()

f2(f1)
```
<details>
<summary>Output</summary>

    I'm from f1

</details>

&nbsp;

> #### The wrapper function is a function that can be used to wrap another function. When working with a function, that we don't want to change it's actual function signature but want to test or do additional things around the function, wrapper comes with benefits. To do this we can use nested functions, that means a function that declared inside another function. 

```python
def outer_func():
    def inner_func():
        return "inner"
    return inner_func
```

The example is still not a wrapper function. It would be called as a wrapper function if the receive a function as parameter. The inner_func() here will call the argument function received by the outer_func(). The addition task will be done inside inner_func(). Here is a template for wrapping functions.

```python
# Wrapper function
def outer_func(func_as_arg):
    def inner_func_wrapper():
        # additional task
        func_as_arg()
        # additional task

    return inner_func_wrapper
```

To invoke the wrapper function
```python
def outer_func(func_as_arg):
    def inner_func_wrapper():
        # additional task
        print("additional task 1")

        # invoking parameter function
        func_as_arg()

        # additional task
        print("additional task 2")

    return inner_func_wrapper

def test():
    print("Testing")

outer_func(test)()
```

We can use decorator to invoke the wrapper function easily. 

```python
def outer_func(func_as_arg):
    def inner_func_wrapper():
        # additional task
        print("additional task 1")

        # invoking parameter function
        func_as_arg()

        # additional task
        print("additional task 2")

    return inner_func_wrapper

# With decorator
@outer_func
def test():
    print("Testing")

test()
```

## Composition and "has a" relation
The inheritance said to be "is a" relation. 

## UML Diagrams
1. UML stands for **Unified Modeling Language". 
2. It used for represent object oriented system components like (mainly 4):
    - classes, 
    - attributes,
    - methods or operations
    - relationship among objects
3. The representation uses visual or graphical notation called diagram to discribe complex structure.

Types:
1. Class diagram 
2. Usecase diagram
3. Sequence diagram 
4. Activity diagram

## Design Pattern
- Generalize and reusable solution to a commonly occurring problem in software design. 
- **Singleton design pattern**: One instance for one class in the source code.
- 