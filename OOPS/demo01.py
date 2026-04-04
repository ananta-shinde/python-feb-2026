
categories = []

def addCategory(name):
    categories.append(name)
def updateCategory(index,newname):
    categories[index] = newname
def renameCategory(oldname,newname):
    index = indexOf(oldname)
    if(index != -1):
        categories[index] = newname
    else:
        print("category does not exist")
def indexOf(name):
    for index in range(len(categories)):
        if(categories[index] == name):
            return index
    return -1

