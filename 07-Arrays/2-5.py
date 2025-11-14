# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   return len(seats)*len(seats[0])

def seats_available(seats):
   av =0 
   for row in seats:
      for place in row:
         if place == 'A':
            av += 1
   return av

def seats_booked(seats):
   booked =0 
   for row in seats:
      for place in row:
         if place == 'B':
            booked += 1
   return booked

def seat_status(seats, row, place):
   for row1 in seats:
       if seats[row-1]== row1:
           if row1[place-1] =='B':
              return 'booked'
           else:
                return 'available'
   


print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))