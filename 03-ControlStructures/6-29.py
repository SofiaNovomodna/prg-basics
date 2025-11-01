n = int(input('N: '))

print("Prime numbers: 2", end=" ")

count = 2 
number = 2
while count <= n:
    while number<=count:
        if count%number==0:
            break
        elif number==(count-1):
            print(count, end=" ")
            break
        else:
            number +=1
    number = 2
    count +=1



