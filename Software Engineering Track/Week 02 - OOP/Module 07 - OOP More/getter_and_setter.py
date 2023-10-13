# getter and setter

class NID:
    def __init__(self, first_name, last_name, age, present_address) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.present_address = present_address

    # getter
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # setter
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    def __repr__(self) -> str:
        return f'Name: {self.name}\nAge: {self.age}\nAddress: {self.present_address}'


Person1 = NID("Subodh", "Shil", 23, "Tongi, Gazipur")
print(Person1.full_name)
Person1.full_name = "Robert Kiosaki"
print(Person1.full_name)
