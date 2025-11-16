
Tuple = (10,20,30,40,50)

print('Tuple:', end= ' ')
for i in Tuple:
    print(i, end= ', ')
print()

i=len(Tuple)-1
print('Reverse order:', end= ' ')
while i>=0:
    print(Tuple[i], end= ', ')
    i-=1
print()