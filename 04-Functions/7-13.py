def f(n):
    result = ''
    for i in range (n+1):
        if i ==0:
            continue
        else:
            result += str (i)
    return result

if __name__ == "__main__":
    print(f(11))
    print(f(4))