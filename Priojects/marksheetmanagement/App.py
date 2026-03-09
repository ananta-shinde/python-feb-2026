
studentData = []

for x in range(3):
    student = {}
    student["name"] = input("enter your name:")
    student["rollNo"] = input("enter your rollno:")
    student["phy"] = float(input("enter your marks for physics:"))
    student["chem"] = float(input("enter your marks for chemistry:"))
    student["maths"] = float(input("enter your marks for Maths:"))
    studentData.append(student)


for x in studentData:
    print(x)