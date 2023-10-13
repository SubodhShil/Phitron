class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self._age = age
        self.__money = money

    @property
    def age(self):
        return self._age

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money
        return self.__money

    @property
    def salary(self):
        return self.__money

    @salary.setter
    def salary(self, value):
        if value < 0:
            return "Salary can't be negative"
        else:
            self.__money += value


person1 = User('Miso', 33, 25000)

# using method as attribute -> getter
print(person1.money)

# set value to a getter attribute -> setter
person1.money = 300
print(person1.money)
person1.salary = 12000
print(person1.money)
