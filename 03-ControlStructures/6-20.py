
#Enter decimal number: 12
#12(10) = 1100(2)
import math
number = int(input('Enter decimal number:'))
q = 0
num = 0
i=0
n=number

while number !=0:
    num = number%2
    q += num*10**i
    number = number//2
    i+=1


q = str(q)
i=len(q)-1

res=''
while i>=0:
    res += q[i]
    i=i-1



print (f'{n}(10) = {res}(2)')
    

