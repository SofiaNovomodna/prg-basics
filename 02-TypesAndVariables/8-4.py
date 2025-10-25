###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

# calculate the number of feet
inches_total = cm/2.54
feet = inches_total//12
inches = inches_total%12
#print
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')