
def letter(frase, letter):
    result = 0
    for char in frase:
        if char == letter:
            result +=1
    return result