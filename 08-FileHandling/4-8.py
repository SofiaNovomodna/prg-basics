import re
with open('files.txt') as file:
    context = file.read()
ext = re.findall('.+\..{4}',context)
for el in ext:
    print(el)