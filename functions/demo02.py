# n1 = input("enter a number")
def avgOfthree(n1,n2,n3):
    avg= n1+n2+n3/3
    print(avg)

def sumofNumbers(numlist):
    sum = 0
    for x in numlist:
        sum = sum + x
    print(sum)
    return sum
def avgNumbers(numlist):
    sum = sumofNumbers(numlist)
    print(sum/len(numlist))

def findValue(numlist,valueTofind):
    for x in numlist:
        if(x == valueTofind):
            return True
    return False


avgOfthree(20,20,55)
avgOfthree(25,45,56)
avgNumbers([20,25,45,56])
findValue([20,56,45],20)