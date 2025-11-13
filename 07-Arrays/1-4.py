
###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('last value', arr[-1])
print('last value', arr[len(arr)-1])
print('sum of the first and last value', arr[0]+arr[len(arr)-1])
print('middle value', (arr[1]+arr[0]+arr[2]+arr[3]+arr[4])/5)
for i in range(0, len(arr)-1):
    print(arr[i], end= ' ')

