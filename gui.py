from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, Qt, plot
import pyqtgraph as pg
import numpy as np
import sys
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

    def plotData(self, data:np.ndarray, mostPoint:np.ndarray):
        self.graphWidget.addItem(pg.PlotCurveItem(x=data[0], y=data[1]))
        self.graphWidget.addItem(pg.ScatterPlotItem(x=mostPoint[0],y=mostPoint[1], size=20))
        self.graphWidget.addItem(pg.GridItem())