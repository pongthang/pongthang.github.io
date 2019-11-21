#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 01:02:02 2019

@author: laishram
"""
print('Enter a player name:')
name = input()
def readTeams(playername):
    read=open(playername+'.csv','r')
    read.readline()
    teams=[]
    for row in read:
        row=row.strip().split(',')
        teams.append(row[9])
    read.close()
    teams=list(set(teams))
    teams.sort()
    return teams
try:
    teams=readTeams(name)
    for i in teams:
        print( i )
except:
    print('Error')

  
   
        
    
