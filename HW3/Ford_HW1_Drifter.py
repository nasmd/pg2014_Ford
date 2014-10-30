# -*- coding: utf-8 -*-
# Trent Ford
# 2014-10-20
#Drifter Data Function

"""
Created on Tue Sep 23 07:48:12 2014

@author: Trent
"""

def  read_drifter(filename):
    """Open file and store information in dictionary
    This function opens a file with the input filename and extracts geographic 
    coordinates based on the input keyword for a dictionary. The output are the
    coordinates for the input key, as the dictionary 'tracks'"""    
    
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
    
if __name__ == '__main__':
    filename = 'drifter.dat'
    data = read_drifter(filename)