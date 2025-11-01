#Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. Sample result:

#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.

age = int (input('Entera dogs age: '))
if age <=2:
    d_age = age *10.5
else:
    d_age = (age - 2)*4 + 2*10.5

print (f'Enter the dogs age in human years: {age}')
print (f'The dogs age in dogs years is {d_age} years')
