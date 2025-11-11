
def f(dice):
    count1 = dice.count(dice[0])
    for char in dice[1:len(dice)-1]:
        count2 = dice.count(char)
        if count2 >= count1:
            count1 = count2
            most = char
    return most
        
        
            

if __name__ == "__main__":
    print(f("5233165554211"))  #5
    print(f("2133"))   #3
