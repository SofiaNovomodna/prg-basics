arr = [[7, 3, 7, 9, 0],
[3, 8, 6, 4, 7],
[8, 7, 1, 1, 5]]

for row in arr:
    for ii in row:
        print(ii,end=' ')
    print()
print()
print()

for row in arr:
    rem = row[0]
    row[0]= row[len(row)-1]
    row[len(row)-1] = rem

for row in arr:
    for ii in row:
        print(ii,end=' ')
    print()