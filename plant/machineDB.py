# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:21:53 2013

@author: jmccormick
"""
import numpy as np

def ep1(d50, f):
    return (f['A1']*d50 + f['A2'])*f['F1']*f['F2']*f['F3']
    
def ep2(d50, f):
    return f['F1']*f['F2']*f['F3']
    

def HMC():
    return {'PN': np.array([100.00,99.00,98.50,98.00,97.40,97.00,96.00,95.00,94.00,93.00,91.40,90.00,75.00,50.00,25.00,10.00,8.00,7.00,6.00,5.00,4.40,3.80,3.30,2.60,2.00,1.60,1.40,1.10,1.00,0.60,0.00]),
       'RD': np.array([-9.00,-6.10,-4.80,-3.90,-3.26,-3.00,-2.60,-2.30,-2.06,-1.90,-1.75,-1.70,-1.00,0.00,1.00,1.80,2.00,2.16,2.38,2.60,2.85,3.17,3.50,4.00,4.70,5.50,6.00,7.00,8.00,9.86,12.00]),
       'epFactors': {'A1': 0.027, 'A2': -0.01, 'F1': 0.91, 'F2': 1.10, 'F3': 1.00},
       'Ep': ep1}

def HMV():
    return {'PN': np.array([100.00,99.00,98.00,97.20,96.50,95.80,95.00,94.00,92.00,90.40,90.00,88.00,84.00,75.00,50.00,25.00,16.00,12.00,10.00,8.00,6.20,5.00,3.40,2.40,2.00,1.40,1.00,0.60,0.30,0.20,0.00]),
       'RD': np.array([-5.00,-4.00,-3.30,-2.90,-2.50,-2.25,-2.00,-1.91,-1.73,-1.65,-1.60,-1.50,-1.38,-1.00,0.00,1.00,1.49,1.67,1.80,2.15,2.55,2.90,3.42,4.00,4.20,4.90,5.50,6.25,7.00,7.25,8.00]),
       'epFactors': {'A1': 0.027, 'A2': -0.01, 'F1': 0.88, 'F2': 1.10, 'F3': 1.00},
       'Ep': ep1}
     
def SPIRALS():
    return {'PN': np.array([100,99.5,99,98.5,98,97,96,95,93,90,85,80,75,50,25,22,20,17,15,12.5,10,9,7,5,4,3,2,1.5,1,0.5,0]),
       'RD': np.array([-4.29,-4.24,-4,-3.82,-3.65,-3.35,-3.12,-2.88,-2.53,-2.03,-1.47,-1.12,-0.88,0,1.12,1.26,1.41,1.59,1.71,1.88,2.12,2.21,2.41,2.65,2.78,3,3.24,3.47,3.71,4.06,4.53]),
       'epFactors': {'A1': 0.0, 'A2': 0.0, 'F1': 0.149, 'F2': 1.00, 'F3': 1.00},
       'Ep': ep2}