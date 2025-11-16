arr=[7,3,8,5,2]
n = int(input('Enter: '))
print('Array:', end= ' ')
for i in arr:
    print(i, end= ', ')
print()
for i in arr:
    if i > n:
        print(i, end= ', ')
print()
