class C:
    def __init__(self, list):
        self.list = list
    
    def m1(self, s,n):
        self.list[s] = n

    def m2(self, s):
        result = 0
        for key, value in self.list.items():
            if key in s:
                result += self.list[key]
        return result
    
stad = C({"A":120,"D":150,"G":90,"K":110})
stad.m1("G",130)
print(stad.m2("GD"))
print(stad.m2("KEJ"))