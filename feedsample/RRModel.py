'''
Created on Oct 2, 2012

@author: jmccormick
'''
import numpy as np

def fromRRYtoRetained(rr):
    '''
    gets the percent retained from the size
    Evaluates R(d)
    '''
    return 100 / (10 ** ( 10 ** ( 0.301 - ((rr - 1) / 36.83) ) ) )

def toRRXaxis(size):
    return np.log10(size)
    
def createRRYValues(retainedArray):
    return ( 1 + (98 * (0.301 - np.log10(np.log10(100.0 / retainedArray)))/2.661) )
    