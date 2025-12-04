import json

with open('dogs.json', 'r',encoding='utf-8') as file:
    data = json.load(file)

for dog in data:
    for key, value in dog.items():
        if dog['age']<5:
            print(key, ':', value)
    print()
