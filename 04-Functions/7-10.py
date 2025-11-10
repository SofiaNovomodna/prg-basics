

def f(x,y):
    i = x
    result = 0
    while i<-1:
        i+=1
        if i%2==0:
            result +=1 
        else:
            continue
    return result

if __name__ == "__main__":
    print(f(-7,8))
    print(f(-1,11))