# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 18:38:28 2017

@author: Hume Dickie
"""
#pe53.py

import scipy as sp

count = 0

for n in range(1,101):
    for k in range(n+1):
        if sp.special.binom(n,k) > 1000000:
            count += 1

print count