# accept roll no  name and marks of 5 student from user and print list

studentList = []

for x in range(5):
    student = {}
    student["rollno"] = int(input("enter roll no :"))
    student["name"] = input("enter name :")
    student["marks"] = float(input("enter marks :"))
    studentList.append(student)


# printing list as it is
print(studentList)

# printing list one by one
for student in studentList:
    print(str(student["rollno"]) + " "+ student["name"]+" " +str(student["marks"]))
