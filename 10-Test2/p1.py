def f(player1, player2):
    def hand_value(hand):
        total = 0
        for i in hand:
            if i in '23456789':
                total += int(i)
            elif i in ('1', 'A', 'J','Q', 'T'):
                total += 10
            elif i == '0':  # optional, if you want to skip zeros
                continue
        return total

    p1 = hand_value(player1)
    p2 = hand_value(player2)

    return p1 >= p2

print(f('AJ972','AQT72'))  
print(f('9532','K8'))      

