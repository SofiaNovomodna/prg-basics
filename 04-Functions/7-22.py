

def f(name):
    result =''
    result += name[0]
    i=-1
    for char in name:
        i+=1
        if char == ' ':
            result += name[i+1]
    return result
            

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
