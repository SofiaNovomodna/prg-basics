
def f(number1,number2,number3):
    if number1 <= number2 <= number3:
        return number3 - number1
    elif number1 <= number3 <= number2:
        return number2 - number1
    elif number2 <= number1 <= number3:
        return number3 - number2
    elif number2 <= number3 <= number1:
        return number1 - number2
    elif number3 <= number1 <= number2:
        return number2 - number3
    elif number3 <= number2 <= number1:
        return number1 - number3

if __name__ == "__main__":
    print(f(7,4,9))
    print(f(2,12,8))
