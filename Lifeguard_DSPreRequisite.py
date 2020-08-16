#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import sys

def load_data(filename):
    global interval
    interval = np.loadtxt(filename, skiprows=1)
    interval = [[int(num) for num in item] for item in interval]
    
def find_maximum_time_covered(interval, N, Q): 
  
    Mark = [0 for i in range(Q)] 
    for i in range(N): 
        l = interval[i][0] 
        r = interval[i][1] - 1
        for j in range(l, r + 1): 
            Mark[j] += 1
      
    # Total Count of covered units of time 
    count = 0
    for i in range(Q): 
        if (Mark[i]): 
            count += 1
  
    # Array to store units of time that occur 
    # exactly in one interval till ith interval 
    new_count = [0 for i in range(Q)] 
    if (Mark[0] == 1): 
        new_count[0] = 1
    for i in range(1, Q): 
        if (Mark[i] == 1): 
            new_count[i] = new_count[i - 1] + 1
        else: 
            new_count[i] = new_count[i - 1] 
      
    maxindex = 0
    maxcoverage = 0
    for i in range(N): 
        l = interval[i][0] 
        r = interval[i][1] - 1
  
        # Calculate New count by removing all units of time 
        # in range [l, r] occurring exactly once 
        elem1 = 0
        if (l != 0): 
            elem1 = new_count[r] - new_count[l - 1] 
        else: 
            elem1 = new_count[r] 
        if (count - elem1 >= maxcoverage): 
            maxcoverage = count - elem1 
            maxindex = i 
    return maxcoverage
  
filename = input("Enter filename - ")
load_data(filename)
Q = np.amax(interval)
N = len(interval)
maxcoverage = find_maximum_time_covered(interval, N, Q)


output_file = open(filename.replace("in", "out"),'w')
sys.stdout = output_file
print(maxcoverage)