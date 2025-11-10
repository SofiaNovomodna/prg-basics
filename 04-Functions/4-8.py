
def time_string(hours, minutes, time_format):
    if time_format == '24':
        if hours <10:
            time = '0'+ str(hours)
        else:
            time = str(hours)
    else:
        if 21>hours >12:
            hours = hours - 12
            time = '0'+ str(hours)
        elif hours >12:
            hours = hours - 12
            time = str(hours)
        if hours <10:
            time = '0'+ str(hours)
        else:
            time = str(hours)
    
    if int(minutes)<10:
        time += ':' +'0'+ str(minutes)
    else:
        time += ':' +str(minutes)

    return time

print (time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))

