import queue

customer_queue = queue.Queue()
customer_queue1 = queue.Queue()
number = 1
while True:
    print('1 - New customer')
    print('2 - Customer served')
    print('3 - Queue')
    print('0 - Exit')
    choice = input('')
    if choice == '1':
        customer_queue.put(number)
        number +=1
    elif choice == '2':
        customer_queue.get()
    elif choice == '3':
        while not customer_queue.empty():
            customer = customer_queue.get()
            print (customer, end=' ')
            customer_queue1.put(customer)
        while not customer_queue1.empty():
            customer = customer_queue1.get()
            customer_queue.put(customer)
        print ()
    elif choice == '0':
        break
