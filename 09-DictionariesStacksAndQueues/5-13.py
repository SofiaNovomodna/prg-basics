import queue

stack = queue.LifoQueue()
while True:
    enter = input('Enter number/sign: ')
    if enter in {'1','2','3','4','5','6','7','8','9','0'}:
        stack.put(enter)
    elif enter in {'+','-','*','/'}:
        n1 = int(stack.get())
        if stack.empty():
            stack.put(n1)
            print('Error')
        n2 = int(stack.get())
        if enter == '+':
            result = n1+n2
        elif enter == '-':
            result = n1-n2
        elif enter == '*':
            result = n1*n2
        elif enter == '/':
            result = n1/n2
        else:
            print('Error')
        stack.put(result)
    elif enter == '=':
        alelua = stack.get()
        if not stack.empty():
            print('Error')
        else:
            print(alelua)
        break

