
List = [20,15,33,45,56,25,65]

print(List)

#printting a list or traversal
for x in List:
    print(x)


print("*****")
# filters
for x in List:
    if(x > 50):
        print(x)

print("**** only even numbers*****")
for x in List:
    if(x%2 == 0):
        print(x)

print("**** only odd numbers *****")
for x in List:
    if(x%2 != 0):
        print(x)


newList = []
print("******* new list *******")
for x in List:
    newList.append(x)
print(newList)


#sorting a list
for x in range(len(List)):
    for i in range(len(List)-1):
        if(List[i] > List[i+1]):
            temp = List[i]
            List[i] = List[i+1]
            List[i+1] = temp


print(List)


