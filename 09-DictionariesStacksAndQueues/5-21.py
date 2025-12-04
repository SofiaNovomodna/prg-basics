import json

data = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "genre": "Science Fiction",
    "main_characters": ["Cooper", "Murph", "Brand"]
}

with open('favourite.json', 'w') as file:
    json.dump(data, file, indent=4)