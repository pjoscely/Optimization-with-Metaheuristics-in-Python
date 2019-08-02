#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:04:07 2019

@author: joscelynec
"""
######################################################
### SIMULATED ANNEALING - METAHEURISTIC
###MIN y = x^4-3x^3+2x
#### y has two unequal mininums
#### Annealing will eventualling find the global min.
######################################################
### Adapted from Optimization with Metaheuristics in Python
### https://www.udemy.com/optimization-with-metaheuristics/
######################################################


import numpy as np
import matplotlib.pyplot as plt

#f(x) = x**4-3*x**3+2*x
def f(x):
    return x**4-3*x**3+2*x


np.seterr(divide="ignore") # ignore the warning of zero division
# or.. np.seterr(divide="ignore", invalid="ignore")

# initial solution you'd like to start at
x = -5 # initial x

# objective function value for x 
z = f(x)

#Display initial values
print()
print()
print("initial x is: %0.3f" % x)
print("initial z is: %0.3f" % z)


# hyperparameters (user inputted parameters)
T0 = 1000 # the temperature (temp.)
temp_for_plot = T0 # for plotting purposes
M = 10000 # how many times you will decrease the temp.
N = 300 # how many times you want to search your neighborhood
alpha = 0.85 # by how much do you want to decrease the temp.
                # when you increase m by 1 (m small)
k = 0.1 # helps reduce the step-size, for example, if your random number
            # was 0.90 and your x value was 1, to make your step size in
            # the search space smaller, instead of making your new x value
            # 1.90 (1 + 0.90), you can multiply the random number (0.90)
            # with a small number to ensure you will take a smaller step...
            # so, if k = 0.10, then 0.90 * 0.10 = 0.09, which will make
            # your new x value 1.09 (1 + 0.09).. this helps you search the
            # search space more efficiently by being more thorough instead
            # of jumping around and taking a large step that may lead you
            # to pass the opital or near-optimal solution


temp = [] # to plot the temprature
obj_val = [] # to plot the obj val reached at the end of each m (small M)
        
for i in range(M): # how many times to decrease the temp.
    
    for j in range(N): # for each m, how many neighborhood searches
        
        
        # for the decision variable x -->
        
        rand_num_x_1 = np.random.rand() # increase or decrease x value?
        rand_num_x_2 = np.random.rand() # by how much?
        
        if rand_num_x_1 >= 0.5: # greater than 0.5, we increase
            step_size_x = k * rand_num_x_2 # make sure we make a smaller
                                            # step-size
        else:
            step_size_x = -k * rand_num_x_2 # less than 0.5, we decrease
        
        
        
        # temporary because we still need to know if we should take this
            # new solution or stay where we are and look again
        x_temporary = x + step_size_x # add or subtract the x value
        
        
        # the possible new move with the temporary values
        # need to see if better or worse than where we currently are
        obj_val_possible = f(x_temporary)
        
        # where we are currently
        obj_val_current = f(x)
        
        
        # in case our possible new solution is worse, we need to figure
        # out if we should take it or not
        rand_num = np.random.rand()
        
        # if the possible solution is worse, with the help of the random
            # number above, we will let a formula decide if we take it or
            # stay where we are
        # the closer we get to the end of our search (the lower the
            # temp. value), it will be less likely to take worse solutions
            # because the random number will most likely be greater
        formula = 1/(np.exp((obj_val_possible - obj_val_current)/T0))
        
        
        # do we change our current solution?
        # is the new potential solution better or worse?
        
        if obj_val_possible <= obj_val_current: # if it's better, then
                                                    # we take it and make
                                                    # it our new solution
            x = x_temporary
        
        elif rand_num <= formula: # if it's worse, then we need to figure
                                        # out if we should take it or not
                                # if the random number is less than the
                                # output of the formula, then we take the
                                # new solution
            x = x_temporary
        
        else: # if the random number was greater than the formula, it means
                # we did not accept the worse solution and stay at our
                # current solution
            x = x
    
    temp.append(T0) # append the temp. to [temp] for plotting reasons
    obj_val.append(obj_val_current) # append the temp. to [temp] for
                                            # plotting reasons
        
    T0 = alpha*T0 # since we are done with a certain m (M small), before
                    # going to the next m, we need to decrease the temp.


print()
print("x is: %0.3f" % x)
print("obj val is: %0.3f" % obj_val_current)
print()
print("------------------------------")


plt.plot(temp,obj_val)
plt.title("Z at Temperature Values",fontsize=20, fontweight='bold')
plt.xlabel("Temperature",fontsize=18, fontweight='bold')
plt.ylabel("Z",fontsize=18, fontweight='bold')

plt.xlim(temp_for_plot,0)
plt.xticks(np.arange(min(temp),max(temp),100),fontweight='bold')

plt.show()

"""
******* Output for a poor choice of a starting value is still optimal
initial x is: -5.000
initial z is: 990.000

x is: 2.141
obj val is: -4.148

"""



