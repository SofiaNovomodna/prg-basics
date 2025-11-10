def f(number, even):
    result = 0
    if even == True:
        for char in str (number):
            char = int(char)
            if char%2 == 0:
                result += char
            else:
                continue
    if even == False:
        for char in str (number):
            char = int(char)
            if char%2 != 0:
                result += char
            else:
                continue
    return result

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))