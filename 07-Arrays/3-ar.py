import random
arr1 = [3,7,1,0,4]
print(arr1)
arr2 = [[2,3],[7,1],[0,4]]
print(arr2)
arr3 = [7 for i in range(5)]
print(arr3)
arr4 = [i for i in range(1,10)]
print(arr4)
arr5 = [i*2 for i in range(1,10)]
print(arr5)
arr6 = [random.randint(1,20) for i in range(10)]
print(arr6)
arr7 = [[] for i in range(5)]
print(arr7)
arr8 = [[1 for i in range(2)] for j in range(4)]
print(arr8)
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(arr9)
#an array with values: 4,0,3
arr1 = [4,0,3]
print(arr1)
#15-element array filled with zeros
arr3 = [0 for i in range(15)]
print(arr3)
#an array with integer values in the range of <1,30>
arr4 = [i for i in range(1,30)]
print(arr4)
#20-element array filled with 0 or 1 randomly
arr4 = [random.randint(0,1) for i in range(20)]
print(arr4)
#two dimensional array with five rows and two columns filled with False
arr4 = [[False for i in range(2)] for i in range(5)]
print(arr4)