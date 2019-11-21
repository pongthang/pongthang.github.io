import matplotlib.pyplot as plt
import numpy as np
import readData as rd
def secmax(l):
    if len(l)==1:
        return l[0]
    l=set(l)
    l.remove(max(l))
    return max(l)
playerdata=None
try:
    print('Enter name of a player')
    name=input()
    playerdata=rd.readData(name)
except:
    print('Invalid Input')
playerdata=rd.fixYear(playerdata)
playerdata=rd.fixRuns(playerdata)
temp_year=playerdata[0][11]
runs={}                      #dict to store runs in a year
runs[temp_year]=[]
for i in range(len(playerdata)):
    run=playerdata[i][0]     #runs scored in a match
    if temp_year==playerdata[i][11]:
        runs[temp_year].append(run)
    else:
        temp_year=playerdata[i][11]
        runs[temp_year]=[run]
X=list(runs.keys())
Y1=[max(runs[x]) for x in runs]
Y2=[secmax(runs[x].copy()) for x in runs]
x=np.arange(len(X))
width=0.35
plt.bar(x-width/2,Y1,width,label='Highest score')
plt.bar(x+width/2,Y2,width,label='Second highest score')
plt.xticks(x,X)
plt.legend()
plt.show()
