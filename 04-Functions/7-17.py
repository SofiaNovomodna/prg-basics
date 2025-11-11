def f(palindrome):
    palindrome = str(palindrome)
    backwards = ''
    i= len(palindrome)-1
    while i !=-1:
        backwards += palindrome[i]
        i-=1
    if backwards == palindrome:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))
