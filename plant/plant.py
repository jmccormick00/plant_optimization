# -*- coding: utf-8 -*-
"""
Created on Thu May 02 22:30:25 2013

@author: James McCormick
"""

class plant:
    
    def __init__(self, name):
        self.unitList = []
        self.name = name
        
    def addUnit(self, unit):
        self.unitList.append(unit)   
    
    def solve(self, d50s, feedSample):
            ''' Computes the following for the current plant:
                    -plant yield
                    -solves the following equation to compute the
                     overall value for each attribute.
                         assume for each machine the following variables:
                             s = size fraction
                             y = size fraction yield
                             q = attribute value
                         overall q = num / denom
                         num = sum for each unit in unitList: (s*y*q)
                         denom = sum for each unit in unitList: (s*y)
            '''
            num = dict.fromkeys(feedSample.attr, 0.0)
            denom = dict.fromkeys(feedSample.attr, 0.0)
            pNum = 0.0
            pDenom = 1.0
            result = {}
            result['unitList'] = {}
            for unit in self.unitList:
                sample = feedSample.getSample(unit.topSize, unit.bottomSize)
                if sample is not None:
                    res = unit.solve(d50s[unit.name], sample['data'])
                    res['feedWt'] = sample['sizeWT']
                    result['unitList'][unit.name] = res
                    pNum += res['yield']*sample['sizeWT']
                    pDenom += sample['sizeWT']
                    for a in feedSample.attr:
                        num[a] += (res[a]*sample['sizeWT']*res['yield'])
                        denom[a] += (sample['sizeWT']*res['yield'])

            result['yield'] = pNum / pDenom            
            
            for a in feedSample.attr:
                result[a] = num[a]/denom[a]
            
            return result
            