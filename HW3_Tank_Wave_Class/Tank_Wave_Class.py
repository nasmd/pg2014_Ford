# -*- coding: utf-8 -*-
#Trent Ford
#2014-11-11
#Homework 3: Create wave moving in a tank (1D channel)
"""
Created on Tue Oct 28 16:13:06 2014

@author: geoglocal
"""
import numpy as np
import matplotlib.pyplot as plt


class wave(object):
    
    def __init__(self, n, dx=100., dt=5., H=10., g=9.8):
        u = np.zeros(n)
        eta = np.arange(n-1)
        
        for p in range(0, n-1):
            u[1:-1] = u[1:-1]-(dt*g/dx)*(eta[1:]-eta[:-1])
            eta = eta-(dt*H/dx)*(u[1:]-u[:-1])
            
        print eta
        x=np.arange(0,n-1)
        plt.plot(x,eta)
        plt.show()
        
if __name__ == '__main__':
    out = wave(n=50.,)

