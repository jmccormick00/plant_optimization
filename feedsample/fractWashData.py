# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:11:41 2013

@author: James McCormick
"""
import numpy as np

class fractWashData:
    ''' A class that represents one set of washdata per size fracion '''
    
    def __init__(self, avgSG, wt, top, bottom, attr = None, attrData = None):
        ''' 
        Creates a set of wash data
        input:  numRows => Number of rows to allocate
                attr => a list of column names to add to the data
        '''
        self.attr = []
        if attr is not None:
            for atr in attr:
                self.attr.append(atr.upper())
        self.top = top
        self.bottom = bottom
        self.data = {'SG': np.array(avgSG, dtype=np.float32), 'WT': np.array(wt, dtype=np.float32)}
        if attr is not None: # Add attributes
            for atr in attr:            
                self.data[(atr.upper())] = np.array(attrData[atr], dtype=np.float32)

    def setData(self, colName, arr):
#        i = self.columnNames.index(colName)
#        self.data[:, i] = arr
        self.data[colName] = arr
    
    def getData(self, colName):
#        i = self.columnNames.index(colName)
#        return self.data[:, i]
        return self.data[colName]
            