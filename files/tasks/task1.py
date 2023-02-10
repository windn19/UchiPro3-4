import json

with open('starwars.json') as file:
    data = json.load(file)

characters = set()
for film in data['results']:
    characters.update(film['characters'])

print(len(characters))
