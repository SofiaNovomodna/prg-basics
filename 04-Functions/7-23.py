

def f(password):
    for char in password:
        count = password.count(char)
        if count >1:
            return False
    if len(password)<6:
        return False
    return True
        
            

if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))