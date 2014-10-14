# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:20:13 2014

@author: Trent
"""

import numpy as np

def distances(n,m):
    """Calculate distances between x,y points
    This function takes two sets of x,y points and calculates the euclidean
    distance between the arrays of points. If the input are nX2 and mX2 arrays, 
    then the output is an nXm array of distances"""
    
    d0 = np.subtract.outer(n[:,0],m[:,0])
    d1 = np.subtract.outer(n[:,1],m[:,1])
    
    return np.hypot(d0,d1)