import json

outgoData = json.load(open('internalData/moneyInfo/uramirez.json', 'r'))

def clear(lane):
    print('clear')

def current(lane):
    print('current')

def close(lane):
    print('exit')

def averages(lane):
    print('total averages')
    
def updateData(typeOf, amount):
    try:
        outgoData[typeOf].append(amount)
        with open('internalData/moneyInfo/uramirez.json', 'w') as file:
            json.dump(outgoData, file, ensure_ascii= False, indent= 4)
        return True
    except KeyError:
        return False

functionsList = {
    "clear": clear,
    "current": current,
    "exit": close,
    "average": averages
}

lanes = ["travel", "lunchFood", "clubOutgo", "nightsOut", "games", "savedMoney", "others"]