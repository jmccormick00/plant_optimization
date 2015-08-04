# -*- coding: utf-8 -*-
"""
Created on Thu Jun 06 20:12:13 2013

@author: James McCormick
"""

from plantsim.plant import machineDB
from plantsim.feedsample import feedsample
from plantsim.plant import pUnit
from plantsim.plant import plant
d50 = {}
d50['hmc'] = 1.633
d50['spiral'] = 1.765
sample = feedsample.feedsample('test')
sample.load('/data/Test1.csv')
hmc = pUnit.pUnit(machineDB.HMC(),'hmc', 50.00, 1.0)
spirals = pUnit.pUnit(machineDB.SPIRALS(),'spiral', 1.00, 0.15)
tPlant = plant.plant('test')
tPlant.addUnit(hmc)
tPlant.addUnit(spirals)
r = tPlant.solve(d50, sample)