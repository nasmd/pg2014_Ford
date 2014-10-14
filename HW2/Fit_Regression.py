# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:20:56 2014

@author: Trent
"""

import numpy as np

def linearFit(x,y,N):
    """Fit N-order polynomial to a set of points
    This function calculates the N-order polynomial regression of a set of 
    points and then returns the residuals"""
    
    sol = np.polyfit(x,y,N)
    ypoly = np.polyval(sol,x)
    
    resid = ypoly - y
    
    return resid