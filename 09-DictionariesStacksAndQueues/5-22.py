product = {}

# read product data from keyboard
product['name'] = input('Name: ')
product['price'] = float(input('Price (real number with two decimal places): '))
product['paid'] = bool(input('paid (True/False): ')) 
# save product data to json file

import json

with open('product.json', 'w') as file:
    json.dump(product, file, indent=4)