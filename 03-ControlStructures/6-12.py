
Number = int (input('Number of products purchased: '))
price = int (input('Product price: '))
if Number >2:
    Amount = 0.75 * Number* price
    print (f'Amount to pay: {Amount}')
else:
    Amount = Number* price
    print (f'Amount to pay: {Amount}')