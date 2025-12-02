import queue

number = queue.LifoQueue()

n=int(input('Natural number: '))

while n!=0:
    rem = n%2
    number.put(rem)
    n = n//2

print('Binary number: ', end='')
while not number.empty():
    print(number.get(),end='')