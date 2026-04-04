
class ListStorage:

    def __init__(self):
        self.datalist = []

    def AddData(self,data):
        self.datalist.append(data)

    def printData(self):
        for student in self.datalist:
            print(student)



slist = ListStorage()
plsit = ListStorage()

slist.AddData("student")
slist.printData()

plsit.AddData("product")
plsit.printData()

