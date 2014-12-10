# -*- coding: utf-8 -*-
#Trent Ford
#2014-12-08
#Homework 3/4: Modification to wave moving in tank, saving output from class 
#in a NetCDF file format. 
"""
Created on Wed Dec 10 07:20:48 2014

@author: Trent
"""


import numpy as np
import matplotlib.pyplot as plt
import netCDF4

#wave class is initialized to model wave moving in a tank of n a certain length
#The time variable (n) determines the number of iterations or time steps over 
#which the model is computed
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
        self.eta = eta
        self.x = x
        
    #writeNetCDF method is used to write the output of the wave model to a 
        #netCDF file with dimensions x and time
    def writeNetCDF(self, fileName,n):
        nc = netCDF4.Dataset(fileName, 'w')
        nc.author = 'Ford'
        
        nc.createDimension('x',n)
        nc.createDimension('time',None)
        
        nc.createVariable('wave', 'd', ('time','x'))
        nc.variables['wave'] = self.eta
        
        nc.createVariable('x','i',('x',))
        nc.variables['x'] = self.x
        
        nc.createVariable('time','d', ('time',))
        nc.variables['time'] = np.arange(1,50)
        
        nc.close()
        
        
    

        
if __name__ == '__main__':
    out = wave(n=50,)
    out.writeNetCDF('Practice1.nc', n=50)
    
