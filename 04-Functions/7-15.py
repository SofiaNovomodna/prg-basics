

def f(detector):
    #detector = str(detector)
    number = 0
    for char in detector:
        if char == '+': 
            number +=1
        else:
            number -=1
        if number >=3:
            return True
        else:
            continue
    return False
    

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))
