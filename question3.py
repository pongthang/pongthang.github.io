import readData as rd
import matplotlib.pyplot as plt 
import numpy as np
import os
files=[]
for x in list(os.walk('/home/akash/Downloads'))[0][2]:
    if x.endswith('.csv'):
        files.append(x[:-4])
files.sort()
for x in files:
    playerdata=rd.readData(x)
    playerdata=rd.fixRuns(playerdata)
    playerdata=rd.fixFours(playerdata)
    fours=[playerdata[i][3] for i in range(len(playerdata))]
    print(f'The maximum number of Fours hit by {x} in an inning (among all innings he has batted) is {max(fours)}')
