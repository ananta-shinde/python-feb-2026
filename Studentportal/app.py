

class College:

    def __init__(self):
        self.__collegeId = None
        self.__name = None
        self.__email = None
        self.__contact = None
        self.__address = None


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


class PersonalInfo:
    def __init__(self):
        self.name = None
        self.email = None
        self.contact = None
        self.address = None

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

class Student(PersonalInfo):

    def __init__(self):
        self.__prn = None

    def getPRN(self):
        return self.__prn




class Department:

    def __init__(self):
        self.__departmentId = None
    pass

class Teacher(PersonalInfo):

    def __init__(self):
        self.__empId = None
        self.salary = None
    pass

class Subject:

    def __init__(self):
        self.subjectId = None
    pass



