
class Student:
    rollno = None
    name = None
    email = None
    __password = None
    contact = None
    address = None

    def printStudentData(self):
        print(self.name + " "+self.email+" "+ self.address)



s1 = Student()
s2 = Student()

s1.name = "Ananta"
s1.email = "demo@gmail.com"
s1.demo = "dsasdasdasd"
s1.address = "pune"
s2.name = "Rahul"
s2.email = "example@gmail.com"
s2.address = "mumbai"
s1.printStudentData()
s2.printStudentData()
print(s1.password)
