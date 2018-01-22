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

from matplotlib.animation import FuncAnimation




import appWindowDesign

from Maths.CP_Maths import extended_complex_plane_CP
from Maths.CP_Maths import Steiner_grids_CP
from Maths.CP_Maths import Mobius_CP





class appMainWindow(QtWidgets.QDialog, appWindowDesign.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(appMainWindow,self).__init__(parent)
        self.setupUi(self)
        
        
        
##################
##################
##### AXES LIMITS

        self.CP_absolute_lim = 100
        self.CP_xlim_left = -self.CP_absolute_lim
        self.CP_xlim_right = self.CP_absolute_lim
        self.CP_ylim_down = -self.CP_absolute_lim
        self.CP_ylim_up = self.CP_absolute_lim
        
        self.mplWidgetIn_pageCP.canvas.axis.set_xlim(self.CP_xlim_left,self.CP_xlim_right)
        self.mplWidgetIn_pageCP.canvas.axis.set_ylim(self.CP_ylim_down,self.CP_ylim_up)

                
        








####################
####################
##### IMPORTED FUNCTIONS - beginning

        self.coords = extended_complex_plane_CP.coordsOfComplex().coords ## This is the vectorized version of coordsFunction
        self.coordsFunction = extended_complex_plane_CP.coordsOfComplex().coordsFunction
        
        self.common_circles = Steiner_grids_CP.commonCircles().common_circles
        self.Apollonius_e_circles1 = Steiner_grids_CP.Apollonius().Apollonius_e_circles1
        self.Apollonius_e_circles2 = Steiner_grids_CP.Apollonius().Apollonius_e_circles2
        self.commonCirclesFunction = Steiner_grids_CP.commonCircles().commonCirclesFunction
        
        self.MobiusAssocToMatrix = Mobius_CP.MobiusAssocToMatrix ## This is a class, not a function

##### IMPORTED FUNCTIONS - end
####################
####################


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
        self.pushButtonCPMTOrbitsSinglePoint.clicked.connect(self.effectOf_pushButtonCPMTOrbitsSinglePoint) ### PERSONAL NOTE: this effect has not been fully/satisfactorily programmed
        self.pushButtonCPMTOrbitsRandomCircle.clicked.connect(self.effectOf_pushButtonCPMTOrbitsRandomCircle) ### PERSONAL NOTE: polish this
        













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
        self.mplWidgetIn_pageCP.canvas.axis.set_xlim(self.CP_xlim_left,self.CP_xlim_right)
        self.mplWidgetIn_pageCP.canvas.axis.set_ylim(self.CP_ylim_down,self.CP_ylim_up)
        self.mplWidgetIn_pageCP.canvas.draw()
        

    def effectOf_pushButtonCPSGCommon(self): #### PERSONAL: should I move the bulk of operations to Steiner_grids_CP.py? 
        centersAndRadii = self.common_circles(
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
        centersAndRadii = self.Apollonius_e_circles1(
                self.lineEditCPSGComplexNumber1.text(),
                self.lineEditCPSGComplexNumber2.text(),
                int(self.spinBoxCPSGCommon.cleanText()))
        theta = numpy.linspace(0,1,101)
        for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
            x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
            y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
            self.mplWidgetIn_pageCP.canvas.axis.plot(x_coord,y_coord,color ="b")
        self.mplWidgetIn_pageCP.canvas.draw()
        centersAndRadii = self.Apollonius_e_circles2(
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
        
        
        
        
        
        
        
        
        
        
        
        
        
#############################################
##############
############## I still have to figure out how to plot an animation of the orbit of a point        
    def effectOf_pushButtonCPMTOrbitsSinglePoint(self):
        MobiusTrans = self.MobiusAssocToMatrix(
                self.lineEditCPMTOrbitsComplexNumberalpha.text(),
                self.lineEditCPMTOrbitsComplexNumberbeta.text(),
                self.lineEditCPMTOrbitsComplexNumbergamma.text(),
                self.lineEditCPMTOrbitsComplexNumberdelta.text())
        z_0 = numpy.complex(self.lineEditCPMTOrbitsComplexNumberz_0.text())
        numberOfPointsInOrbit = int(self.spinBoxCPMTOrbits.cleanText())
        Orbit = MobiusTrans.Mob_trans_iterable(z_0,numberOfPointsInOrbit)
        pointsForPlot = self.coords(Orbit)
        
        for k in range(0,numberOfPointsInOrbit,1):
            self.mplWidgetIn_pageCP.canvas.axis.plot((pointsForPlot[0])[k],(pointsForPlot[1])[k],'ob')
        line, = self.mplWidgetIn_pageCP.canvas.axis.plot((pointsForPlot[0])[0],(pointsForPlot[1])[0],marker='o',color='r')

        def update(i):
            # Update the line and the axes (with a new xlabel). Return a tuple of
            # "artists" that have to be redrawn for this frame.
            line.set_xdata((pointsForPlot[0])[i])
            line.set_ydata((pointsForPlot[1])[i])
            return line, 
#        x = numpy.arange(0, 20, 0.1)
#        self.mplWidgetIn_pageCP.canvas.axis.scatter(x, x + numpy.random.normal(0, 3.0, len(x)))
#        line, = self.mplWidgetIn_pageCP.canvas.axis.plot(x, x - 5, 'r-', linewidth=2)
#
#        def update(i):
#            # Update the line and the axes (with a new xlabel). Return a tuple of
#            # "artists" that have to be redrawn for this frame.
#            line.set_ydata(x - 5 + i)
#            return line, 
                
#        initialPlot, = self.mplWidgetIn_pageCP.canvas.axis.plot((pointsForPlot[0])[0],(pointsForPlot[1])[0],'or', animated = True)
#        
##        def init():
##            initialPlot.set_data([],[])
##            return initialPlot,
#        
#        def animate(k):
#            x = (pointsForPlot[0])[k]
#            y = (pointsForPlot[1])[k]
#            print(x,y)
#            initialPlot.set_data(x,y)
#            return initialPlot,
#        
        anim = FuncAnimation(self.mplWidgetIn_pageCP.canvas.fig, update,
                             #init_func=init,
                             frames=numberOfPointsInOrbit,interval=500,blit=True)
        self.mplWidgetIn_pageCP.canvas.draw()
##        for k in range(0,numberOfPointsInOrbit,1):
##            self.mplWidgetIn_pageCP.canvas.axis.plot((pointsForPlot[0])[k],(pointsForPlot[1])[k],'ob')
##            self.mplWidgetIn_pageCP.canvas.draw()
##            
##        
#                
#        
#      

##############
############## 
#############################################
 
        
    def effectOf_pushButtonCPMTOrbitsRandomCircle(self):
        MobiusTrans = self.MobiusAssocToMatrix(
                self.lineEditCPMTOrbitsComplexNumberalpha.text(),
                self.lineEditCPMTOrbitsComplexNumberbeta.text(),
                self.lineEditCPMTOrbitsComplexNumbergamma.text(),
                self.lineEditCPMTOrbitsComplexNumberdelta.text())
        P = numpy.complex(numpy.random.random()*self.CP_absolute_lim, numpy.random.random()*self.CP_absolute_lim)
        Q = numpy.complex(numpy.random.random()*self.CP_absolute_lim, numpy.random.random()*self.CP_absolute_lim)
        R = numpy.complex(numpy.random.random()*self.CP_absolute_lim, numpy.random.random()*self.CP_absolute_lim)
        numberOfPointsInOrbit = int(self.spinBoxCPMTOrbits.cleanText())
        OrbitP = MobiusTrans.Mob_trans_iterable(P,numberOfPointsInOrbit)
        OrbitQ = MobiusTrans.Mob_trans_iterable(Q,numberOfPointsInOrbit)
        OrbitR = MobiusTrans.Mob_trans_iterable(R,numberOfPointsInOrbit)
        
        centersAndRadii = [(self.commonCirclesFunction(OrbitP[k],OrbitQ[k]))(OrbitR[k]) for k in range(0,numberOfPointsInOrbit,1)]
        
        t = numpy.linspace(0, 2*numpy.pi,500)
        
        print(MobiusTrans.fixedPoints()[0])
        print(MobiusTrans.fixedPoints()[1])
        print(self.coordsFunction(MobiusTrans.fixedPoints()[0]))
        print(self.coordsFunction(MobiusTrans.fixedPoints()[1]))
        
        
#        self.mplWidgetIn_pageCP.canvas.axis.plot(
#                self.coordsFunction(MobiusTrans.fixedPoints()[0])[0],
#                self.coordsFunction(MobiusTrans.fixedPoints()[0])[1],'ro')        
#        self.mplWidgetIn_pageCP.canvas.axis.plot(
#                self.coordsFunction(MobiusTrans.fixedPoints()[1])[0],
#                self.coordsFunction(MobiusTrans.fixedPoints()[1])[1],'ro')
#        
        for k in range(0,numberOfPointsInOrbit,1):
            self.mplWidgetIn_pageCP.canvas.axis.plot(
                ((centersAndRadii[k])[0])[0] + (centersAndRadii[k])[1]*numpy.cos(t),
                ((centersAndRadii[k])[0])[1] + (centersAndRadii[k])[1]*numpy.sin(t),'b-')
            
        line, = self.mplWidgetIn_pageCP.canvas.axis.plot(
                ((centersAndRadii[0])[0])[0] + (centersAndRadii[0])[1]*numpy.cos(t),
                ((centersAndRadii[0])[0])[1] + (centersAndRadii[0])[1]*numpy.sin(t),
                'r-', linewidth=2)       
        def update(k):
            # Update the line and the axes (with a new xlabel). Return a tuple of
            # "artists" that have to be redrawn for this frame.
            line.set_xdata(((centersAndRadii[k])[0])[0] + (centersAndRadii[k])[1]*numpy.cos(t))
            line.set_ydata(((centersAndRadii[k])[0])[1] + (centersAndRadii[k])[1]*numpy.sin(t))
            line.set_linewidth(3)
            return line,

        anim = FuncAnimation(self.mplWidgetIn_pageCP.canvas.fig, update,
                             #init_func=init,
                             frames=numberOfPointsInOrbit,interval=250,blit=True)
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

