###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    letter = ord(char)
    if letter == 32:
        encrypted_text = encrypted_text + char
    else:
        # add one to the character's code
        letter = letter +1 
        # replace new character code with its
        # corresponding character (use chr())
        char = chr(letter)
        # add encrypted character to encrypted text
        encrypted_text = encrypted_text + char

print(plain_text)
print(encrypted_text)