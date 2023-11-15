class Person:
    name = "Ryan"
    age = 33
    job = "Engineer"

    def wish(self):
        print(f"I am Ryan, at age 33 I wish everyone in the world be happy")

# human = Person()
# human.wish()


class School:
    # method
    def marks(self, n, m, s):
        self.n = n
        self.m = m
        self.s = s
        print(f"{n} got marks: {m} and {s}")


student1 = School()
student1.marks("student1", 90, 85)

student2 = School()
student2.marks("student2",  33, 25)

""" How it internally works
School.marks(student1, n, m, s)
School.marks(student2, n, m, s)
"""
