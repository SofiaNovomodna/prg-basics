arr=[2, 6, 4, 9, 7]

def star(n):
    print (n, ': ', end='')
    for i in range(0,n):
        print ('*', end='')
    print()

for i in arr:
    star(i)
