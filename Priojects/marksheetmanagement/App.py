
studentData = []

for x in range(3):
    student = {}
    student["name"] = input("enter your name:")
    student["rollNo"] = input("enter your rollno:")
    student["phy"] = float(input("enter your marks for physics:"))
    student["chem"] = float(input("enter your marks for chemistry:"))
    student["maths"] = float(input("enter your marks for Maths:"))
    studentData.append(student)

print("rollno  name   physics  chemistry  maths")
for student in studentData:
    print(student["rollNo"] +" "+student["name"]+" "+str(student["phy"])+" "+str(student["chem"])+" "+str(student["maths"]))