emp = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

print(list(map(lambda employee: f'{str(employee[0]).upper()}, {employee[1]}', emp)))