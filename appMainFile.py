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


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

from matplotlib.animation import FuncAnimation




import appWindowDesign

from exception_handling import Maybe
from exception_handling import myInputError

from Maths.CP_Maths import extended_complex_plane_CP
from Maths.CP_Maths import Steiner_grids_CP
from Maths.CP_Maths import Mobius_CP

#### SOME FUNCTIONS IMPORTED FROM Maths.CP_Maths.extended_complex_plane_CP
oo = extended_complex_plane_CP.numpyExtendedComplexPlane().oo
coords = extended_complex_plane_CP.numpyExtendedComplexPlane().coords
isooInArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().isooInArgs
isooInList = extended_complex_plane_CP.numpyExtendedComplexPlane().isooInList
extendedValue = extended_complex_plane_CP.numpyExtendedComplexPlane().extendedValue
areAllDistinctArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().areAllDistinctArgs
areAllDistinctList = extended_complex_plane_CP.numpyExtendedComplexPlane().areAllDistinctList
removeooFromArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().removeooFromArgs
removeooFromList = extended_complex_plane_CP.numpyExtendedComplexPlane().removeooFromList
e_circumcenter_and_radius = extended_complex_plane_CP.numpyExtendedComplexPlane().e_circumcenter_and_radius
####



class appMainWindow(QtWidgets.QDialog, appWindowDesign.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(appMainWindow,self).__init__(parent)
        self.setupUi(self)
        


##################
##################
##### AXES LIMITS for PlotWidgetIn_pageCP

        self.CP_absolute_lim = 100
        self.CP_xlim_left = -self.CP_absolute_lim
        self.CP_xlim_right = self.CP_absolute_lim
        self.CP_ylim_down = -self.CP_absolute_lim
        self.CP_ylim_up = self.CP_absolute_lim
        
        self.PlotWidgetIn_pageCP.setXRange(self.CP_xlim_left,self.CP_xlim_right)
#        self.graphicsView_2.setYRange(self.CP_ylim_down,self.CP_ylim_up)
        self.PlotWidgetIn_pageCP.setAspectLocked(1.0)



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
        self.horizontalSliderCPSGLoxodromesAngleTheta.sliderMoved.connect(self.effectOf_horizontalSliderCPSGLoxodromesAngleTheta)
        
        self.pushButtonCPMTOrbitsSinglePoint.clicked.connect(self.effectOf_pushButtonCPMTOrbitsSinglePoint) ### PERSONAL NOTE: this effect has not been fully/satisfactorily programmed
        self.pushButtonCPMTOrbitsRandomCircle.clicked.connect(self.effectOf_pushButtonCPMTOrbitsRandomCircle)













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
        if self.timer:
            self.timer.stop()
            del self.timer
#        self.timer.stop()
#        self.timer = None
#        del self.timer
        self.PlotWidgetIn_pageCP.clear()

        

    def effectOf_pushButtonCPSGCommon(self):
        #### PERSONAL: should I move the bulk of operations to Steiner_grids_CP.py?
        #I think doing so would create a mess because there would be more dependencies
        try:
            P = extendedValue(self.lineEditCPSGComplexNumber1.text())
            Q = extendedValue(self.lineEditCPSGComplexNumber2.text())
            n = int(self.spinBoxCPSGCommon.cleanText())
            if isooInArgs(P,Q) == False:
                centersAndRadii = Steiner_grids_CP.commonCircles().common_circlesFunction(
                        P, Q, n )
                theta = numpy.linspace(0,1,101)
                for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
                    x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
                    y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
                    self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen="w")
            else:
                finitePoint = removeooFromArgs(P,Q)[0]
                theta = numpy.linspace(0,360,n)
                for t in theta: ### triple comes in the format [[R.real,R.imag],P], where R and P are (finite) complex numbers. PERSONAL NOTE: This is NOT elegant!!!!!!
                    line = pg.InfiniteLine(pos = [finitePoint.real,finitePoint.imag], angle = t, pen='r')
                    self.PlotWidgetIn_pageCP.addItem(line)
        except: #### Implement a pop-up window???
            pass
            
    def effectOf_pushButtonCPSGApollonius(self): ## WARNING(?): THE EXACT SAME CODE APPEARS TWICE, EXCEPT FOR importing.Apollonius_e_circles1 AND importing.Apollonius_e_circles2
        try:
            P = extendedValue(self.lineEditCPSGComplexNumber1.text())
            Q = extendedValue(self.lineEditCPSGComplexNumber2.text())
            n = int(self.spinBoxCPSGCommon.cleanText())
            if isooInArgs(P,Q) == False:
                centersAndRadii = Steiner_grids_CP.Apollonius().Apollonius_e_circles1(
                        P,Q,n)
                theta = numpy.linspace(0,1,101)
                for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
                    x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
                    y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
                    self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen ="w")
                centersAndRadii = Steiner_grids_CP.Apollonius().Apollonius_e_circles2(
                        P,Q,n)
                theta = numpy.linspace(0,1,101)
                for triple in centersAndRadii: ### triple comes in the format [(x,y),r]
                    x_coord = (triple[0])[0] + (triple[1])*numpy.cos(theta*2*numpy.pi)
                    y_coord = (triple[0])[1] + (triple[1])*numpy.sin(theta*2*numpy.pi)
                    self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen="w")
            else:
                finitePoint = removeooFromArgs(P,Q)[0]
                theta = numpy.linspace(0,1,101)
                for t in range(1,(n)**2+1,n):
                    x_coord = finitePoint.real + t*numpy.cos(theta*2*numpy.pi)
                    y_coord = finitePoint.imag + t*numpy.sin(theta*2*numpy.pi)
                    self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen="w")
        except:
            pass
                
    def effectOf_pushButtonCPSGSteiner(self):
        self.effectOf_pushButtonCPSGCommon()
        self.effectOf_pushButtonCPSGApollonius()
        x = numpy.arange(0,10,1)
        y = x**2
        point = pg.ScatterPlotItem(x,y)
        self.PlotWidgetIn_pageCP.addItem(point)
        
    
        
    
    def effectOf_horizontalSliderCPSGLoxodromesAngleTheta(self):
        try:
            self.PlotWidgetIn_pageCP.clear()
            P = extendedValue(self.lineEditCPSGComplexNumber1.text())
            Q = extendedValue(self.lineEditCPSGComplexNumber2.text())
            n = int(self.spinBoxCPSGCommon.cleanText())
            theta = int(self.horizontalSliderCPSGLoxodromesAngleTheta.value())*2*numpy.pi/360
            for k in range(0,n,1):
                self.PlotWidgetIn_pageCP.plot((Steiner_grids_CP.loxodromes().loxCurve(P,Q,theta,n))[k][0],(Steiner_grids_CP.loxodromes().loxCurve(P,Q,theta,n)[k][1]),pen='w')
        except:
            pass
        
        
        
        
        
        
        
        
        
        
#############################################
##############
############## Something strange happens when one clicks on "Clear Canvas" and then
############## tries to plot the orbit of a new point   



    def effectOf_pushButtonCPMTOrbitsSinglePoint(self):
        MobiusTrans = Mobius_CP.MobiusAssocToMatrix(
                self.lineEditCPMTOrbitsComplexNumberalpha.text(),
                self.lineEditCPMTOrbitsComplexNumberbeta.text(),
                self.lineEditCPMTOrbitsComplexNumbergamma.text(),
                self.lineEditCPMTOrbitsComplexNumberdelta.text())
        z_0 = extendedValue(self.lineEditCPMTOrbitsComplexNumberz_0.text())
        numberOfPointsInOrbit = int(self.spinBoxCPMTOrbits.cleanText())
        Orbit = MobiusTrans.Mob_trans_iterable(z_0,numberOfPointsInOrbit)

        
        if z_0 != oo:
            self.radioButtonCPoo.setChecked(False)
            initialDot = pg.ScatterPlotItem([z_0.real],[z_0.imag],pen='w',brush='b')
            self.PlotWidgetIn_pageCP.addItem(initialDot)
        else:
            self.radioButtonCPoo.setChecked(True)
            
        
        k=0
        def update():
            self.radioButtonCPoo.setChecked(False)
            nonlocal k
            previous_z = Orbit[k]
            if previous_z != oo:
                previousDot = pg.ScatterPlotItem([previous_z.real],[previous_z.imag],pen='r')
                self.PlotWidgetIn_pageCP.addItem(previousDot)
            current_z = Orbit[(k+1)%numberOfPointsInOrbit]
            if current_z !=oo:
                currentDot = pg.ScatterPlotItem([current_z.real],[current_z.imag],pen='w',brush='b')
                self.PlotWidgetIn_pageCP.addItem(currentDot)
            else:
                self.radioButtonCPoo.setChecked(True)
            k = (k+1)%numberOfPointsInOrbit
        #    QtCore.QTimer.singleShot(1000, update)
        #update()
        
        
#        timer = QtCore.QTimer(self)
#        timer.timeout.connect(update)
#        timer.start(250)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(update)
        self.timer.start(250)
        
        
    



##############
############## 
#############################################
 
        
    def effectOf_pushButtonCPMTOrbitsRandomCircle(self):
        alpha = self.lineEditCPMTOrbitsComplexNumberalpha.text() 
        beta = self.lineEditCPMTOrbitsComplexNumberbeta.text()
        gamma = self.lineEditCPMTOrbitsComplexNumbergamma.text()
        delta = self.lineEditCPMTOrbitsComplexNumberdelta.text()
        MobiusTrans = Mobius_CP.MobiusAssocToMatrix(alpha,beta,gamma,delta)
        P = numpy.complex(numpy.random.random(), numpy.random.random())
        Q = numpy.complex(numpy.random.random(), numpy.random.random())
        R = numpy.complex(numpy.random.random(), numpy.random.random())
        numberOfPointsInOrbit = int(self.spinBoxCPMTOrbits.cleanText())
        OrbitP = MobiusTrans.Mob_trans_iterable(P,numberOfPointsInOrbit)
        OrbitQ = MobiusTrans.Mob_trans_iterable(Q,numberOfPointsInOrbit)
        OrbitR = MobiusTrans.Mob_trans_iterable(R,numberOfPointsInOrbit)
        centersAndRadii = [e_circumcenter_and_radius(OrbitP[k],OrbitQ[k],OrbitR[k]) for k in range(0,numberOfPointsInOrbit,1)]
        t = numpy.linspace(0, 2*numpy.pi,500)
#        for k in range(0,numberOfPointsInOrbit,1):
#            x_coord = ((centersAndRadii[k])[0])[0] + (centersAndRadii[k])[1]*numpy.cos(t)
#            y_coord = ((centersAndRadii[k])[0])[1] + (centersAndRadii[k])[1]*numpy.sin(t)
#            self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen="b")
        x_coord = ((centersAndRadii[0])[0])[0] + (centersAndRadii[0])[1]*numpy.cos(t)
        y_coord = ((centersAndRadii[0])[0])[1] + (centersAndRadii[0])[1]*numpy.sin(t)
        self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen="w")
        k = 0
        def update():
            nonlocal k
            X_current = ((centersAndRadii[k])[0])[0] + (centersAndRadii[k])[1]*numpy.cos(t)
            Y_current = ((centersAndRadii[k])[0])[1] + (centersAndRadii[k])[1]*numpy.sin(t)
            #C = pyqtgraph.hsvColor(time.time()/5%1,alpha=.5)
            #pen=pyqtgraph.mkPen(color=C,width=10)
            self.PlotWidgetIn_pageCP.plot(X_current,Y_current,pen='r',clear=False)
            X_next = ((centersAndRadii[(k+1)%numberOfPointsInOrbit])[0])[0] + (centersAndRadii[(k+1)%numberOfPointsInOrbit])[1]*numpy.cos(t)
            Y_next = ((centersAndRadii[(k+1)%numberOfPointsInOrbit])[0])[1] + (centersAndRadii[(k+1)%numberOfPointsInOrbit])[1]*numpy.sin(t)
            #C = pyqtgraph.hsvColor(time.time()/5%1,alpha=.5)
            #pen=pyqtgraph.mkPen(color=C,width=10)
            self.PlotWidgetIn_pageCP.plot(X_next,Y_next,pen='w',clear=False)
            k = (k+1)%numberOfPointsInOrbit
        #    QtCore.QTimer.singleShot(1000, update)
        #update()
        
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(update)
        self.timer.start(100)
        
            
        
#        
#        
#        line, = self.mplWidgetIn_pageCP.canvas.axis.plot(
#                ((centersAndRadii[0])[0])[0] + (centersAndRadii[0])[1]*numpy.cos(t),
#                ((centersAndRadii[0])[0])[1] + (centersAndRadii[0])[1]*numpy.sin(t),
#                'r-', linewidth=3)       
#        def update(k):
#            # Update the line and the axes (with a new xlabel). Return a tuple of
#            # "artists" that have to be redrawn for this frame.
#            line.set_xdata(((centersAndRadii[k])[0])[0] + (centersAndRadii[k])[1]*numpy.cos(t))
#            line.set_ydata(((centersAndRadii[k])[0])[1] + (centersAndRadii[k])[1]*numpy.sin(t))
#            return line,
#
#        anim = FuncAnimation(self.mplWidgetIn_pageCP.canvas.fig, update,
#                             #init_func=init,
#                             frames=numberOfPointsInOrbit,interval=250,blit=True)
#        self.mplWidgetIn_pageCP.canvas.draw()        

        
        
        
        
            
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