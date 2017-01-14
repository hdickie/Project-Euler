# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:18:49 2017

@author: Hume Dickie
"""
import os
#pe67

#same as pe18 but w 100 rows instead of 15

#read in triangle
os.chdir('C:\Users\Hume Dickie\Desktop')
eyes = open("p067_triangle.txt",'r')

triangle = eyes.read()
triangleLists = triangle.split('\n')

triangleCoords = {}

for i in range(100):
    for j in range(i+1):
        triangleCoords[(i,j)] = int(triangleLists[i].split(" ")[j])
        
        
memoizedValues = {}
memoizedValues[0,0] = (triangleCoords[(0,0)],"")
        
def findMaxPath(i,j):
    print str(i) + " " + str(j) + " input to findMaxPath"
    
    if i == 0 and j == 0:
        print "woohoo!"
        return memoizedValues[0,0]
        
    if not (i,j) in memoizedValues:
        
        if j == 0: #left side
            if not (i-1,0) in memoizedValues:
                memoizedValues[i-1,0] = findMaxPath(i-1,0)
            newPath = memoizedValues[i-1,0][1] + "L"            
            memoizedValues[i,0] = (memoizedValues[i-1,0][0] + triangleCoords[i,0],newPath)
            return memoizedValues[i,0]
                
        
        if i == j: #right side
            if not (i-1,j-1) in memoizedValues:
                memoizedValues[(i-1,j-1)] = findMaxPath(i-1,j-1)
            newPath = memoizedValues[i-1,j-1][1] + "R"
            memoizedValues[i,j] = (triangleCoords[(i,j)] + memoizedValues[i-1,j-1][0], newPath)
            return memoizedValues[i,j]
            
            
        rightMaxPath = findMaxPath(i-1,j-1)
        leftMaxPath = findMaxPath(i-1,j)
        if leftMaxPath[0] > rightMaxPath[0]:
            newPath = leftMaxPath[1] + "L"   
            entry = (leftMaxPath[0]+triangleCoords[i,j], newPath)
        else: 
            newPath = rightMaxPath[1] + "R"
            entry = (rightMaxPath[0]+triangleCoords[i,j], newPath)
            
        memoizedValues[i,j] = entry
        return entry
        
    if (i,j) in memoizedValues:
        return memoizedValues[i,j]
        
        
potentialSolutions = []
for y in range(100):
    potentialSolutions.append(findMaxPath(99,y))
    
final = 0
for sol in potentialSolutions:
    if sol[0] > final: 
        final = sol[0]
        
print(final)
            
            #code works but my answer was wrong :/
