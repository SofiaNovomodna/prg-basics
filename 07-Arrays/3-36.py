def transform(arr):
    n_arr =[]
    for row in arr:
        for col in row:
            n_arr.append(col)
    return n_arr

print(transform([[2, 3],[
1, 5]]))
print(transform([[5, 0, 3, 7, 5],[
9, 0, 9, 1, 2]]))
print(transform([[2, 1],[
3, 5],[
7, 4],[
2, 6]]))