import json

outgoData = json.load(open('internalData/moneyInfo/uramirez.json', 'r'))

def updateData(typeOf, amount):
    try:
        outgoData[typeOf].append(amount)
        with open('internalData/moneyInfo/uramirez.json', 'w') as file:
            json.dump(outgoData, file, ensure_ascii= False, indent= 4)
        return True
    except KeyError:
        return False