class Contact:
    def __init__(self,name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name:<15} {self.email:<25} {self.telephone}"

class Contact_List:
    def __init__(self):
        self.list = []

    def add(self, Contact):
        self.list.append(Contact)

    def info(self):
        for i in self.list:
            print(i)


phone = Contact_List()
phone.add(Contact('John Brown', 'brown@onet.pl', '555234000'))
phone.add(Contact('Anna May', 'am@o2.pl', '232000199'))
phone.add(Contact('George Small', 'smallg@google.pl', '222999100'))
phone.add(Contact('Paola Big', 'bigpaola@poczta.pl', '100200300'))
phone.info()