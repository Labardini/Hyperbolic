#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:32:00 2018

@author: daniellabardini
"""

# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111,aspect = "equal")
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.mpl_toolbar = NavigationToolbar(self.canvas,parent) # Include toolbar --it appears at the bottom
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.mpl_toolbar)
        self.setLayout(self.vbl)