#existed array: 15 8 31 47 2 19 
#reverse array: 19 2 47 31 8 15
ex_arr = [15, 8, 31, 47, 2, 19 ]

print('existed array:', end=' ')
for i in ex_arr:
    print (i, end=' ') 
print()
print('reverse array:', end=' ')
i = len(ex_arr)-1
while i>=0:
    print (ex_arr[i], end=' ') 
    i-=1