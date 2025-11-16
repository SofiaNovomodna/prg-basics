arr = [[7, 3, 7, 9, 0],
[3, 8, 6, 4, 7],
[8, 7, 1, 1, 5]]

for row in arr:
    for ii in row:
        print(ii,end=' ')
    print()
print()
print()
rem = arr[0]
arr[0]= arr[len(arr)-1]
arr[len(arr)-1] = rem

for row in arr:
    for ii in row:
        print(ii,end=' ')
    print()