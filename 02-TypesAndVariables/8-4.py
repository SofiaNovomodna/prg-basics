###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

# calculate the number of feet
feet = cm//30.48
inches = cm%30.48
#print
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')