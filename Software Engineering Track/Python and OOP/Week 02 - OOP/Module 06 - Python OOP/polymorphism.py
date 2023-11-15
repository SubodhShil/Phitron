class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal making some sound')

# Polymorphism
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Roar Roar!!')


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("I am meditating, I don't make sounds")


class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Mehh Mehh")

pussiCat = Cat('Pussi')
# pussiCat.make_sound()

germanShepard = Dog('Roku')
# germanShepard.make_sound()

blankBengal = Goat("Kala")
# blankBengal.make_sound()

# create list that contains different object of 'Animal' class
animals = [pussiCat, germanShepard, blankBengal]
for animal in animals:
    animal.make_sound()
