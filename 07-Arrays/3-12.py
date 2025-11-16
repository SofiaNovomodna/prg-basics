#Array: 2 3 2 5 8 1 9 8
#Unique elements: 3 5 1 9
arr = [2, 3, 2, 5, 8, 1, 9, 8]

print('Array:', end= ' ')
for i in arr:
    print(i, end= ' ')
print()

print('Unique elements:', end= ' ')
i=0
ii=0
un = True
while i<len(arr):
    
    while ii < len(arr):
        if i == ii:
            ii+=1
            continue
        else:
            if arr[i]==arr[ii]:
                un = False
        ii+=1
    if un == True:
        print(arr[i], end=' ')
    i+=1
    ii=0
    un = True

