arr=[-15, 8, -31, 47, -2, 19]

if arr[0]>arr[1]:
    min=arr[1]
else:
    min=arr[0]

for i in arr:
    if min>i:
        min=i

print(min)


if arr[0]>arr[1]:
    max=arr[0]
else:
    max=arr[1]

for i in arr:
    if max<i:
        max=i

print(max)