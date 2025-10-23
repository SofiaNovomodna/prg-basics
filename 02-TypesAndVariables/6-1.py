###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Sofia'   # replace Anna with your name
surname = 'Novomodna' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(surname)+characters_in_name+1}') # with a space between name and surname