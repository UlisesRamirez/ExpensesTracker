import json
import math

outgoData = json.load(open('internalData/moneyInfo/uramirez.json', 'r'))

def clear(lane):
    outgoData[lane] = []
    with open('internalData/moneyInfo/uramirez.json', 'w') as file:
        json.dump(outgoData, file, ensure_ascii= False, indent= 4)

def current(lane):
    current, i = 0, 0
    while i < len(outgoData[lane]):
        current += outgoData[lane][i]["amount"]
        i += 1
    print('The total spent on this lane is: ' + str(current))

def averages():
    laneTotal, total = [], 0
    for item in outgoData:
        temp, i = 0, 0
        while i < len(outgoData[item]):
            total += outgoData[item][i]["amount"]
            temp += outgoData[item][i]["amount"]
            i += 1
        laneTotal.append(temp)
    indexer = 0
    while indexer < len(laneTotal):
        try:
            percentage = math.ceil(((laneTotal[indexer] * 100) / total) * 100) / 100
            print('the lane {} represents the {} of the total of {}'.format(laneTotal[indexer], percentage, total))
            indexer += 1
        except ZeroDivisionError:
            print('Math error, there is no values added.')
            print('add some expenses and try again... ')
            break

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
    "average": averages
}

lanes = ["travel", "lunchFood", "clubOutgo", "nightsOut", "games", "savedMoney", "others"]