class PersonalInfo:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__contact = None
        self.__address = None

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getContact(self):
        return self.__contact

    def setContact(self, contact):
        self.__contact = contact

    def getAddress(self):
        return self.__address

    def setContact(self, address):
        self.__address = address


class College:

    def __init__(self,collegeId,name):
        self.__collegeId = collegeId
        self.__name = name
        self.__email = None
        self.__contact = None
        self.__address = None
        self.__departments = []


    def getCollegeId(self):
        return self.__collegeId
    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getContact(self):
        return self.__contact

    def setContact(self, contact):
        self.__contact = contact

    def getAddress(self):
        return self.__address

    def setContact(self, address):
        self.__address = address

    def setDepartment(self,department):
        self.__departments.append(department)

    def getDepartments(self):
        return self.__departments



class Student(PersonalInfo):

    def __init__(self,prn):
        self.__prn = prn

    def getPRN(self):
        return self.__prn





class Teacher(PersonalInfo):

    def __init__(self,empId):
        self.__empId = empId
        self.__salary = None

    def getEmpId(self):
        return self.__empId

    def getSalary(self):
        return self.__salary

    def setSalary(self,amount):
        self.__salary = amount

class Subject:

    def __init__(self,sunId,name):
        self.__subjectId = sunId
        self.__name = name


class Department:

    def __init__(self,departmentId,name):
        self.__departmentId = departmentId
        self.__name = name

    def getDepaertmentId(self):
        return self.__departmentId

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name




mit = College(1000,"MIT")
cse = Department(100,"CSE")
mit.setDepartment(cse)
print(mit.getDepartments()[0].getName())
