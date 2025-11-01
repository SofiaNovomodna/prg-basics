
c_price = int (input('Current product price: '))
p_price = int (input('Previous product price: '))
sale = 100 - (c_price / p_price*100)
if sale >=10:
    print (f'Buy the product!!')
    print (f'Product price reduced by {sale}%')