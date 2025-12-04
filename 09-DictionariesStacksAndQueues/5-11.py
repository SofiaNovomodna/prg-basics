import json

with open("voting.json", "r") as file:
    contex = json.load(file) 
    
vote = input('Enter name: ')
voted = False
for key, value in contex.items():
    if key == vote:
        n_value = value + 1
        contex[key]=n_value
        voted = True
        break
if voted == False:
    contex[vote]=1
    
with open("voting.json", "w") as file:
    json.dump(contex, file)

