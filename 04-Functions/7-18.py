
def f(sentence):
    result = ''
    for char in sentence:
        if char == ' ':
            continue
        else:
            result+=char
    return result

if __name__ == "__main__":
    print(f("integrated development environmen"))
    print(f("A programming language is a system of notation for writing"))
