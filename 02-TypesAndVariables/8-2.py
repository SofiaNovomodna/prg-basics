###
# Calculation of circle area and circumference 
#

# determine radius and PI values
import math
radius = int (input('radius: '))
pi = 3.14
# calculate area
area =  radius ** 2 * pi
# calculate circumference 
circumference = 2 * pi * radius
# print results
print (f'area: {area}')
print (f'circumference: {circumference}')