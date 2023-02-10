import json
from pprint import pprint


with open("data.json", encoding="UTF-8") as file:
   data = json.load(file)
print(type(data))
pprint(data)
