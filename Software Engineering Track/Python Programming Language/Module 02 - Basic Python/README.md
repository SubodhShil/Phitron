> # ```args and kwargs in Python```

## args
**args** are arguments contains in a tuple. 

*args are beneficial when we don't know how many arguments could be passed in a function. Args are arguments contained in a tuple and we can also iterate on args. To indicate *args as argument, the symbol ( * ) known as the unpacking operator. The *args is not a strict keyword to be used, we can use any valid identifier but ensure use * before an identifier. 

```python 
def sum(*numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum

print(sum(10, 20, 30, 5))
```
## kwargs 
Assume **kwargs** as dictionary input, where the argument needs to be mentioned with key-name. Using **kwargs we can have access to both key and its corresponding value.

```python 
student = {'name': "Pulkit", 'age': 33, 'isMarried': False}

def student_details(**student):
    for key, value in student.items():
        print(f"{key}: {value}")

student_details(**student)
```

## Multiple return
Unlike most other programming languages, python can return multiple values. If you return multiple values from a function, it will return values in a tuple.

## Variable scopes
Variable can be defined as same identifier name in both global and local scope. But while working in a function, the local scoped variable has more priority. 

**Global variable**: Global variables are the variables declared outside any function body, they can be used in the function scope, but modifying global variables isn't valid. If you still want to modify a global variable in a local scope or in a function body you've to use the 'global' keyword. The modification or changes of a global variable from a local scope only be visible to the local scope, so it doesn't affect the actual global value.

```python
global_value = 300      

def useGlobal():
    global global_value
    global_value = global_value - 100

print(global_value)
```

## Modules


### list, array and collection all same and interchangeable names in python.
