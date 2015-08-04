'''
Created on Jun 12, 2012

@author: jr
'''

import math

class line(object):
    '''
    A class for handling a line on the Rosin Rammler plot
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.slopeRR = None
        self.interceptRR = None
        
    def getCumalativeWt(self, size):
        '''
        gets the percent retained from the size
        Evaluates R(d)
        '''
        size = math.log10(size)
        y = self.slopeRR*size + self.interceptRR
        return (10**(10**(y))) * 100
    
    def getName(self):
        return self.name
    
    def createByOffset(self, percent):