
student = { "name":"Rahul","marks": 456,"email":"demo@gmail.com"}

print(student["marks"])

print(student)
print(list(student.values()))
print(list(student.keys()))
print(len(student))
print(list(student.items()))
print(student.pop("email"))
print(student)
student["newKey"] = 20
#print(student.clear())
print(student.get("name"))

print(student)
