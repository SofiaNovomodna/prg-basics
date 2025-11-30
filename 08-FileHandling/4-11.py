with open('powers.txt', 'w') as file:
    for i in range (1,101):
        line = f'{i}, {i*i}, {i*i*i} \n'
        file.write(line)
        