# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 17:37:24 2017

@author: Hume Dickie
"""

#Project Euler problem 1
#Find the sum of all the multiples of 3 or 5 below 1000.
runningSum = 0
for i in range(1,1000):
    if (i%3 == 0 or i%5 == 0):
        runningSum += i
    
print runningSum