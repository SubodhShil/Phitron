from School import School, ClassRoom
from Persons import Student

def main():
    school = School("Holy Moly School", "Dhaka-1230")
    eight = ClassRoom('Eight')
    school.add_classroom(eight)

    nine = ClassRoom('Nine')
    school.add_classroom(nine)

    ten = ClassRoom('Ten')
    school.add_classroom(ten)

    # Students 
    moksed = Student("Abul Khan Moksed", nine)
    school.student_admission(moksed)
    
    print(school)

if __name__ == '__main__':
    main()