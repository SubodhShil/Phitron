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
## Inner function
Function is a first class object in Python. That means functions can be passed like regular variables or data structures. 

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

1. We can have nested function, that means a function that declared inside another function. 

    ```python
    def outer_func():
        def inner_func():
            return "inner"
        return inner_func
    ```

2. We can pass function as a parameter in another function.
   ```python
    def hola(pass_func):
        return pass_func

    def message(msg):
        return msg
    
    print(message('message says hola'))
   ```