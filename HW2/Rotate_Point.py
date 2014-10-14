# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:23:03 2014

@author: Trent
"""

from math import *
import numpy as np

class Point(object):
    """docstring for Point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)
        
        return sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Point(%f, %f)' % (self.x, self.y)
        
    def rot(self,p,radians,origin=Point(0,0)):
        
        orig = np.array([origin.x,origin.y])
        point = np.array([p.x, p.y])
        
        x = point[0]-orig[0]
        yorz = point[1]-orig[1]
        newx = (x*cos(radians)) - (yorz*sin(radians))
        newyorz = (x*sin(radians)) - (yorz*cos(radians))
        newx += orig[0]
        newyorz += orig[1]
        
        return newx,newyorz       
        
    
if __name__ == '__main__':
    p1 = Point(3.0, 4.0)
    p2 = Point(5.0, 8.0)
    
    p3 = p1 + p2
    
    print p3.x, p3.y
    print p1.distance()
    print p1.distance(p2)
    
    print p1