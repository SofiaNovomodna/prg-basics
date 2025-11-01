
hours = int (input('Enter hours: '))
fee = 0

if 1<= hours <=2:
    fee = 5
elif 3<= hours <=6:
    fee = 15
elif 6< hours :
    fee = 20

print(f'Your fee: {fee}')