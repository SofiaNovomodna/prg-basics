i=0
while i<30:
    i+=1
    if i%3==0:
        print ('THREE')
        if i%5 ==0:
            print('BINGO!!')
    elif i%5 ==0:
        print('FIVE')
    else:
        print(i)