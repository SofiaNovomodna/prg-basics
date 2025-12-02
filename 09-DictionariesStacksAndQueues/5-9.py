with open('vehicle.txt') as file:
    content = file.read()
cars = content.splitlines()

import csv
with open('province.csv') as file:
    context = csv.reader(file)
    headers = next(context)
    for row in context:
        count = 0
        for car_n in cars:
            if car_n[0] == row[headers.index('Letter')]:
                count +=1
        print(row[headers.index('Name')],':', count)