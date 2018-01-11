#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:53:06 2018

@author: daniellabardini
"""

from PyQt5 import QtWidgets
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
import sys
import matplotlib

import appWindowDesign

class appMainWindow(QtWidgets.QDialog, appWindowDesign.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(appMainWindow,self).__init__(parent)
        self.setupUi(self)
        



#####
##### Daniel's own configuration of some buttons, signals and slots,
##### for navigation through the app's pages     
        
        self.toolButtonHome.clicked.connect(self.effectOf_toolButtonHome)
        self.toolButtonCP.clicked.connect(self.effectOf_toolButtonCP)
        self.toolButtonHP.clicked.connect(self.effectOf_toolButtonHP)
        self.toolButtonTS.clicked.connect(self.effectOf_toolButtonTS)
        self.toolButtonMS.clicked.connect(self.effectOf_toolButtonMS)
        self.toolButtonArt.clicked.connect(self.effectOf_toolButtonArt)
        
        
    def effectOf_toolButtonHome(self):
        self.stackedWidgetAllPages.setCurrentIndex(0)
    
    def effectOf_toolButtonCP(self):
        self.stackedWidgetAllPages.setCurrentIndex(1)
    
    def effectOf_toolButtonHP(self):
        self.stackedWidgetAllPages.setCurrentIndex(2)
    
    def effectOf_toolButtonTS(self):
        self.stackedWidgetAllPages.setCurrentIndex(3)
    
    def effectOf_toolButtonMS(self):
        self.stackedWidgetAllPages.setCurrentIndex(4)
    
    def effectOf_toolButtonArt(self):
        self.stackedWidgetAllPages.setCurrentIndex(5)
        
        






        
        
        
app = QtWidgets.QApplication(sys.argv)
form = appMainWindow()
form.show()
app.exec_()

