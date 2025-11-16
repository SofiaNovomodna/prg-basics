def identity_matrix(n):
    mat = []
    for i in range(0,n):
        add = []
        for ii in range(0,i):
            add.append(0)
        add.append(1)
        for ii in range(i,n-1):
            add.append(0)
        mat.append(add)
        add = []
    return mat

for row in identity_matrix(5):
    for ii in row:
        print(ii,end=' ')
    print()
