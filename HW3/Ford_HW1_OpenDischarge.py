# -*- coding: utf-8 -*-

# Trent Ford
# 2014-10-20
#Discharge Data Function

"""
Created on Tue Sep 23 07:46:04 2014

@author: Trent
"""

import datetime as dt

def extract(filename):
    """Open file and extract discharge data
    This function opens a file with the input filename and extracts the dates
    and corresponding discharge information, which are stored in "dates" and 
    "discharge", respectively"""
    
    f = open(filename)
        
    discharge = []
    dates = []
    
    for line in f.readlines():
        
        data = line.split('\t')
        # $GPGGA,124628,4907.718,N,12312.802,W,2,06,1.30,5,M,,,,*29
        if (data[0] == 'USGS'):
            
            year = int(data[2][:4])
            month = int(data[2][5:7])
            day = int(data[2][8:10])
            Date = dt.date(year,month,day)
            
            flowString = data[3]
            flowString = flowString.rstrip('\n')
            flowString = flowString.rstrip('_P')
            flowString = flowString.rstrip('_A')
            flowString = flowString.rstrip('_e')
            
            flow = int(flowString)
            
            dates.append(Date) 
            discharge.append(flow)
    return dates
    return discharge   
    
if __name__ == '__main__':
    filename = 'discharge.dat'
    data = extract(filename)