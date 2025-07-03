import json

with open("json1.txt", "r") as file:
    data = json.load(file)

print(data)
print(data["hobbies"][0])

with open("json2.txt", "r") as file:
    people = json.load(file)
    
print(people["person"]["address"]["city"])

with open("json3.txt", "r") as file:
    people = json.load(file)
    
print(people["people"][1]["name"])
print(people["people"][1]["hobbies"][0])