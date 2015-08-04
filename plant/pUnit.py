# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:11:58 2013

@author: James McCormick
"""
import numpy as np
from scipy.interpolate import interp1d

class pUnit:
    ''' A class for representing a gravity seperation unit in a plant'''
    
    def __init__(self, mData, name, topSize, bottomSize):
        self.mProfile = mData
        self.name = name
        self.bottomSize = bottomSize
        self.topSize = topSize

    def buildEp(self, d50):
        #TODO - Add the size factors in calculating the Ep if they exist
        return self.mProfile['Ep'](d50, self.mProfile['epFactors'])
    
    def buildRD(self, d50, ep):
        ep = self.buildEp(d50)
        num = len(self.mProfile['RD'])
        rd = np.zeros(num)
        for x in xrange(0, num):
            rd[x] = d50 + (self.mProfile['RD'][x] * ep)
        return rd
        
        
    def buildPN(self, d50, rd, grav):
        f1 = interp1d(rd, self.mProfile['PN'])
        min = rd.min()
        max = rd.max()
        num = len(grav)
        pn = np.zeros(num)
        for x in xrange(0, num):
            if grav[x] < min:
                pn[x] = 100.0
            elif grav[x] > max:
                pn[x] = 0.01
            else:
                pn[x] = f1(grav[x])
        return pn
                
    def solve(self, d50, wash):
        res = {}
        ep = self.buildEp(d50)
        rd = self.buildRD(d50, ep)
        pn = self.buildPN(d50, rd, wash.getData('SG'))
        res['d50'] = d50
        res['Ep'] = ep
        #res['rd'] = rd
        #res['pn'] = pn
        #res['wt'] = np.multiply(wash.data['WT'], pn/100.0)
        wt = np.multiply(wash.data['WT'], pn/100.0)
        res['yield'] = wt.sum()
        # Calculate the cumalative for each attribute
        for atr in wash.attr:
            res[atr] = np.dot(wt, wash.data[atr])/res['yield']  
        return res
        
           