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
    def __init__(self, school_name) -> None:
        self.school_name = school_name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        # storing teacher objects into self.teachers list
        self.teachers.append(teacher)
        return f'Thanks for joining our school, {name}'

    def student_enroll(self, stu_name: str, fee: float, current_class: int):
        if fee < 6000:
            return f'Student fee is 6000 taka, please provide remaining {6000 - fee} taka to ensure enrollment'
        else:
            remain = fee - 6000
            if remain:
                print(f'Your change is {fee - 6000} taka')
            id = len(self.students) + 1001
            new_student = Student(stu_name, current_class, id)
            self.students.append(new_student)
            return f'Thanks for choosing the school.\nWelcome {stu_name} to the school at class {current_class}'

    def __repr__(self):
        print(f"Welcome to {self.school_name}")
        print(f"\n------------------\nOur Teachers\n------------------")
        for teacher in self.teachers:
            print(teacher.name)
        print(f"\n------------------\nOur Students\n------------------")
        for student in self.students:
            print(student.name)
        return '\nThanks for having us'

# Kratos = Student("Kratos", 8, 3)
# print(Kratos)


# Declaring School object
OM_Shanti_School = School("OM Shanti Vedic School")

print(OM_Shanti_School.student_enroll("Subodh", 6500, 8))
print(OM_Shanti_School.student_enroll("Lali", 6000, 6))
print(OM_Shanti_School.student_enroll("Sahil", 5500, 2))

print(OM_Shanti_School.add_teacher("Rohomot Ali Maxwell", "Programming"))
print(OM_Shanti_School.add_teacher("Siplu Shil", "Mathematics"))

print()
print(OM_Shanti_School)