# Assignment: Making Dictionaries
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def MakingDict(l1,l2):
    DictOutput = {}
    DictList = zip(l1,l2)
    DictOutput = dict(DictList)
    print DictOutput

MakingDict(name, favorite_animal)
