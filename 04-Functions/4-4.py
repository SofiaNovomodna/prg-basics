# Take an integer input from the user. The number can be positive, negative, or zero.
# Handle Negative Numbers: Convert the number to its absolute value using the abs() function. This step ensures the algorithm correctly processes negative numbers by ignoring the negative sign.
# Convert to String: Convert the number to a string using str(). This allows iteration over each digit in the number.
# Iterate Over Digits:
# Loop through each character (digit) in the string representation of the number.
# Convert each character back to an integer.
# Sum Digits: Add each integer value to a running total.
# Output the Result: Return the sum of the digits
###
# Calculates the sum of the digits in a number
#
import math

def sum_digits(number):
    total =0
    number=abs(number)
    number =str(number)
    for char in number:
        digit = int(char)
        total += digit
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')