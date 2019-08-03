#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:17:51 2019

@author: joscelynec
"""

### Adapted from Optimization with Metaheuristics in Python
### https://www.udemy.com/optimization-with-metaheuristics/
### http://optlab-server.sce.carleton.ca/POAnimations2007/SimAnnealing.aspx

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#The best possible solution for this problem is a tour length ??????

Dist = pd.DataFrame([[0.0,1.0,2.0,4.0,9.0,8.0,3.0,2.0,1.0,5.0,7.0,1.0,2.0,9.0,3.0],
                     [1.0,0.0,5.0,3.0,7.0,2.0,5.0,1.0,3.0,4.0,6.0,6.0,6.0,1.0,9.0],
                     [2.0,5.0,0.0,6.0,1.0,4.0,7.0,7.0,1.0,6.0,5.0,9.0,1.0,3.0,4.0],
                     [4.0,3.0,6.0,0.0,5.0,2.0,1.0,6.0,5.0,4.0,2.0,1.0,2.0,1.0,3.0],
                     [9.0,7.0,1.0,5.0,0.0,9.0,1.0,1.0,2.0,1.0,3.0,6.0,8.0,2.0,5.0],
                     [8.0,2.0,4.0,2.0,9.0,0.0,3.0,5.0,4.0,7.0,8.0,3.0,1.0,2.0,5.0],
                     [3.0,5.0,7.0,1.0,1.0,3.0,0.0,2.0,6.0,1.0,7.0,9.0,5.0,1.0,4.0],
                     [2.0,1.0,7.0,6.0,1.0,5.0,2.0,0.0,9.0,4.0,2.0,1.0,1.0,7.0,8.0],
                     [1.0,3.0,1.0,5.0,2.0,4.0,6.0,9.0,0.0,3.0,3.0,5.0,1.0,6.0,4.0],
                     [5.0,4.0,6.0,4.0,1.0,7.0,1.0,4.0,3.0,0.0,9.0,1.0,8.0,5.0,2.0],
                     [7.0,6.0,5.0,2.0,3.0,8.0,7.0,2.0,3.0,9.0,0.0,2.0,1.0,8.0,1.0],
                     [1.0,6.0,9.0,1.0,6.0,3.0,9.0,1.0,5.0,1.0,2.0,0.0,5.0,4.0,3.0],
                     [2.0,6.0,1.0,2.0,8.0,1.0,5.0,1.0,1.0,8.0,1.0,5.0,0.0,9.0,6.0],
                     [9.0,1.0,3.0,1.0,2.0,2.0,1.0,7.0,6.0,5.0,8.0,4.0,9.0,0.0,7.0],
                     [3.0,9.0,4.0,3.0,5.0,5.0,4.0,8.0,4.0,2.0,1.0,3.0,6.0,7.0,0.0]],
                    columns=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"],
                    index=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])

print(Dist)
T0 = 1000
M = 500
N = 25
alpha = 0.9

#initial solution to the TSP
#Form an initial circuit guess
X0 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]

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
        # ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
                
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
