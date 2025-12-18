Tuple = (50,20,40,50,30,50)
print('Tuple:', end= ' ')
for i in Tuple:
    print(i, end= ', ')
print()
Value = int(input('Value: '))
Number_of_occurrences = 0

for i in Tuple:
    if i == Value:
        Number_of_occurrences +=1
print('Number of occurrences: ', Number_of_occurrences)

