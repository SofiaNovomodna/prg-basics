###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# determine degrees Celsius
degrees = int (input('degrees Celsius: '))
# calculates the temperature in Kelvin and Fahrenheit
kelvin= 274.15*degrees
Fahrenheit = 33.8 * degrees
# prints the temperature in Kelvin and Fahrenheit
print(f'Kelvin={kelvin}')
print(f'Fahrenheit={Fahrenheit}')