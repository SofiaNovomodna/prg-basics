

def f(expression):
    i=0
    number1=int(expression[0])
    while i<len(expression)-1:
        i+=1
        operator = expression[i]
        i+=1
        number2=int(expression[i])
        if operator == '+':
            number1=number1+number2
        if operator == '-':
            number1=number1-number2
    return number1
        
        
            

if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))
