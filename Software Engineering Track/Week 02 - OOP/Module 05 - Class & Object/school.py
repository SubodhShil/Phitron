class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    # __repr__ represents the current object details
    def __repr__(self):
        return f'Student name: {self.name}\nID: {self.id}\nClass: {self.current_class}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'{self.name}\n{self.subject}\n{self.id}'

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []

    def add_teacher(self, name, subject):


Kratos = Student("Kratos", 8, 3)
print(Kratos)

Subodh = Teacher("Subodh", "Programming", 2)
print(Subodh)
