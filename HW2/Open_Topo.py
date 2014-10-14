# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:21:24 2014

@author: Trent
"""

import numpy as np
import matplotlib as mp
from mpl_toolkits.basemap import Basemap

def get_Etopo(filename):
     f = open(filename)
     
     topo = []
     for line in f.readlines():        
        obs = line.split('\t')
        topo.append(obs)
     
     topo = np.array(topo)     
     lats = np.unique(topo[:,1])
     
     count = 1
     world = []
     for lat in lats:
         world[count,:] = topo[topo[:,1] == lat].T

     m = Basemap(projection = 'lcc',llcrnrlon=-180,urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90,lat_0=0,lon_0=0,resolution='l')
     m.fillcontinents()
     pcm = m.pcolormesh(lats,lons,world,cmap=plt.cm.RdBu_r,vmin=-1000,vmax=10-0)
     #Draw meridians with labels at bottom and left
     m.drawmeridians(np.arange(-120,40,10), dashes=[1,0], labels=[1,0,0,1])
     m.drawparallels(np.arange(-10,80,10), dashes=[1,0],labels=[0,1,0,0])
     #put in colorbar
     #add axis for colorbar
     cax = fig.add_axes([0.18,0.58,0.2,0.02])
     cb = m.colorbar(pcm,orientation='horizontal')
     
     return lats,topo