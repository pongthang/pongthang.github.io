#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 01:56:32 2019

@author: laishram
"""
print('Enter a player name:')
playername = input()
def readTeams(playername):
    read=open(playername+'.csv','r')
    read.readline()
    teams=[]
    for row in read:
        row=row.strip().split(',')
        teams.append(row[9])
    read.close()
    return teams
teams = readTeams(playername)
def runs_against_teams(playername):
    read=open(playername+'.csv','r')
    read.readline()
    runs=[]
    for row in read:
        row =row.strip().split(',')
        if row[0]=='DNB' or row[0]=='TDNB':
            runs.append(0)
        elif row[0].endswith('*'):
            runs.append(int(row[0][:-1]))
        else:
            runs.append(int(row[0]))
    return runs
runs=runs_against_teams(playername)

def get_runs_stat(teams,runs):
    team_run={}
    for i in range(len(teams)):
        run=0
        for j in range(len(teams)):
            if teams[i]==teams[j]:
                run+=runs[j]
        team_run[teams[i]]=run
        run=0
    return team_run
team_run=get_runs_stat(teams,runs)
teams=list(team_run.keys())
teams.sort()
for i in teams:
    print(i,':',team_run[i])

        
        
                
                
                
                
                
                
                
                
                
                
                
    
            
            
             