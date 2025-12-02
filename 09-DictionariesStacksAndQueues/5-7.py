hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    list = []
    for hotel in hotels:
        list.append(hotel['name'])
    return list
def avg_price(hotels):
    total = 0
    count = 0
    for hotel in hotels:
        total += hotel['price']
        count += 1
    return total //count

print('Hotels in Krakow: ',end='')
for i in hotel_list(hotels_in_Krakow):
    print (i,end=',')
print()
print('Average hotel price in Krakow: ',avg_price(hotels_in_Krakow))
print('Hotels in Sopot: ',end='')
for i in hotel_list(hotels_in_Sopot):
    print (i,end=',')
print()
print('Average hotel price in Sopot: ',avg_price(hotels_in_Sopot))
print('Cheaper hotels in: ',end='')
if avg_price(hotels_in_Krakow)<avg_price(hotels_in_Sopot):
    print('Krakow')
elif avg_price(hotels_in_Krakow)>avg_price(hotels_in_Sopot):
    print('Sopot')