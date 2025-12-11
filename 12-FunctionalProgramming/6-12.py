medals = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

more_than_10 = list(filter(lambda country: country['gold']+country['silver']+country['bronze'] >10,medals))

for i in more_than_10:
    for ii in i.values():
        print(ii, end=' ')
    print()