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
playerdata=rd.fixFours(playerdata)
temp_year=playerdata[0][11]
fours={}                      #dict to store fours in a year
fours[temp_year]=0
for i in range(len(playerdata)):
    four=playerdata[i][3]     #fours scored in a match
    if temp_year==playerdata[i][11]:
        fours[temp_year]+=four
    else:
        temp_year=playerdata[i][11]
        fours[temp_year]=four
X=list(fours.keys())
Y=[fours[x] for x in fours]
x=np.arange(len(X))
plt.bar(x,Y,0.5,align='center')
plt.xlabel('Years')
plt.ylabel('Fours')
plt.xticks(x,X)
plt.show()
