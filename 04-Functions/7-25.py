
def f(x,y):
    result =0
    for i in range (x-1,y+1):
        if i%6==0 and i%4!=0:
            result+=i
    return result
        
        
            

if __name__ == "__main__":
    print(f(1,20))  #24
    print(f(10,30))   #48