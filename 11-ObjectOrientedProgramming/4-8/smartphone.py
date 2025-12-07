from contact import Contact
from contact_list import Contact_List

phone = Contact_List()
phone.add(Contact('John Brown', 'brown@onet.pl', '555234000'))
phone.add(Contact('Anna May', 'am@o2.pl', '232000199'))
phone.add(Contact('George Small', 'smallg@google.pl', '222999100'))
phone.add(Contact('Paola Big', 'bigpaola@poczta.pl', '100200300'))
phone.info()