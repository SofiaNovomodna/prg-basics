import json

with open('reservations.json', 'r')as file:
    data = json.load(file)

data = data['reservations']

def number_of_rooms(data):
    print(len(data))

def number_of_paid_reservations(data):
    for room in data:
        if room['paid'] == True:
            print(room['room_number'])

def nnumber_of_unpaid_reservations(data):
    count = 0
    for room in data:
        if room['paid'] == False:
            print(room['room_number'])

def total_value_of_paid_reservations(data):
    count = 0
    for room in data:
        if room['paid'] == True:
            count +=1
    print(count)

def total_value_of_unpaid_reservations(data):
    count = 0
    for room in data:
        if room['paid'] == False:
            count +=1
    print(count)

number_of_rooms(data)
print()
number_of_paid_reservations(data)
print()
nnumber_of_unpaid_reservations(data)
print()
total_value_of_paid_reservations(data)
print()
total_value_of_unpaid_reservations(data)
print()