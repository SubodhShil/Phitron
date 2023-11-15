class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def workout(self, time_limit):
        print(f"I workout for {time_limit} hours. IT'S ABOUT DRIVE, IT'S ABOUT POWER, WE STAY HUNGRY, WE DEVOUR")
    
    def read(self):
        print("If you want to be a very good human being then one should study 'Srimad Bhagavad-Gita'")
        print(f"As a strategical person I love the book called '48 laws of power'")

    def eat(self):
        print("One should eat Satvic food to maintain good health")

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # overriding the base class method 'eat'
    def eat(self):
        print("Say no to unhealthy food, and eat satvic food")
    
    def workout(self, time_limit):
        return super().workout(time_limit)
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.age}, {self.height}, {self.weight}, {self.team}'

    # overload '+' operator
    def __add__(self, other):
        return self.age + other.age
    
    # overload 'len' method
    def __len__(self):
        return self.height
    
    # overload '>' operator
    def __gt__(self, other):
        if self.age > other.age:
            return f'{self.name} is bigger than {other.name} in age'
        else:
            return f'{self.name} is smaller than {other.name} in age'

MS_Dhoni =  Cricketer("Mahi", 50, 68, 90, "India")
Kohli = Cricketer("Virushka", 40, 65, 85, "India")

print(MS_Dhoni)
MS_Dhoni.read()
MS_Dhoni.eat()
MS_Dhoni.workout(3)

# if you add two circketer object it will add up the age of two cricketer object
# print(MS_Dhoni + MS_Dhoni)
# print(len(MS_Dhoni))
print(MS_Dhoni > Kohli)