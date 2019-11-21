import readData as rd
import matplotlib.pyplot as plt 
import numpy as np
import os
def secmax(l):
    if len(l)==1:
        return l[0]
    l=set(l)
    l.remove(max(l))
    return max(l)
files=[]
for x in list(os.walk(os.getcwd()))[0][2]:
    if x.endswith('.csv'):
        files.append(x[:-4])
files.sort()
X=[]
Y1=[]
Y2=[]
for x in files:
    X.append(x)
    playerdata=rd.readData(x)
    playerdata=rd.fixRuns(playerdata)
    runs=[playerdata[i][0] for i in range(len(playerdata))]
    Y1.append(max(runs))
    Y2.append(secmax(runs.copy()))
xpos=np.arange(len(X))
plt.xticks(xpos,X,rotation=90,fontsize=7)
plt.xlabel('Players')
plt.ylabel('Score')
width=0.35
plt.bar(xpos-width/2,Y1,width,label='Highest score')
plt.bar(xpos+width/2,Y2,width,label='Second highest score')
plt.legend()
plt.show()
