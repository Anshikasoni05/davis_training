class Student:

    def __init__(self, name, roll_no, course, semester, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.semester = semester
        self.marks = marks

    def details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"Semester: {self.semester}")
        print(f"Marks: {self.marks}")


student1 = Student("Anshika soni", 101, "B.Tech CSE", 7, 92)
student2 = Student("rohan", 102, "B.Tech CSE", 7, 88)

student1.details()

print("\nAfter Updating Student Details:\n")

student1.course = "B.Tech AI & ML"
student1.semester = 8
student1.marks = 95

student1.details()