class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student: object):
        className = student.classroom.name 
        
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f"No such classroom as {className}")

    def __repr__(self) -> str:
        print(f"Classrooms in {self.name}")
        for key, value in self.classrooms.items():
            print(key)
        return ''
    
class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students) + 1}'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)
        self.subjects = []
        self.marks = {}
        self.grade = None

    def __str__(self) -> str:
        return f"{self.name}-{len(self.students)}"

    # TODO: sort students by grade
    def get_top_students(self):
        pass