matrix =[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
#Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Print the modified array. Sample result:

#1 0 0
#0 1 0
#0 0 1
i=-1
for row in matrix:
    i+=1
    row[i] = 1

for row in matrix:
    for i in row:
        print(i, end=' ')
    print()
