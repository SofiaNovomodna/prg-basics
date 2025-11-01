
time_24 = input('Enter time (24-hour format): ')

if int (time_24[0:2]) >12:
    print (f'Time in 12-hour format: {int (time_24[0:2])-12}:{time_24[3:5]} pm')
else:
    print (f'Time in 12-hour format: {time_24} am')