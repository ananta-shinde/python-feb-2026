
studentList = []

#add new student
def addStudent():
    student = {}
    student["rollno"] = int(input("enter roll no :"))
    student["name"] = input("enter name :")
    student["branch"] = input("enter branch name :")
    studentList.append(student)
    print("student was added")

#update student
def updateStudent(rollno):
    for student in studentList:
        if(student["rollno"] == rollno ):
            branch = input("enter new branch name :")
            student["branch"] = branch
            return
    print("invalid roll no")
# get student by roll no
def printStudentDetails(rollno):
    for student in studentList:
        if(student["rollno"] == rollno):
            print("name:"+ student["name"]+ " branch :"+ student["branch"])
            return
    print("invalid roll no")

# get list of all students
def printAllStudent():
    if(len(studentList) != 0):
        for student in studentList:
            print("name:" + student["name"] + " branch :" + student["branch"])
    else:
        print("list is empty")



print("************* welcome ************************")

while(True):
    print("choose from following menus :")
    print("1.add new student 2.update student 3.get details by rollno 4. exit")
    choice = int(input("enter your choice"))
    if(choice == 1):
        addStudent()
    elif(choice == 2):
        rollno = int(input("enter roll no :"))
        updateStudent(rollno)
    elif(choice == 3):
        rollno = int(input("enter roll no :"))
        printStudentDetails(rollno)
    elif(choice == 4):
        break
    else:
        print("invalid choice")