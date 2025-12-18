def f(array2D):
    count = 0
    while count<=len(array2D)-1:
        col = 0
        for i in array2D:
            col += i[count]
        if col != sum(array2D[count]):
            return False
        count+=1
    return True


    


print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2,1],[4,2,5,1],[9,2,1,1]]))