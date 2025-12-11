avg_speed = lambda distance,hours,minutes: (distance/(hours+minutes/60))


n1 = int(input('Enter distance in km: '))
n2 = int(input('Enter number of travel hours: '))
n3 = int(input('Enter number of travel minutes: '))

print(f'Average speed: {avg_speed(n1,n2,n3):.1f} km/h')