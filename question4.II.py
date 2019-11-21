#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:28:52 2019

@author: laishram
"""
import readData as rd
try:
    all_players=rd.listAll()
    print('Enter your choice')
    name=all_players[int(input())-1]
    playerdata=rd.readData(name)
    playerdata=rd.fixYear(playerdata)
except:
    print('Invalid Input')
total_run_in_a_year ={}
strike_rate=[]
years = []

for i in range(len(playerdata)):
    if playerdata[i][5]=='-':
        strike_rate.append(0)
    else:
        strike_rate.append( float(playerdata[i][5]))
    years.append(playerdata[i][11])

def total_strike_in_a_year(strike_rate,years):
    strike_rate_in ={}
    s=0.00
    for i in range(len(strike_rate)):
        if i==len(strike_rate)-1:
            s+=strike_rate[i]
            strike_rate_in[years[i]]=round(s,2)
            break
        if years[i]==years[i+1]:
            s+=strike_rate[i]
            continue
        elif years[i]!=years[i+1]:
            s+=strike_rate[i]
            strike_rate_in[years[i]]=round(s,2)
            s=0.00
    return strike_rate_in
strike_rate_in_a_year =total_strike_in_a_year(strike_rate,years)
years=list(strike_rate_in_a_year.keys())
strike_rate=list(strike_rate_in_a_year.values())

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(len(years))
plt.bar(x,strike_rate,align = 'center')
plt.xticks(x,years,rotation=90)
plt.ylabel('strike rate',fontsize =17)
plt.xlabel('years',fontsize=17)
plt.title(name)
plt.show() 







