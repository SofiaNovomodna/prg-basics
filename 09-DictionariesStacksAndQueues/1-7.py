prod = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for name, count in prod.items():
    print (f'{name} : {count}')

total = 0
for count in prod.values():
    total += count

print (total)
