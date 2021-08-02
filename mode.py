from collections import Counter
import csv
with open("SOCR-HeightWeight.csv", newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))

n=len(newData)

data=Counter(newData)
modeDataforrange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height, occurrence in data.items():
    if 50 < float(height)<60:
        modeDataforrange["50-60"]+=occurrence

    elif 60 < float(height)<70:
        modeDataforrange["60-70"]+=occurrence

    elif 70 < float(height)<80:
        modeDataforrange["70-80"]+=occurrence
    
modeRange, modeOccurrence = 0,0
for range,occurrence in modeDataforrange.items():
    if occurrence>modeOccurrence:
        modeRange,modeOccurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence

mode=float((modeRange[0]+modeRange[1])/2)
print(mode)