from functools import reduce

numbers = [2,4,6,3,7,5]

print(reduce(lambda x,y: x+y, filter(lambda x: x%2==0, numbers)))