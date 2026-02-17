# accept three numbers from user and print largest number
n1 = int(input("Enter a number"))
n2 = int(input("Enter a number"))
n3 = int(input("Enter a number"))
if(n1>n2 and n1>n3):
    print(n1)
if(n2>n1 and n2>n3):
    print(n2)
if(n3>n1 and n3>n2):
    print(n3)