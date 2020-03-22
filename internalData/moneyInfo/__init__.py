import json
import math

class Session():
    def __init__(self, user):
        self.path = 'internalData/moneyInfo/DataBases/' + str(user) + '.json'
        try:
            with open(self.path, 'r') as file:
                self.outgoData = json.load(file)
        except FileNotFoundError:
            print('creating new database')
            with open(self.path, 'w+') as file:
                baseJson = {
                    "travel": [],
                    "lunchFood": [],
                    "clubOutgo": [],
                    "nightsOut": [],
                    "games": [],
                    "savedMoney": [],
                    "others": [] }
                json.dump(baseJson, file, ensure_ascii= False, indent= 4)
            with open(self.path, 'r') as file:
                self.outgoData = json.load(file)
        self.lanes = ["travel", "lunchFood", "clubOutgo", "nightsOut", "games", "savedMoney", "others"]

    def clear(self, lane):
        self.outgoData[lane] = []
        with open(self.path, 'w') as file:
            json.dump(self.outgoData, file, ensure_ascii= False, indent= 4)

    def current(self, lane):
        current, i = 0, 0
        while i < len(self.outgoData[lane]):
            current += self.outgoData[lane][i]["amount"]
            i += 1
        print('The total spent on this lane is: ' + str(current))

    def close(self):
        print('Ending session... ')
        exit()

    def helpLines(self):
        print('Help') # Format the help pages

    def averages(self):
        laneTotal, total = [], 0
        for item in self.outgoData:
            temp, i = 0, 0
            while i < len(self.outgoData[item]):
                total += self.outgoData[item][i]["amount"]
                temp += self.outgoData[item][i]["amount"]
                i += 1
            laneTotal.append(temp)
        indexer = 0
        while indexer < len(laneTotal):
            try:
                percentage = math.ceil(((laneTotal[indexer] * 100) / total) * 100) / 100
                print('the lane {} represents the {}% of the total of {}'.format(self.lanes[indexer], percentage, total))
                indexer += 1
            except ZeroDivisionError:
                print('Math error, there is no values added.')
                print('add some expenses and try again... ')
                break

    def attachData(self, typeOf, amount, description):
        self.outgoData[typeOf].append({"amount": int(amount), "description": description})
        with open(self.path, 'w') as file:
            json.dump(self.outgoData, file, ensure_ascii= False, indent= 4)
    
    functionsList = {
        "help": helpLines,
        "exit": close,
        "clear": clear,
        "current": current,
        "averages": averages
    }