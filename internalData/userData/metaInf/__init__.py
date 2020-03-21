import json

data = ''
with open('internalData/userData/metaInf/users.json', 'r') as file:
    data = json.load(file)

def addNewUser(load):
    with open('internalData/userData/metaInf/users.json', 'w') as file:
        json.dump(load, file, ensure_ascii= False, indent= 4)