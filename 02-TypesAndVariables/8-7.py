###
# The program reads an integer number and prints
# its binary and hexadecimal representation.
#

number = int(input('Enter number: '))

# convert to binary and hexadecimal using built-in functions
binary_number = bin(number)
hexadecimal_number = hex(number)

# print results
print(f'Binary number: {binary_number}')
print(f'Hexadecimal number: {hexadecimal_number}')