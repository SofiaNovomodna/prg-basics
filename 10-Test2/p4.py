def f(subjects):
    name = ''
    av = 0
    for key, value  in subjects.items():
        if sum(value)/len(value) >av:
            av = sum(value)/len(value) 
            name = key
    return name




print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}) )  #"comp" 