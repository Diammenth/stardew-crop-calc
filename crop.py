import json
class Crop:
    def __init__(self,entry):
        self.name = entry["name"]
        self.seedPrice = entry["seedPrice"]
        self.sellPrice = entry["sellPrice"]
        self.isRepeat = entry["isRepeat"]
        if self.isRepeat == True:
            self.repeatInterval = entry["repeatInterval"]
        self.growthInterval = entry["growthInterval"]
        self.seasons = entry["seasons"]
        self.cropType = entry["cropType"]
        self.keg = entry["keg"]
        self.preserves = entry["preserves"]
        if self.cropType == "fruit":
            self.dehydrator = entry["dehydrator"]
        self.jsonInfo = entry


    def get_rarity_value(self,tier: int) -> int: #returns the price of the crop in a specific rarity 0 = normal; 1 = silver; 2 = gold; 3 = iridium
        match tier:
            case 1:
                return int(self.sellPrice*1.25)
            case 2:
                return int(self.sellPrice*1.5)
            case 3:
                return int(self.sellPrice*2)
            case _:
                return int(self.sellPrice)


    def get_harvests(self,seasons: int) -> int: #returns the amount of harvests in a specific period of seasons
        if self.isRepeat == False:
            return (28*seasons)//self.growthInterval
        else:
            return (((28*seasons)-self.growthInterval)//self.repeatInterval)+1



