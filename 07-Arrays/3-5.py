arr = [15, 8, 31, 47, 2, 19]

for i in arr:
    print(i, end= ' ')

print()
sum=0
for i in arr:
    sum+=i
print(sum/len(arr))