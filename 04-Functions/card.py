def hide(card_number):
    card_number = str(card_number)
    result = ''
    for i in range(len(card_number)):
        if i < 2 or i >= len(card_number) - 4:
            result += card_number[i]
        else:
            result += '*'
    return result