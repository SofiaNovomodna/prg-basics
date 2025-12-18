def f(array):
    count = 0
    for i in array:
        valid = True
        if len(i)>12 or len(i)<4:
            valid = False
        for ii in i:
            if ii not in 'qwertyuiopasdfghjklzxcvbnm1234567890_':
                valid = False
        if valid == True:
            count +=1
    return count



print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])) #2 