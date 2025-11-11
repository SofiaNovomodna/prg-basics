

def f(product_code):
    result = True
    if int(product_code[0])+int(product_code[1])+int(product_code[2])%7 !=int(product_code[3]):
        result = False
    return result
        
        
            

if __name__ == "__main__":
    print(f("1082"))  #True
    print(f("2035"))   #True
    print(f("1114"))   #False
    print(f("7071"))   #False