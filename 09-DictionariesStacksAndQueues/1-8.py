
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

#prints a list of products and their prices before the discount
for name, count in price_list.items():
    print (f'{name} : {count}')
#prints the total value of the products before the discount
total = 0
for count in price_list.values():
    total += count
print (round(total,2))
#modifies the price list according to the discount (round prices to two decimal places)
for name, price in price_list.items():
    price = round(price * 0.9, 2)
    price_list[name] = price
#prints a list of products and their prices after the 10% discount
for name, count in price_list.items():
    print (f'{name} : {count}')
#prints the total value of the products after the discount
total = 0
for count in price_list.values():
    total += count
print (round(total,2))