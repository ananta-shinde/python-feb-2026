
def isNumber(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def isValidAadhar(num):
    if(len(str(num)) == 12 and isNumber(num) ):
        return True
    else:
        return False


def isValidEmail(email):
    email = str(email)
    if(email.find("@") != -1 and email.find(".") != -1):
        return True
    else:
        return False


def isGmail(email):
    email = str(email)
    if(isValidEmail(email) and email.endswith("@gmail.com")):
        return True
    else:
        return False

print(isGmail("demo@gmail.com"))