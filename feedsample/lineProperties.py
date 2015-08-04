'''
Created on Jun 13, 2012

@author: jr
'''

class LineProperties(object):
    '''
    classdocs
    '''

    def __init__(self, pointColor=(), pointStyle='', lineColor=(), lineStyle='', name=''):
        '''
        Constructor
        '''
        self.pointColor = pointColor
        self.pointStyle = pointStyle
        self.lineColor = lineColor
        self.lineStyle = lineStyle
        self.name = name