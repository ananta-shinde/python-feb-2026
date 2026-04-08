
class Address:
    atPost =None
    city = None
    state = None
    country =None
    pincode = None
class College:
    id = None
    name = None
    email = None
    contact = None
    address = Address()

class Departmant:
    id = None
    name = None
class Teacher:
    empId = None
    name = None
    email = None
    salary = None
    contact = None
    address = Address()
    department = Departmant()

class Student:
    prn = None
    name = None
    email = None
    contact = None
    address = Address()
    department = Departmant()


