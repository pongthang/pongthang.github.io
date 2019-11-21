import matplotlib.pyplot as plt
import numpy as np
import readData as rd
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
fifty={}                      #dict to store 50's scored in a year
fifty[temp_year]=0
for i in range(len(playerdata)):
    if temp_year==playerdata[i][11]:
        if playerdata[i][0]>=50 and playerdata[i][0]<100:
            fifty[temp_year]+=1
    else:
        temp_year=playerdata[i][11]
        if playerdata[i][0]>=50 and playerdata[i][0]<100:
            fifty[temp_year]=1
        else:
            fifty[temp_year]=0
X=list(fifty.keys())
Y=[fifty[x] for x in fifty]
x=np.arange(len(X))
width=0.5
plt.xlabel('Years')
plt.ylabel('Fifties')
plt.bar(x,Y,width,align='center')
plt.xticks(x,X)
plt.legend()
plt.show()
