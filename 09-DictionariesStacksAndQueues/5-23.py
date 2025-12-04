import json

with open('euro.json', 'r') as file:
    data = json.load(file)

print("Date           Buying Rate     Selling Rate")
print("============================================")

data = data['rates']
for exchange in data:
    date =exchange['effectiveDate']
    br = exchange['bid']
    sr = exchange['ask']
    print(f"{date:<15}{br:<16}{sr}")