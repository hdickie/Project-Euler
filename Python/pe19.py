# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:22:46 2017

@author: Hume Dickie
"""

#pe19.py

n = {
    0: 31,
    1: 28,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9:31,
    10:30,
    11:31
    
}

sunday = 0
dayOfTheWeek = 2 #starts on a tuesday
for t in range(1901,2001):
    for m in range(12):
        numdays = n[m]
        if(m == 1 and t%4 == 0 and (t%100 != 0 or t%400 == 0)): #leap years in feb
            numdays+=1
        for d in range(numdays):
            dayOfTheWeek = (dayOfTheWeek + 1)%7
            if (d == 0 and dayOfTheWeek == 0):
                sunday+=1
            
print sunday