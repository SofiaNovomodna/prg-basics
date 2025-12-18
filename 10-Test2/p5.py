def f(first_letter,last_letter):
    with open('data.txt') as file:
        context = file.read()
    
    words = context.split()
    count =0
    for i in words:
        if i[0] == first_letter and i[len(i)-1]== last_letter:
            count +=1
    return count

print(f('w', 'd'))