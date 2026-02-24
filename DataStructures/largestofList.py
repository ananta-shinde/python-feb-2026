# accept a list of numbers from user and print largest number
count = 0
numbers = []
count  = int(input("enter no of values"))

for x in range(count):
    numbers.append( int(input("enter a number :")))

largest = numbers[0]
for x in range(len(numbers)):
    if(numbers[x] > largest):
        largest = numbers[x]

print("largest value is :"+ str(largest))





