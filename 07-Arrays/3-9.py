
def compare(array1, array2):
    same = True
    if len(array1)!=len(array2):
        same = False
    i =0 
    if same == True:
        while i<len(array1):
            if array1[i]!=array2[i]:
                same = False
            i+=1
    

    print('Array1: ', end= ' ')
    for i in array1:
        print(i, end= ' ')
    print()
    print('Array2: ', end= ' ')
    for i in array2:
        print(i, end= ' ')
    print()
    print('Comparison: ', end= ' ')
    if same == True:
        print('arrays are the same')
    else:
        print('arrays are not the same')
    print()


compare(["water","book","sky"] ,  ["water","book","sky"])
compare([True,False]  , [True,False,True])
compare([5,3,1]  , [5,2,1])
compare([3,2,1] ,  [3,2])
