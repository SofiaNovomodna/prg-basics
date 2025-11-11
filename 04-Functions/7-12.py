

def f(n):
    result = '*'
    for i in range (n-1):
        result += '/*'
    return result

if __name__ == "__main__":
    print(f(4))
    print(f(1))