from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name
        
    def __str__(self) -> str:
        pass

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.nmae = name
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, name, height, base) -> None:
        self.name = name
        self.height = height
        self.base = base
        super().__init__(name)

    def area(self):
        return (1/2 * self.base * self.height)

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.name = name
        self.radius = radius
        super().__init__(name) 

    def area(self):
        return pi * self.radius * self.radius
