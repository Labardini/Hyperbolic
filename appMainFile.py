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
#import matplotlib
import numpy

import appWindowDesign

from Maths.CP_Maths import Steiner_grids_CP
from Maths.CP_Maths import Mobius_CP






class appMainWindow(QtWidgets.QDialog, appWindowDesign.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(appMainWindow,self).__init__(parent)
        self.setupUi(self)
        



#####
##### Daniel's own configuration of some buttons, signals and slots,
##### for navigation through the app's pages
##### DEFINITIONS OF CONNECTIONS FOR SIGNALS
##### SEE BELOW FOR THE DEFINITIONS OF THE SIGNALS
        
        self.toolButtonHome.clicked.connect(self.effectOf_toolButtonHome)
        self.toolButtonCP.clicked.connect(self.effectOf_toolButtonCP)
        self.toolButtonHP.clicked.connect(self.effectOf_toolButtonHP)
        self.toolButtonTS.clicked.connect(self.effectOf_toolButtonTS)
        self.toolButtonMS.clicked.connect(self.effectOf_toolButtonMS)
        self.toolButtonArt.clicked.connect(self.effectOf_toolButtonArt)
        
        
        
#####
##### Daniel's own configuration of some buttons and signals that are supposed
##### to have a mathematical effect
##### DEFINITIONS OF CONNECTIONS FOR SIGNALS
##### SEE BELOW FOR THE DEFINITIONS OF THE SIGNALS

        self.pushButtonCPClearCanvas.clicked.connect(self.effectOf_pushButtonCPClearCanvas)

        self.pushButtonCPSGCommon.clicked.connect(self.effectOf_pushButtonCPSGCommon)
        self.pushButtonCPSGApollonius.clicked.connect(self.effectOf_pushButtonCPSGApollonius)
        self.pushButtonCPSGSteiner.clicked.connect(self.effectOf_pushButtonCPSGSteiner)
        self.pushButtonCPMTOrbits_1.clicked.connect(self.effectOf_pushButtonCPMTOrbits_1)













#####
##### Daniel's own configuration of some buttons, signals and slots,
##### for navigation through the app's pages 
##### DEFINITIONS OF SIGNALS


        
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
        
        
#####
##### Daniel's own configuration of some buttons and signals that are supposed
##### to have a mathematical effect
##### DEFINITIONS OF SIGNALS

    def effectOf_pushButtonCPClearCanvas(self):
        self.mplWidgetIn_pageCP.canvas.axis.clear()
        self.mplWidgetIn_pageCP.canvas.draw()
        

    def effectOf_pushButtonCPSGCommon(self): #### PERSONAL: should I move the bulk of operations to Steiner_grids_CP.py? 
        centersAndRadii = Steiner_grids_CP.commonCircles().common_circles(
                self.lineEditCPSGComplexNumber1.text(),
                self.lineEditCPSGComplexNumber2.text(),
                int(self.spinBoxCPSGCommon.cleanText()))
        theta = numpy.linspace(0,1,101)
        for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
            x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
            y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
            self.mplWidgetIn_pageCP.canvas.axis.plot(x_coord,y_coord,color ="b")
        self.mplWidgetIn_pageCP.canvas.draw()
            
    def effectOf_pushButtonCPSGApollonius(self): ## WARNING(?): THE EXACT SAME CODE APPEARS TWICE, EXCEPT FOR importing.Apollonius_e_circles1 AND importing.Apollonius_e_circles2
        centersAndRadii = Steiner_grids_CP.Apollonius().Apollonius_e_circles1(
                self.lineEditCPSGComplexNumber1.text(),
                self.lineEditCPSGComplexNumber2.text(),
                int(self.spinBoxCPSGCommon.cleanText()))
        theta = numpy.linspace(0,1,101)
        for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
            x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
            y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
            self.mplWidgetIn_pageCP.canvas.axis.plot(x_coord,y_coord,color ="b")
        self.mplWidgetIn_pageCP.canvas.draw()
        centersAndRadii = Steiner_grids_CP.Apollonius().Apollonius_e_circles2(
                self.lineEditCPSGComplexNumber1.text(),
                self.lineEditCPSGComplexNumber2.text(),
                int(self.spinBoxCPSGCommon.cleanText()))
        theta = numpy.linspace(0,1,101)
        for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
            x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
            y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
            self.mplWidgetIn_pageCP.canvas.axis.plot(x_coord,y_coord,color="b")
        self.mplWidgetIn_pageCP.canvas.draw()
                
    def effectOf_pushButtonCPSGSteiner(self):
        self.effectOf_pushButtonCPSGCommon()
        self.effectOf_pushButtonCPSGApollonius()
        
    def effectOf_pushButtonCPMTOrbits_1(self):
        MobiusTrans = Mobius_CP.MobiusAssocToMatrix(
                self.lineEditCPMTOrbitsComplexNumberalpha.text(),
                self.lineEditCPMTOrbitsComplexNumberbeta.text(),
                self.lineEditCPMTOrbitsComplexNumbergamma.text(),
                self.lineEditCPMTOrbitsComplexNumberdelta.text())
        z_0 = numpy.complex(self.lineEditCPMTOrbitsComplexNumberz_0.text())
        numberOfPointsInOrbit = int(self.spinBoxCPMTOrbits.cleanText())
        Orbit = MobiusTrans.Mob_trans_iterable(z_0,numberOfPointsInOrbit)
        print(Orbit)
        pointsForPlot = Steiner_grids_CP.coordsOfComplex().coords(Orbit)
        for k in range(0,numberOfPointsInOrbit,1):
            self.mplWidgetIn_pageCP.canvas.axis.plot((pointsForPlot[0])[k],(pointsForPlot[1])[k],'ob')
        self.mplWidgetIn_pageCP.canvas.draw()
            
        
        
        
        
        
        
        
            
#####
#####





        
        
        
app = QtWidgets.QApplication(sys.argv)
form = appMainWindow()
form.show()
app.exec_()

#if __name__ == "__main__":            
#    app = QtWidgets.QApplication(sys.argv)
#    form = appMainWindow()
#    form.show()
#    app.exec_()

