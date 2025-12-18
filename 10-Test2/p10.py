def f(array):
    valid = False
    row = 0
    col = 0
    min = array[0][0]
    for r in array:
        for c in r:
            if c <= min:
                min = c
                if row == col:
                    valid = True
                else:
                    valid = False
            col +=1
        col = 0
        row +=1
    return valid


print(f([[7,8],[5,3],[9,4]]))#True     # 3, row 1, col 1 
print(f([[7,8,5,3],[9,4,2,6]]))#False  # 2, row 1, col 2