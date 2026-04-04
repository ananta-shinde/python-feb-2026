num = 100
def firstFun():
    num = secondFun()
    print("I am first function")
    return num
def secondFun():
    num = thirdFun()
    print("I am second function")
    return num

def thirdFun():
    num = 100
    num = num +1
    print("I am third function")
    return num

num = firstFun()
print(num)