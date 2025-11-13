def bubbleSort(arr):
   n = len(arr)
   for i in range(0,n-1):
      for j in range(0,n-i-1):
         if arr[j] > arr[j+1]:
               rem = arr[j]
               arr[j] = arr[j+1]
               arr[j+1] = rem
   return arr

l=[8,7,6,5,4,3,10]
print(bubbleSort(l))