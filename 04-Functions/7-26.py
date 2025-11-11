
def f(text):
    result =''
    for i in text:
        result = result + '-' + i
    result = result[1:len(result)]
    return result
        
        
            

if __name__ == "__main__":
    print(f("Univesity"))  #24
    print(f("UE"))   #48
    print(f("x"))   #48
    print(f(""))   #48
