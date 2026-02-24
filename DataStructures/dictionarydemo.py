# studentData = [20,40,75]
studentData = {"key1":20,"key2":50,"key3":55}

#inserting new value to dictionary
studentData["key3"] = 56

#update dictionary
studentData["key3"] = 80

# delete a value from dictionary
studentData.pop("key2")

for x in studentData:
    print(studentData[x])

print(studentData)