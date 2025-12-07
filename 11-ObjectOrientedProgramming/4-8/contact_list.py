
class Contact_List:
    def __init__(self):
        self.list = []

    def add(self, Contact):
        self.list.append(Contact)

    def info(self):
        for i in self.list:
            print(i)