def bubblesort(array):
   n = len(array)
   for i in range(0,n-1):
      for j in range(0,n-i-1):
         if array[j] > array[j+1]:
               rem = array[j]
               array[j] = array[j+1]
               array[j+1] = rem
   return array

print(bubblesort([15,4,12,14,7]))
print(bubblesort([14,10,5,6,2]))
print(bubblesort([7,5,9,10,14]))