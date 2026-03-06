listOfTempMonth = []
firstweek = []
# accept temp of a week
for x in range(7):
   temp =  float(input("enter temprature of the day"))
   firstweek.append(temp)
listOfTempMonth.append(firstweek)

sumOfMonth = 0
for temp in listOfTempMonth:
    sumOfMonth =sumOfMonth + temp

#sum of temp for 1st week
sum = 0
for index in range(7):
    sum = sum + listOfTemp[index]

print("avg temp of 1st week:"+ str(sum/7))

print("avg temp of month:" + str(sumOfMonth/len(listOfTemp)))