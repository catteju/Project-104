import csv
from collections import Counter
with open('Height.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))

data = Counter(newData)
modeDataForRange = {
    "75-85": 0,
    "85-95" : 0,
    "95-105" : 0,
    "105-115": 0,
    "115-125" : 0,
    "125-135" : 0,
    "135-145": 0,
    "145-155" : 0,
    "155-165" : 0,
    "165-175" : 0
}

for height,occurence in data.items():
    if 75<float(height)<85:
        modeDataForRange["75-85"] += occurence
    elif 85<float(height)<95:
        modeDataForRange["85-95"] += occurence
    elif 95<float(height)<105:
        modeDataForRange["95-105"] += occurence
    elif 105<float(height)<115:
        modeDataForRange["105-115"] += occurence
    elif 115<float(height)<125:
        modeDataForRange["115-125"] += occurence
    elif 125<float(height)<135:
        modeDataForRange["125-135"] += occurence
    elif 135<float(height)<145:
        modeDataForRange["135-145"] += occurence
    elif 145<float(height)<155:
        modeDataForRange["145-155"] += occurence
    elif 155<float(height)<165:
        modeDataForRange["155-165"] += occurence
    elif 165<float(height)<175:
        modeDataForRange["165-175"] += occurence

modeRange, modeOccurence = 0,0

for range,occurence in modeDataForRange.items():
    if occurence>modeOccurence:
        modeRange, modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0] + modeRange[1])/2)
print(mode)