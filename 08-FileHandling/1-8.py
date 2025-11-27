def read(name):
    with open(name) as file:
        content = file.read() 
    return content

content = read('pets.txt')
words = content.split()
print(len(words))