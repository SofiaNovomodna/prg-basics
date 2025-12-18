def f(exp):
    import queue
    list = queue.LifoQueue()
    
    for i in exp.split():
        if i == '+' or i == '-':
            n1 = list.get()
            n2 = list.get()
            if i == '+':
                res = n2 + n1
                list.put(res)
            elif i == '-':
                res = n2 - n1
                list.put(res)
        else:
            i = int(i)
            list.put(int(i))

    return list.get()


print(f("2 3 +"))# 5 
print(f("2 6 + 4 5 - +") )# 7 
print(f("11 7 + 15 - 14 +") )#17 