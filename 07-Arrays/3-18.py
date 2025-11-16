

arr=[7,3,8,5,2]
s_arr = arr.copy()
print('Numbers:', end= ' ')
for i in arr:
    print(i, end= ', ')
print()

def bubblesort(array):
   n = len(array)
   for i in range(0,n-1):
      for j in range(0,n-i-1):
         if array[j] > array[j+1]:
               rem = array[j]
               array[j] = array[j+1]
               array[j+1] = rem
   return array

s_arr = bubblesort(s_arr)
print('Second largest number:', s_arr[len(s_arr)-2]) 
print('Median:', arr[len(arr)//2])
print('Smallest and largest number:',s_arr[0], s_arr[len(s_arr)-1])
print('Numbers as a string:', end= ' ')
for i in arr:
    print(i, end= '-')
print()