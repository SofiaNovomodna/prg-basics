for i in range(6,-1,-3):
    for j in range(1,4):
        print(f'{i+j}',end=' ')
    print()


ii=6
jj=1
while ii>-1:
    while jj!=4:
        print (f'{ii+jj}',end=' ')
        jj+=1
    print()
    jj=1
    ii-=3