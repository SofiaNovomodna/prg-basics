#Enter the amount in PLN: 18
#The amount of PLN 18 in coins:
#5 PLN coins: 3
#2 PLN coins: 1
#1 PLN coins: 1

amount = int(input('Enter the amount in PLN:'))

coin_5 = amount//5
coin_2 = (amount%5)//2
coin_1 = (amount%5)%2

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coin_5}')
print(f'2 PLN coins: {coin_2}')
print(f'1 PLN coins: {coin_1}')