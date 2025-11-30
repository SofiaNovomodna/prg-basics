with open('it_company.csv') as file:
    content = file.read()
content = content.splitlines()

i=1
for line in content:
    if i == 6:
        input('press enter')
        i=1
        continue
    print(line)
    i+=1