import readData as rd
import matplotlib.pyplot as plt 
import math
import os
files=[]
for x in list(os.walk('/home/akash/Downloads'))[0][2]:
    if x.endswith('.csv'):
        files.append(x[:-4])
files.sort()
for x in files:
    playerdata=rd.readData(x)
    playerdata=rd.fixRuns(playerdata)
    fifties=0
    for i in range(len(playerdata)):
        if playerdata[i][0]>=50 and playerdata[i][0]<100:
            fifties+=1
    print(f'{x} scores a fifty on an average after {math.ceil(len(playerdata)/fifties)} matches.')

