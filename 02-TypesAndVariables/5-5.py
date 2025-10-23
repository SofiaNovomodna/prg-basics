price = input('Enter price=')
price = int (price)
discount = input('Enter discount %=')
discount = int (discount)
Reduction = discount/100*price
Price_with_discount= price-Reduction
print (f'Enter price: {price}')
print (f'Enter discount %: {discount}')
print (f'Price with discount: {Price_with_discount}')
print (f'Reduction: {Reduction}')
