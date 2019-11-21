#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:35:14 2019

@author: laishram
"""
import readData as rd
try:
    print('Enter name of a player')
    name=input()
    playerdata=rd.readData(name)
    playerdata = rd.fixRuns(playerdata)
except:
    print('Invalid Input')
def find_no_match():
    count =0
    s=0
    run=1000
    no_of_match=[]
    run_to_be_reached =[]
    for i in range(len(playerdata)):
        s+=playerdata[i][0]
        count+=1
        if i==len(playerdata)-1:
            if s>=run:
                no_of_match.append(count)
                run_to_be_reached.append(run)
                break
            elif s<run:
                break
        elif s>=run:
            no_of_match.append(count)
            run_to_be_reached.append(run)
            run+=1000
    return no_of_match,run_to_be_reached
no_of_match,run_to_reached = find_no_match()
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(len(run_to_reached))
plt.bar(x,no_of_match,align = 'center')
plt.xticks(x,run_to_reached)
plt.ylabel('no. of match to be played',fontsize =17)
plt.xlabel('run to be reached',fontsize=17)
plt.show()    
            
            
            
            
            
            
            
            
            
            
            