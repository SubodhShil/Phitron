import random

def grade_to_value(grade):
    grade_map = {"A+": 5.00, "A": 4.00, "A-": 3.50, "B": 3.00, "C": 2.00, "D": 1.00, "F": 0.00}
    return grade_map[grade]

def value_to_grade(value):
    if 4.5 <= value <= 5.00:
        return 'A+'
    elif 3.5 <= value < 4.5:
        return 'A'
    elif 3.0 <= value < 3.5:
        return 'A-'
    elif 2.5 <= value < 3.0:
        return 'B'
    elif 2.0 <= value < 2.5:
        return 'C'
    elif 1.0 <= value < 2.0:
        return 'D'
    else:
        return 'F'

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def teach(self):
        pass
    
    def __repr__(self) -> str:
        return f'{self.name}'
    
    def evaluate_exam(self):
        marks = random.randint(0, 100)
        return marks

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def calculate_final_grade(self):
        total_point = 0

        for grade in self.subject_grade.values():
            point = grade_to_value(grade)
            total_point += point
            print(self.name, grade, point)

        point_avg = total_point/len(self.subject_grade)
        self.grade = value_to_grade(point_avg)
        print(f"{self.name}'s final grade is: {self.grade} with pionts avg: {point_avg}")
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
        
    



