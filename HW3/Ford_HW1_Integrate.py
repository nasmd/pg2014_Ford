# -*- coding: utf-8 -*-
# Trent Ford
# 2014-10-20
#Integration Function

"""
Created on Tue Sep 23 07:45:01 2014

@author: Trent
"""

import numpy as np

def integrate(f,dx=1.0):
    """Integrate over a list of numbers
    This function calculates the integral, usin gthe trapezoidal rule, over a 
    list of numbers. The default value of dx = 1.0, but is also an input to the 
    function"""
    
    x = np.array(f)
    area = 0.0
    
    for i in range(len(x)-1):
        area = area+((x[i]+x[i+1])/2)*dx
        
    return area
    print area
    
if __name__ == '__main__':
    f = [1,2,3,4,5]
    integral = integrate(f)