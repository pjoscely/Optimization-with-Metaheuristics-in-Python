#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:44:52 2019

@author: joscelynec
"""
### Adapted from Optimization with Metaheuristics in Python
### https://www.udemy.com/optimization-with-metaheuristics/

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


### The Traveling Saleswitch Problem

### Example: : Sabrina has the following list of errands:
### Pet store (the black cat needs a new litterbox) (P)
###   Greenhouse (replenish supply of deadly nightshade) (G)
###   Pick up black dress from cleaners (C)
###   Drugstore (eye of newt, wing of bat, toothpaste) (D)
###   Target (weekly special on cauldrons) (T)
###   In witch which order should she do these errands in order to minimize the time spent on her broom?

### Home (H) Pet store (P) Greenhouse (G) Cleaners (C) Drugstore (D) Target (T) 
print("Times between each pair of locations (minutes):")
print("Home (H) Pet store (P) Greenhouse (G) Cleaners (C) Drugstore (D) Target (T)") 
Dist = pd.DataFrame([[0, 36, 32, 54, 20, 40],
                     [36, 0, 22, 58, 54, 67],
                     [32, 22, 0, 36, 42, 71],
                     [54, 58, 36, 0, 50, 92],
                     [20, 54, 42, 50, 0, 45],
                     [40, 67, 71, 92, 45, 0]],
                    columns=["H","P","G","C","D","T"],
                    index=["H","P","G","C","D","T"])
print(Dist)
T0 = 1500
M = 250
N = 20
alpha = 0.9

#initial solution to the TSP
#Form an initial circuit guess
X0 = ["H", "D", "T", "G", "P", "C", "H"]

Temp = []
Min_Cost = []

for i in range(M):
    for j in range(N):
        ran_1 = np.random.randint(0,len(X0))
        ran_2 = np.random.randint(0,len(X0))
        
        while ran_1==ran_2:
            ran_2 = np.random.randint(0,len(X0))
        
        xt = []
        # initial circuit
        # ["H", "D", "T", "G", "P", "C", "H"]
                
        A1 = X0[ran_1]
        A2 = X0[ran_2]

        # Make a new random circuit
        
        w = 0
        for i in X0:
            if X0[w]==A1:
                xt = np.append(xt,A2)
            elif X0[w]==A2:
                xt = np.append(xt,A1)
            else:
                xt=np.append(xt,X0[w])
            w = w+1
        
        #compute initial circuit distance
        sum_init = 0
        for i in range(len(X0)-1):
            sum_init+= Dist[X0[i]][X0[i+1]]
        
        #compute new circuit distance
        sum_new  = 0
        for i in range(len(xt)-1):
            sum_new+= Dist[xt[i]][xt[i+1]]
        
        
        rand1 = np.random.rand()
        form = 1/(np.exp(sum_new-sum_init)/T0)
        
        if sum_new<=sum_init:
            X0=xt
        elif rand1<=form:
            X0=xt
        else:
            X0=X0
    
    Temp.append(T0)
    Min_Cost.append(sum_init)
    
    T0 = alpha*T0
    
print("Result of run:")
print("Final Solution:",X0)
print("Minimized Cost:",sum_init)
        

plt.plot(Temp,Min_Cost)
plt.title("Cost vs. Temp.", fontsize=20,fontweight='bold')
plt.xlabel("Temp.", fontsize=18,fontweight='bold')
plt.ylabel("Cost", fontsize=18,fontweight='bold')
plt.xlim(1500,0)

plt.xticks(np.arange(min(Temp),max(Temp),100),fontweight='bold')
plt.yticks(fontweight='bold')
plt.show()
"""
Times between each pair of locations (minutes):
Home (H) Pet store (P) Greenhouse (G) Cleaners (C) Drugstore (D) Target (T)
    H   P   G   C   D   T
H   0  36  32  54  20  40
P  36   0  22  58  54  67
G  32  22   0  36  42  71
C  54  58  36   0  50  92
D  20  54  42  50   0  45
T  40  67  71  92  45   0
Result of run:
Final Solution: ['G' 'P' 'H' 'T' 'D' 'C' 'G']
Minimized Cost: 229
"""


