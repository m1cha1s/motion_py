from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, Qt, plot
import pyqtgraph as pg
import numpy as np
import sys
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

    def plotData(self, data:np.array):
        self.graphWidget.plotItem