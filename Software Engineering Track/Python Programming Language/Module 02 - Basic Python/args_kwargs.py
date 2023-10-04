# *args

def sum(*numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum


print(sum(10, 20, 30, 5))

# **kwargs
student = {'name': "Pulkit", 'age': 33, 'isMarried': False}

def student_details(**student):
    for key, value in student.items():
        print(f"{key}: {value}")

student_details(**student)
