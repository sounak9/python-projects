def biggest(aDict):
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

print(biggest({"L":['Lion'],'D':['Donkey','Deer'],'E':['Elephant']}))