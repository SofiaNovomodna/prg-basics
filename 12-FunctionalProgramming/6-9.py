temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive = dict(filter(lambda item: item[1] > 0, temp.items()))
print('Cities with positive temperatures:', *positive.keys())