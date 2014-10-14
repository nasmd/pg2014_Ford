# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 12:22:13 2014

@author: Trent
"""

"""This class creates an OpenData object that relates to discharge data from 
the USGS."""

import datetime
import numpy as np
import matplotlib as mp
from urllib2 import urlopen

class OpenData(object):
    
    def __init__(self, webpage):
        self.webpage = webpage        
        data = urlopen(webpage)
        
        times = []
        discharge = []
        
        for line in data:
            obs = line.split('\t')
            
            if obs[0] == 'USGS':
                
                year = int(obs[2][0:4])
                month = int(obs[2][5:7])
                day = int(obs[2][8:10])
                
                if obs[3] == '':
                    dis = 0
                else:
                    dis = int(obs[3])
                    dis *= 0.0283
                
                discharge.append(dis)             
                times.append(datetime.date(year,month,day))
                
        self.time = np.array(times)
        self.discharge = np.array(discharge)
        
    """The get_Year method extracts the specified year's worth of data"""            
    def get_Year(self,year):
        
        dates = []
        dis = []
        count = 0
        for d in self.time:
            if self.time[count].year == year:
                dates.append(datetime.date(self.time[count].year, self.time[count].month,self.time[count].day))
                dis.append(self.discharge[count])
                
            count += 1
        
        dis = np.array(dis)
        dates = np.array(dates)     
        
        return dis, dates
    
    """The plot_Hydrograph method is self-explanatory, plotting the hydrograph
    over the entire time series"""            
    def plot_Hydrograph(self):
        plt.plot(self.time,self.discharge)
        plt.xticks(fontsize = 18)
        plt.yticks(fontsize = 18)
        plt.ylabel('Discharge ($m^3 s^{-1})$', fontsize = 24)
        plt.xlabel('Date', fontsize = 24)
        
    """The get_MeanAnnual method calculates the mean annual discharge from the 
    data and plots it in a hydrograph"""    
    def get_MeanAnnual(self):
        
        years = np.arange(1967,2015,1)
        yearStrings = np.array(map(str,years)) 
        average = []
        deviation = []
        dates = []
        
        for days in np.arange(0,366,1):
            dis = []
            for years in yearStrings:
                dt = np.datetime64(years) + np.timedelta64(days,'D')
                try: 
                    ind = np.nonzero(self.time==dt)[0][0]
                except IndexError: 
                    ind = 0
                if ind != 0:
                    dis.append(self.discharge[ind])
                    
            average.append(np.mean(dis)) 
            deviation.append(np.std(dis))
            
        count = 0            
        for d in self.time:
            if self.time[count].year == 2012:
                dates.append(datetime.date(self.time[count].year, self.time[count].month,self.time[count].day))
            count += 1
                                
        plt.plot(dates,average) 
        self.average = average
        self.deviation = deviation
        
        return average, deviation
        
    """The make_DeviationPlot method plots the hydrograph of the specified year
    with the mean annual hydrograph as well as standard deviation areas."""
    def make_DeviationPlot(self,year):
        average = np.array(self.average)
        deviation = np.array(self.deviation)
        
        dates = []
        dis = []
        count = 0
        for d in self.time:
            if self.time[count].year == year:
                dates.append(datetime.date(self.time[count].year, self.time[count].month,self.time[count].day))
                dis.append(self.discharge[count])
                
            count += 1
        
        dis = np.array(dis)
        dates = np.array(dates)  
        
        if len(dates) == 365:
            average = np.delete(average,-1)
            deviation = np.delete(deviation,-1)
            
        plus1 = np.array(average+deviation)
        minus1 = np.array(average-deviation)
        
                
        plt.plot(dates,dis,'r')
        x = np.linspace(1,366,366)
        plt.plot(dates,average,'k')
        plt.fill_between(dates,average,plus1,facecolor='gray')
        plt.fill_between(dates,average,minus1,facecolor='gray')