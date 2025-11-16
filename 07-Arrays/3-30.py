arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

i =1
while i <= len(arr):
    for ii in range(0,len(arr)):
        arr[i-1][ii] += i*(ii+1)
    i+=1

for row in arr:
    for ii in row:
        print(ii,end='')
    print()
