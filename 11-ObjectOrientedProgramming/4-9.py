class C:
    def __init__(self,name, surname, age, seniority ):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        if self.age < 18:
            result = f'{str(self.surname).lower()}{str(self.name)[0].lower()}{self.seniority}'
        else:
            result = f'{str(self.surname).upper()}{str(self.name)[0].upper()}{self.seniority}'
        return result

print( C("Anna","May",17,7))
print( C("George","Brown",21,4))
