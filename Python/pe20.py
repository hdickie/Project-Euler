# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:23:43 2017

@author: Hume Dickie
"""

#pe20.py

import math

digit = str(math.factorial(100))

run = 0
for d in digit:
    run +=int(d)
    
print(run)