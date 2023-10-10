from abc import ABC, abstractmethod

# abstract base class
class Animal(ABC):
    
    @abstractmethod  # enforce all derive class to have the 'eat' method
    def eat(self):
        pass

    @abstractmethod
    def hobby(self):
        pass

class Dog(Animal):
    def __init__(self, name) -> None:
        self.name = name
        self.category = 'Bull dog'
        super().__init__()
        
    def eat(self):
        print(f'I am {self.name} and a good {self.category}, I love dog food!!')
        
    def hobby(self):
        print("I love to swim and roam around park")

bulldog = Dog('Billi')
bulldog.eat()
bulldog.hobby()

