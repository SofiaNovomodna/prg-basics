class Statistics:
    def __init__(self):
        self.array = []
    
    def add(self, element):
        self.array.append(element)

    def info (self):
        for i in self.array:
            print(i,end=' ')
        print ()

    def max(self):
        max = self.array[0]
        for i in self.array:
            if i>max:
                max = i
        self.max = max
        print('Max: ',max)

    def min(self):
        min = self.array[0]
        for i in self.array:
            if i<min:
                min = i
        self.min = min
        print('Min: ',min)

    def arithmetic_mean(self):
        total = 0 
        for i in self.array:
            total += i
        self.arithmetic_mean = total/len(self.array)
        print('arithmetic_mean: ', total/len(self.array))

    def median(self):
        self.array.sort()
        if len(self.array)%2 == 1:
            print('median: ', self.array[len(self.array)//2])
            self.median = self.array[len(self.array)//2]
        else:
            print('median: ', self.array[len(self.array)//2-1], self.array[len(self.array)//2])
            self.median = [self.array[len(self.array)//2-1], self.array[len(self.array)//2]]

    def quantities(self):
        print(f'minimum {self.max}, maximum {self.min}, arithmetic mean {self.arithmetic_mean}, median {self.median}')



aa = Statistics()
aa.add(12)
aa.add(37)
aa.add(6)
aa.add(9)
aa.add(17)

aa.info()
aa.max()
aa.min()
aa.arithmetic_mean()
aa.median()
aa.quantities()