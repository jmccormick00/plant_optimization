# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:12:37 2013

@author: jmccormick
"""
import csv
from .sizedistribution import sizedistribution
from .fractWashData import fractWashData

class feedsample:
    ''' Represents a feed sample to a plant.  Contains the size distribution
        and the washability fractions.
    '''
    def __init__(self, name):
        self.name = name
        
    def load(self, filename, delim=','):
        '''
            Load in a feed sample from a CSV file
            Expected format is:
            ATTRIBUTES,a,...    <= List the attributes where a is
            SIZE,
            [sizedata]
            SG,top,bottom,
            [sgdata]
        '''
        f = open(str(filename))
        data = list(csv.reader(f, delimiter=delim))
        f.close()
        
        self.sizeDist = sizedistribution()
        self.washList = []
        self.attr = []
        num = len(data)
        x = 0
        while x < num:
            if data[x][0].upper() == 'ATTRIBUTES':
                for a in data[x][1:]:
                    if a != '' and a != '\n':
                        self.attr.append(a.upper())
                x = x + 1
            elif data[x][0].upper() == 'SIZE':
                # Load in a size distribution
                size = []
                cumWt = []
                x = x + 1
                size.append(float(data[x][0]))
                cumWt.append(0.0)
                while x < num and (not data[x][0].isalpha()):
                    size.append(float(data[x][1]))
                    cumWt.append(float(data[x][2]))
                    x = x + 1
                self.sizeDist.loadData(size, cumWt)
                
            elif data[x][0].upper() == 'SG':
                # Load in a gravity fraction
                avgSG = []
                wt = []
                top = float(data[x][1])
                bottom = float(data[x][2])
                x = x + 1
                if self.attr is not None:
                    attrData = dict.fromkeys(self.attr, [])
                else:
                    attrData = None
                while x < num and (not data[x][0].isalpha()):
                    avgSG.append((float(data[x][0]) + float(data[x][1])) / 2.0)
                    wt.append(float(data[x][2]))
                    if attrData is not None:
                        i = 3
                        for a in self.attr:
                            attrData[a].append(float(data[x][i]))
                            i = i + 1
                    x = x + 1
                self.washList.append(fractWashData(avgSG, wt, top, bottom, self.attr, attrData))
            else:
                x = x + 1

    def getSample(self, topSize, botSize):
        res = None
        for f in self.washList:
            if (f.top <= topSize) and (f.bottom >= botSize):
                res = {}
                res['data'] = f
                res['sizeWT'] = self.sizeDist.getRangeCumalativeWt(topSize, botSize)
        return res
    
    def printSample(self):
        print "-----------------SIZE-----------------"
        print "Size, CumWt"
        for x in xrange(0, len(self.sizeDist.size)):
            print self.sizeDist.size[x], ',', self.sizeDist.cumalativeWt[x] 
        print "------------GRAVITY FRACTIONS------------"
        for f in self.washList:
            print 'Top[mm]:', f.top
            print 'Bottom[mm]:', f.bottom
            for atr in f.attr:
                print atr,
            print
            for x in xrange(0, len(f.data['SG'])):
                for atr in f.attr:
                    print f.data[atr][x],
                print
            print "-----------------------------------------"
                
            
                
            
        