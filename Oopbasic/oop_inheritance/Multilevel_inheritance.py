class Student:
    def getStudent(self):
        self.name = input("name: ")
        self.age = input("age: ")
        self.gender = input("gender: ")


class Test(Student):
    def getMarks(self):
        # Accept class and marks
        self.studentclass = input("class: ")
        print("Enter the marks of respective subject")
        self.literature = int(input("literature: "))
        self.maths = int(input("maths: "))
        self.biology = int(input("biology: "))
        self.physics = int(input("physics: "))


class Marks(Test):
    def display(self):
        # Display student's information along with total marks
        print("/n/nName:", self.name)
        print("age: ",self.age)
        print("gender: ",self.gender)
        print("class: ",self.studentclass)
        print("literature: ",self.literature)
        print("maths: ",self.maths)
        print("biology: ",self.biology)
        print("physics: ",self.physics)
        total_marks = self.literature + self.maths + self.biology + self.physics
        if total_marks > 100:
            print("Passed")
        else:
            print("Failed")
        print("Total marks: ", total_marks)

# Create an object of Marks class
m = Marks()
#
# # Collect student details
m.getStudent()
#
# # Collect marks details
m.getMarks()
#
# # Display all information
m.display()
