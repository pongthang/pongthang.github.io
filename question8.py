#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:23:35 2019

@author: laishram
"""

import readData as rd
try:
    print('Enter name of a player')
    name=input()
    playerdata=rd.readData(name)
    playerdata = rd.fixRuns(playerdata)
    playerdata=rd.fixYear(playerdata)
except:
    print('Invalid Input')
#run is in 1st column, year is in 12th column
total_run_in_a_year ={}
runs=[]
years = []
for i in range(len(playerdata)):
    runs.append( playerdata[i][0])
    years.append(playerdata[i][11])

def total_run_in_a_year(runs,years):
    run_in_a_year ={}
    s=0
    for i in range(len(runs)):
        if i==len(runs)-1:
            s+=runs[i]
            run_in_a_year[years[i]]=s
            break
        if years[i]==years[i+1]:
            s+=runs[i]
            continue
        elif years[i]!=years[i+1]:
            s+=runs[i]
            run_in_a_year[years[i]]=s
            s=0
    return run_in_a_year

run_in_a_year=total_run_in_a_year(runs,years)
years=list(run_in_a_year.keys())
runs =list(run_in_a_year.values())

def cumulative_run(runs):
    s=0
    runc=[]
    for i in range(len(runs)):
        s+=runs[i]
        runc.append(s)
    return runc
cum_run =cumulative_run(runs)
#print(cum_run)
import matplotlib.pyplot as plt
plt.title(name+' cumlative runs line graph')
plt.plot(years,cum_run,linewidth=5)
plt.xticks(years,fontsize=15,rotation=90)
plt.show()
            
            
            
            
            
            
            
            
            
            
        
            
    
