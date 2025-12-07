class C:
    def __init__ (self, array):
        self.array = array
    
    def m(self, n):
        count = 0
        for i in self.array:
            count_or = True
            for ii in i:
                if ii<=0:
                    count_or = False
            if count_or == True:
                count += 1
        if count >= n:
            return True
        else:
            return False


array = C([[2,3],[1,8],[-6,4],[3,-7]])  
print(array.m(2))
print(array.m(3))

