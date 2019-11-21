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
    playerdata=rd.fixFours(playerdata)
    fours=0
    for i in range(len(playerdata)):
        fours+=playerdata[i][3]
    print(f'The number of Fours hit by {x}  in his overall career are {fours}')

