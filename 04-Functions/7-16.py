
def f(number):
    #number = int (number)
    n=0
    m=1
    if number%2==0:
        for i in range((number//2)-1):
            n= m+n
            m = n+m
        return m
    else:
        for i in range((number//2)):
            n= m+n
            m = n+m
        return n

    

if __name__ == "__main__":
    print(f(5))
    print(f(9))
    print(f(4))
