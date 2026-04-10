from pandas import Period


class Person:

    def __init__(self,prn):
        self.__prn = prn
        self.__name = None
        self.email = None
        self.password = None

    def getName(self):
        return self.__name

    def setName(self,name):
        if(isinstance(name,(str))):
            self.__name = name

    def getPrn(self):
        return self.__prn


p1 = Person(221212212)
p1.email = "54545545454"
p1.setName("Ananta")

p2 = Person(5454545)
print(p2.getPrn())

print(p1.getPrn())

