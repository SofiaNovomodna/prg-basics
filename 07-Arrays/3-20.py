arr = [7,9,2,4,5,6]
s_arr =[]
for i in arr:
    if i%2==0:
        s_arr.append(i)
for i in arr:
    if i%2!=0:
        s_arr.append(i)
print(arr)
print(s_arr)