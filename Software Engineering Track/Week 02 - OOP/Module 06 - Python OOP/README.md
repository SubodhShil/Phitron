> # ```OOP Concepts```

### Pillars of OOP  
1. Abstraction
2. Encapsulation
3. Inheritance 
4. Polymorphism

Attributes can be occur multiple time in various classes.

1. **Simple Inheritance**: A child class inherits from a single parent class.
2. **Multi-level Inheritance**: In multi-level inheritance, a chain of inheritance exists from the base class to child classes.
3. **Multiple Inheritance**: A class can inherit from multiple other classes.

## Encapsulation
Encapsulation refers to giving priviledge to a user what data it can access. For example, 
1. Public: Attribute and methods can accessible by anywhere in the codebase.
2. Private: Attribute and methods are only accessible within the class.
3. Protected: Attribute and method are accessible within itself and derived classes.

## Abstraction
1. Abstract method is a method which only has declaration and doesn't have definition.

2. A class is called abstract class only if it has at least one abstract method.
when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class. If it is not done then child class also becomes abstract class automatically.

3. Python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract.

4. Creating object of an abstract class will give you error.

5. If a derived class is using any abstract class then it must use the abstract method

> Abstract class -এ কমপক্ষে একটি method থাকতে হয় । Method গুলোতে কোন definition দেওয়া থাকে না । যে derived class, কোন abstract class কে ব্যবহার করবে তাকে সেগুলো এইক্ষেত্রে abstract class method এর definition নিজের মতো করে দিয়ে দিবে ।  

## Polymorphism

"Poly" means many, "morph" means shape.

## Access Modifiers
There is not specific keyword to instantiate access and visibility of a class attributes. Instead it do it differently without mentioning any keyword.

```python
class DemoClass:
    # This is a public method
    # A public method name follows regular naming convention, that precede by nothing
    def publicMethod(self):
        pass
        
    # This is a protected method
    # A procted method name is precede by single underscore(_)
    def _protectedMethod(self):
        pass

    # This is a private method
    # A private method name is precede by double underscore(__)
    def __privateMethod(self):
        pass
```

