def reverse(word):
    import queue
    word = input('Enter: ')
    stack = queue.LifoQueue()
    for i in word:
        stack.put(i)
    n_word = ''
    while not stack.empty():
        n_word += stack.get()
    return n_word

print(reverse(1))
