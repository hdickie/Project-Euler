# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:57:02 2017

@author: Hume Dickie
"""

import math 
#pe24.py
# this boils down to a*9! + b*8! + c*7! + d*6! + e*5! + f*4! + g*3! + h*2! + i
# where 0 <= a,b,c,d,e,f,g,i <=9

a = 2
b = 6
c = 6
d = 2
e = 5
F = 1
g = 2
h = 2
i = 0

def f(n):
    return math.factorial(n)
    
print a*f(9) + b*f(8) + c*f(7) + d*f(6) + e*f(5) + F*f(4) + g*f(3) + h*f(2) + i