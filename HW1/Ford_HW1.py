# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 07:19:24 2014

@author: Trent
"""
#*****************************************************************
#def fib(N):
#    """Return N Fibonacci numbers
#    This function takes in the N number of values and outputs N Fibonacci
#    numbers"""
#    
#    a,b = 0,1
#    fibArray = []
#    
#    fibArray.append(b)
#    for i in range(N-1):
#        c = a+b
#        a = b
#        b = c
#        fibArray.append(c)        
#    return fibArray
#    
#    
#print fibArray
#********************************************************************


#import numpy as np
#
#def integrate(f,dx=1.0):
#    """Integrate over a list of numbers
#    This function calculates the integral, usin gthe trapezoidal rule, over a 
#    list of numbers. The default value of dx = 1.0, but is also an input to the 
#    function"""
#    
#    x = np.array(f)
#    area = 0.0
#    
#    for i in range(len(x)-1):
#        area = area+((x[i]+x[i+1])/2)*dx
#        
#    return area
#    print area
               
#**********************************************************
#import datetime as dt
#
#def extract(filename):
#    
#    f = open(filename)
#        
#    discharge = []
#    dates = []
#    
#    for line in f.readlines():
#        
#        data = line.split('\t')
#        # $GPGGA,124628,4907.718,N,12312.802,W,2,06,1.30,5,M,,,,*29
#        if (data[0] == 'USGS'):
#            
#            year = int(data[2][:4])
#            month = int(data[2][5:7])
#            day = int(data[2][8:10])
#            Date = dt.date(year,month,day)
#            
#            flowString = data[3]
#            flowString = flowString.rstrip('\n')
#            flowString = flowString.rstrip('_P')
#            flowString = flowString.rstrip('_A')
#            flowString = flowString.rstrip('_e')
#            
#            flow = int(flowString)
#            
#            dates.append(Date) 
#            discharge.append(flow)
#    return dates
#    return discharge                
#******************************************************************            
            
def  read_drifter(filename):
    import sys
    f = open(filename)
    
      
    names = []
    
    for line in f.readlines():
        data = line.split('\t')
        
        if (data[0] == 'Waypoint'):
            names.append(data[1])
    f.close()
    #---------------------------------
    tracks = {}   
    test = []
    for name in names:
        sys.stdout.write(name)
        latLongList = ()
        f = open(filename)
        lines = f.readlines()
        for i in range(0,len(lines)):
            data = lines[i].split('\t')
            if len(data) > 2 and data[0] == 'Track' and data[1] == name:
                data = lines[i+4].split('\t')
                test.append(data)
                count = 5
                            
                while (data[0] == 'Trackpoint' and i+count < len(lines)):
                    lats = float(data[1][4:10])
                    longs = float(data[1][15:21])
                    latLongList = latLongList + (lats,longs)
                    data = lines[i+count].split('\t')
                    count += 1
                    
                    
                    
        tracks[name] = latLongList                    
        f.close()
        
                    
                 
            
  
    
    f.close()        
    return tracks,test
    print tracks
    
    
    