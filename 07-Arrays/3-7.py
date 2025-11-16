arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
Longest = len(arr[0])
Longest_name = arr[0]
for name in arr:
    if len(name)>Longest:
        Longest = len(arr[0])
        Longest_name = name

print('Names: ', end= ' ')
for i in arr:
    print(i, end= ' ')
print()
print('Longest name: ', Longest_name)
