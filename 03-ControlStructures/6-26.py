
i=0

while i<3:
    i+=1
    code = input ('Enter the PIN code:')
    if str(code) == '0805':
        print ('Correct')
        break
    else:
        print ('Incorrect...')
if i==3:
    print('Sorry, your payment card has been blocked.')


