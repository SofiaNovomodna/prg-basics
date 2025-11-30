#File name: books.txt
#Number of lines: 14
#Number of characters: 2540
#Number of words: 703
import re

try:
    with open(input('File name: ')) as file:
        context = file.read()
except FileNotFoundError:
    print(f"Hey! The file does not exist.")

lines = context.splitlines()
print ('Number of lines: ', len(lines))

char = re.findall('\w', context)
print ('Number of characters: ', len(char))

words = re.findall('[a-zA-Z]+', context)
print ('Number of words: ', len(words))