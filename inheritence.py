class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def displayMarks(self):
        print("Marks:", self.marks)


def startProgram():

    student = Student("Karan", 21, 85)

    student.display()
    student.displayMarks()


startProgram()