'''
Created on Jun 4, 2012

@author: jmccormick
'''
from ..feedsample import rrmodel
import numpy as np
from PyQt4 import QtGui

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib.ticker import FixedLocator, FuncFormatter
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

textSize = 8

# Generate the y tick labels 
OrYLabels = [1, 2, 3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 
             55, 60, 65, 70, 75, 80, 82, 85, 88, 90, 91, 92, 93, 94, 
             95, 96, 97, 97.5, 98, 98.5, 99]
YLabels = np.asarray(OrYLabels, dtype=np.float32)
YLabels = rrmodel.createRRYValues(YLabels)
#YLabels = np.log10(np.log10(100.0 / (YLabels)))
YLabelsList = YLabels.tolist()

# Generate the x tick labels
# The original list is in mm
OrMajorXLabels = [0.037, 0.044, 0.053, 0.074, 0.088, 0.104, 0.147, 0.20, 0.246, 
                  0.295, 0.4, 0.5, 0.589, 0.8, 0.9, 1.0, 1.168, 1.397, 1.651, 1.981, 2.362, 
                  3.327, 4.7625, 6.35, 7.9375, 9.525, 12.7, 15.875, 19.05,
                  22.225, 25.4, 31.75, 38.1, 44.45, 50.8, 63.5, 76.2, 88.9, 101.6, 127]
xLabels = np.asarray(OrMajorXLabels, dtype=np.float32)
xLabels = np.log10(xLabels)
XLabelsList = xLabels.tolist()

def yLabelFormat(y, pos):    
    i = YLabelsList.index(y)
    return OrYLabels[i]

def xLabelFormat(x, pos):    
    i = XLabelsList.index(x)
    if(x < 1.0):
        return "{:.3f}".format(OrMajorXLabels[i])
    else:
        return "{:.2f}".format(OrMajorXLabels[i])
    
class RRCanvas(FigureCanvas):
    """A canvas that displays an RR plot"""
    def __init__(self, parent=None, width=5, height=4.5, dpi=100):
        plt.rc('axes', grid=True)
        plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)

        fig = plt.figure(figsize=(width, height), dpi=dpi, facecolor='white')
        self.axescolor = '#f6f6f6'

        self.axes = fig.add_subplot(111, axisbg=self.axescolor)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.setUpPlot()
        
        
    def setUpPlot(self):
        self.axes.tick_params(labelsize=textSize)
        self.axes.yaxis.set_major_formatter(FuncFormatter(yLabelFormat))
        self.axes.xaxis.set_major_formatter(FuncFormatter(xLabelFormat))
        self.axes.yaxis.set_major_locator(FixedLocator(YLabelsList))
        self.axes.xaxis.set_major_locator(FixedLocator(XLabelsList))
        self.axes.set_xlim(xLabels[0], xLabels[-1])
        self.axes.set_ylim(YLabels[-1], YLabels[0])
        self.axes.set_ylabel('% Retained')
        self.axes.set_xlabel('Particle Size (mm)')
        self.axes.set_title(label="Rosin Rammler Screen Analysis Chart", size=12)
        for label in self.axes.get_xticklabels():
            label.set_rotation(45)
            label.set_horizontalalignment('right')   
    
    def updatePlot(self, distroList):
        self.axes.cla()
        self.setUpPlot()
        for l in distroList:
            self.addDistribution(l)
        
        props = font_manager.FontProperties(size=textSize)
        self.axes.legend(prop=props, loc='best')

        self.draw()
    
    def addDistribution(self, sizeDistro):
        xfit = np.linspace(xLabels[0], xLabels[-1], 50)
        yfit = sizeDistro.getLine(xfit)
        x, y = sizeDistro.getRRPoints()
        # Draw the plot
        legendLabel = sizeDistro.properties.name + ' - Original'
        self.axes.plot(x, y, sizeDistro.properties.pointStyle, color=sizeDistro.properties.pointColor, label=legendLabel)
        legendLabel = sizeDistro.properties.name + ' - Fitted line'
        self.axes.plot(xfit, yfit, linestyle=sizeDistro.properties.lineStyle, color=sizeDistro.properties.lineColor, label=legendLabel)
        
        
    def savePlot(self, filename):
        self.figure.savefig(filename)
        