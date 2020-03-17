import json
import math

outgoData = json.load(open('internalData/moneyInfo/uramirez.json', 'r'))

def clear(lane):
    print('clear')

def current(lane):
    current = 0
    for item in outgoData[lane]:
        current += outgoData[lane][item]["amout"]
    print('The total spent on this lane is: ' + current)

def close(lane):
    print('Ending session... ')
    exit()

def averages(lane):
    laneTotal, total, indexer = [], 0, 0
    while indexer < len(outgoData):
        temp = 0
        for j in outgoData[indexer]:
            total += outgoData[indexer][j]["amount"]
            temp += outgoData[indexer][j]["amount"]
        laneTotal.append(temp)
        indexer += 1
    secondIndexer = 0
    while secondIndexer < len(laneTotal):
        percentage = math.ceil(((laneTotal[secondIndexer] * 100) / total) * 100) / 100
        print('the lane {} represents the {} of the total of {}'.format(laneTotal[secondIndexer], percentage, total))
        secondIndexer += 1

def attachData(typeOf, amount, description):
    try:
        outgoData[typeOf].append({"amount": int(amount), "description": description})
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