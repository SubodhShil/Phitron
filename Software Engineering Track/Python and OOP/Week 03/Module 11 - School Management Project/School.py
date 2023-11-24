from Persons import Person, Teacher, Student

class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom:object):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student: object):
        className = student.classroom.name

        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f"No such classroom as {className}")


    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
        
    def __repr__(self) -> str:
        print(f"-------- Classrooms in {self.name} --------")
        for key, value in self.classrooms.items():
            print(key)

        print(f"--------- Students of Class Eight ---------")
        eight = self.classrooms['Eight']
        for student in eight.students:
            print(student.name)
        print(len(eight.students))

        print(f"--------- Subjects ---------")
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        print(f"--------- Exam Result ---------")
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value, student.subject_grade[key])
            print("")
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

    def add_subject(self, subject):
        self.subjects.append(subject)
        
    def take_semester_final(self):
        # take exam
        for subject in self.subjects:
            subject.exam(self.students)

        # calculate final grade
        for student in self.students:
            student.calculate_final_grade()

    def __str__(self) -> str:
        return f"{self.name}-{len(self.students)}"

    # TODO: sort students by grade
    def get_top_students(self):
        pass

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 40
    
    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)

