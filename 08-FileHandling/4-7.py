import re
text = input('enter ')
vowels = re.findall('[AEIOUYaeiouy]', text)
print(len(vowels))