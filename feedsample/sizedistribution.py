'''
Created on Jun 5, 2012

@author: jmccormick
'''
import rrmodel
import numpy as np
from scipy.interpolate import interp1d

from lineProperties import LineProperties

class sizedistribution(object):
    '''
    A class to handle a size distribution
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.size = []
        self.cumalativeWt = []
        self.rrX = []
        self.rrY = []
        self.interpFunc = None   # The interpolation function
        self.properties = LineProperties()
    
    def getCumalativeWt(self, size):
        '''
        gets the percent cumalativeWt from the size
        Evaluates R(d)
        '''
        size = np.log10(size)
        y = self.interpFunc(size)
        return rrmodel.fromRRYtoRetained(y)
    
#    def getSizeFromRetained(self, retained):
#        y = rrmodel.createRRYValues(retained)
#        x = (y - self.interceptRR) / self.slopeRR
#        return 10 ** x
    
    def generateFractional(self, cumalativeWt):
        fractionalWt = []
        last = cumalativeWt[0]
        for c in cumalativeWt:
            fractionalWt.append(last-c)
            last = c
        fractionalWt.pop(0)
        return fractionalWt
        
    def generateMidpointSizes(self, sizeArray):
        avg = []
        last = sizeArray[0]
        for c in sizeArray:
            avg.append( (c+last) / 2.0 )
            last = c
        avg.pop(0)
        return avg
        
    def getRangeCumalativeWt(self, upperLimit, lowerLimit):
        lower = self.getCumalativeWt(lowerLimit)
        upper = self.getCumalativeWt(upperLimit)
        return (lower-upper)
    
    def getMassMeanDiameter(self, upperLimit, lowerLimit):
        xArray = np.linspace(lowerLimit, upperLimit, 20)
        retained = self.getCumalativeWt(xArray)
        fractionalWt = self.generateFractional(retained)
        midPointsArray = self.generateMidpointSizes(xArray)
        midPointsArray = midPointsArray / self.getRangeCumalativeWt(upperLimit, lowerLimit)
        massMeanDia = np.dot(fractionalWt, midPointsArray)
        return massMeanDia
        
    def getAverageGrainSize(self, upperLimit, lowerLimit):
        xArray = np.linspace(lowerLimit, upperLimit, 20)
        retained = self.getCumalativeWt(xArray)
        midPointsArray = self.generateMidpointSizes(xArray)
        fractionalWt = self.generateFractional(retained)
        avgArray = np.divide(fractionalWt, midPointsArray)
        avgSum = np.sum(avgArray)
        precentRetained = self.getRangeCumalativeWt(upperLimit, lowerLimit)
        return (precentRetained/avgSum)
    
    def getRRPoints(self):
        return self.rrX, self.rrY
    
    def getLine(self, xArray):
        return self.interpFunc(xArray)
    
    def buildFitLine(self):
        # Need to reverse the order of the arrays in order to get the interp1d to work properly
        x = self.rrX[::-1]
        y = self.rrY[::-1]
        self.interpFunc = interp1d(x, y, kind='cubic')
        
    def loadData(self, size, cumWt):
        s = []
        r = []
        count = len(size)
        for i in range(0, count):
            if float(size[i]) > 0.0 and float(cumWt[i]) > 0.0:
                s.append(float(size[i]))
                r.append(float(cumWt[i]))
        self.size = np.asfarray(s, dtype=np.float32)
        self.cumalativeWt = np.asfarray(r, dtype=np.float32)
        
        self.rrX = np.log10(self.size)
        self.rrY = rrmodel.createRRYValues(self.cumalativeWt)
        self.buildFitLine()