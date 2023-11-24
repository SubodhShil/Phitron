from School import School, ClassRoom, Subject
from Persons import Student, Teacher

def main():
    school = School("Holy Moly School", "Dhaka-1230")
    eight = ClassRoom('Eight')
    school.add_classroom(eight)

    nine = ClassRoom('Nine')
    school.add_classroom(nine)

    ten = ClassRoom('Ten')
    school.add_classroom(ten)

    # Students
    moksed = Student("Abul Khan Moksed", eight)
    school.student_admission(moksed)
    leon = Student("Illiot Leon", eight)
    school.student_admission(leon)

    # Subjects
    physics_teacher = Teacher('Maxwell Pathan')
    physics = Subject("Physics", physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Murali Singh')
    chemistry = Subject("Chemistry", chemistry_teacher)
    eight.add_subject(chemistry)

    # Taking Exam 
    eight.take_semester_final()
    print(school)

if __name__ == '__main__':
    main()