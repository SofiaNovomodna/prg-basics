def f(binary_number):
    binary_number = str(binary_number)
    for char in binary_number:
        if char != '1' and char != '0':
            return False
        else:
            continue
    return True

print (f('1311a10100'))
print (f('11100001'))