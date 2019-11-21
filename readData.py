import os
def readData(player_name):
    playerdata=[]
    read=open(player_name+'.csv','r')
    read.readline()
    for row in read:
        row=row.strip().split(',')
        if row[0]=='DNB' or row[0]=='TDNB':
            continue;
        playerdata.append(row)
    read.close()
    return playerdata
def fixRuns(playerdata):
    for i in range(len(playerdata)):
        if playerdata[i][0].endswith('*'):
            playerdata[i][0]=int(playerdata[i][0][:-1])
        else:
            playerdata[i][0]=int(playerdata[i][0])
    return playerdata
def fixYear(playerdata):
    for i in range(len(playerdata)):
        date=playerdata[i][11]   #date in ddmmyyyy format
        date=date.split('-')     #turn it into a list
        year=date[2].strip()
        if int(year)>=0 and int(year)<20:
            year='20'+year
        else:
            year='19'+year
        playerdata[i][11]=int(year)   #now the 12th column contains only the year
    return playerdata
def fixFours(playerdata):
    for i in range(len(playerdata)):
        if playerdata[i][3]=='-':
            playerdata[i][3]=0
        else:
            playerdata[i][3]=int(playerdata[i][3])
    return playerdata
def listAll():
    all_players=[]
    for x in list(os.walk(os.getcwd()))[0][2]:
        if x.endswith('.csv'):
            all_players.append(x[:-4])
    all_players.sort()
    [print(f'{i+1}.) {x}') for i,x in enumerate(all_players)]
    return all_players