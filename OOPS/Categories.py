class Category:
    # categoryList = []

    def __init__(self):
        self.categoryList = []

    def addCategory(self,name):
        self.categoryList.append(name)

    def printCategories(self):
        for cat in self.categoryList:
            print(cat)
