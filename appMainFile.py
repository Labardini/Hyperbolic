#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:53:06 2018
@author: daniellabardini
"""
clicks = []


from PyQt5 import QtWidgets
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
import sys

import numpy


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore


import appWindowDesign

from exception_handling import Maybe
from exception_handling import myInputError

from Maths.CP_Maths import extended_complex_plane_CP
from Maths.CP_Maths import Steiner_grids_CP
from Maths.CP_Maths import Mobius_CP
from Maths.HP_Maths import UHP_Maths

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
areCollinear = extended_complex_plane_CP.numpyExtendedComplexPlane().areCollinear
####

j = 1j

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
        #self.PlotWidgetIn_pageCP.setLimits(yMin=0.0)
        self.PlotWidgetIn_pageCP.disableAutoRange()
#        self.graphicsView_2.setYRange(self.CP_ylim_down,self.CP_ylim_up)
        self.PlotWidgetIn_pageCP.setAspectLocked(1.0)




##################
##################
##### AXES LIMITS for PlotWidgetIn_pageUHP
        self.UHP_absolute_lim = 100
        self.UHP_xlim_left = -self.UHP_absolute_lim
        self.UHP_xlim_right = self.UHP_absolute_lim
        #self.UHP_ylim_down = -self.CP_absolute_lim
        self.UHP_ylim_up = self.UHP_absolute_lim
        
        self.PlotWidgetIn_pageUHP.setXRange(self.UHP_xlim_left,self.UHP_xlim_right)
        self.PlotWidgetIn_pageUHP.setLimits(yMin=0.001)
        self.PlotWidgetIn_pageUHP.disableAutoRange()
#        self.graphicsView_2.setYRange(self.CP_ylim_down,self.CP_ylim_up)
        self.PlotWidgetIn_pageUHP.setAspectLocked(1.0)




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
        self.pushButtonCPMTOrbitsSteinerGrid.clicked.connect(self.effectOf_pushButtonCPMTOrbitsSteinerGrid)

        self.PlotWidgetIn_pageUHP.scene().sigMouseClicked.connect(self.passCoordsFromPlotWidgetIn_pageUHPto_checkBoxUHPGMShowGeodesicSegments)
        #self.checkBoxUHPGMShowGeodesicSegments.stateChanged.connect(self.effectOf_checkBoxUHPGMShowGeodesicSegments)












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
        
        
#######################
##### Function for plotting any point of the extended complex plane

    def plottingPointInExtendedPlane(self,point,pen,brush):
        P = extendedValue(point)
        if P != oo:
            pointForPlot = pg.ScatterPlotItem([P.real],[P.imag],pen=pen,brush=brush)
            self.PlotWidgetIn_pageCP.addItem(pointForPlot)
        else:
            self.radioButtonCPoo.setChecked(True)
        
        
#######################        
##### Function for plotting a line or circle through three points
##### without having to worry about collinearity or about one of the points being oo
##### Notice that it plots only in PlotWidgetIn_pageCP

    def PlottingCircleOrLineThrough3Points(self,p,q,r,color):
        P,Q,R = extendedValue(p),extendedValue(q),extendedValue(r)
        if areAllDistinctArgs(P,Q,R) == False:
            raise myInputError(str(P)+','+str(R)+','+str(Q),"The points must be distinct")
        else:
            if areCollinear(P,Q,R) == False:
                centerAndRadius = e_circumcenter_and_radius(P,Q,R)## comes in format [[x,y]],radius]
                center = centerAndRadius[0]
                radius = centerAndRadius[1]
                theta = numpy.linspace(0,2*numpy.pi,500)
                x_coord = center[0] + radius*numpy.cos(theta)
                y_coord = center[1] + radius*numpy.sin(theta)
                self.PlotWidgetIn_pageCP.plot(x_coord,y_coord,pen=color)
            else:
                finitePoints = removeooFromArgs(P,Q,R)
                angleWithHorizontalLines = 180*numpy.angle(finitePoints[1]-finitePoints[0])/numpy.pi
                line = pg.InfiniteLine(pos = [finitePoints[0].real,finitePoints[0].imag], angle = angleWithHorizontalLines, pen=color)
                self.PlotWidgetIn_pageCP.addItem(line)
                
        
                
        
        
        
#####
##### Daniel's own configuration of some buttons and signals that are supposed
##### to have a mathematical effect
##### DEFINITIONS OF SIGNALS

    def effectOf_pushButtonCPClearCanvas(self):
        try:
            self.timer.stop()
            self.timer.deleteLater()
        except:
            pass
#        self.timer = None
#        del self.timer
        self.PlotWidgetIn_pageCP.clear()

##############
############## 
#############################################        

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
                    line = pg.InfiniteLine(pos = [finitePoint.real,finitePoint.imag], angle = t, pen='w')
                    self.PlotWidgetIn_pageCP.addItem(line)
        except: #### Implement a pop-up window???
            pass

##############
############## 
#############################################
            
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

##############
############## 
#############################################
                
    def effectOf_pushButtonCPSGSteiner(self):
        self.effectOf_pushButtonCPSGCommon()
        self.effectOf_pushButtonCPSGApollonius()
        x = numpy.arange(0,10,1)
        y = x**2
        point = pg.ScatterPlotItem(x,y)
        self.PlotWidgetIn_pageCP.addItem(point)
        
##############
############## 
#############################################          
    
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

##############
############## 
#############################################        
            
    def effectOf_pushButtonCPMTOrbitsSteinerGrid(self):
        nIterations = int(self.spinBoxCPMTOrbits.cleanText())
        alpha = self.lineEditCPMTOrbitsComplexNumberalpha.text() 
        beta = self.lineEditCPMTOrbitsComplexNumberbeta.text()
        gamma = self.lineEditCPMTOrbitsComplexNumbergamma.text()
        delta = self.lineEditCPMTOrbitsComplexNumberdelta.text()
        MobiusTrans = Mobius_CP.MobiusAssocToMatrix(alpha,beta,gamma,delta)
        fixedPoints = MobiusTrans.fixedPoints()
        P = fixedPoints[0]
        Q = fixedPoints[1]
        
        
        if MobiusTrans.isParEllHypLox() == 'PARABOLIC':
            ThreePoints = MobiusTrans.frameOfParabolic()[0]
            Orbit1 = MobiusTrans.Mob_trans_iterable(ThreePoints[0],nIterations)
            Orbit2 = MobiusTrans.Mob_trans_iterable(ThreePoints[1],nIterations)
            Orbit3 = MobiusTrans.Mob_trans_iterable(ThreePoints[2],nIterations)
            
            for p in ThreePoints:
                self.plottingPointInExtendedPlane(p,'y','y')
            
            k=0
            def update():
                nonlocal k
                previous_Pt1 = Orbit1[k]
                previous_Pt2 = Orbit2[k]
                previous_Pt3 = Orbit3[k]
                #self.PlottingCircleOrLineThrough3Points(previous_Pt1,previous_Pt2,previous_Pt3,'r')
                #self.PlottingCircleOrLineThrough3Points(P,previous_Pt2,Q,'b')
                previous_points = pg.ScatterPlotItem([previous_Pt1.real,previous_Pt2.real,previous_Pt3.real],[previous_Pt1.imag,previous_Pt2.imag,previous_Pt3.imag],pen='b')
                self.PlotWidgetIn_pageCP.addItem(previous_points)
                current_Pt1 = Orbit1[(k+1)%nIterations]
                current_Pt2 = Orbit2[(k+1)%nIterations]
                current_Pt3 = Orbit3[(k+1)%nIterations]
                #self.PlottingCircleOrLineThrough3Points(current_Pt1,current_Pt2,current_Pt3,'w')
                #self.PlottingCircleOrLineThrough3Points(P,current_Pt2,Q,'y')
                current_points = pg.ScatterPlotItem([current_Pt1.real,current_Pt2.real,current_Pt3.real],[current_Pt1.imag,current_Pt2.imag,current_Pt3.imag],pen='y')
                self.PlotWidgetIn_pageCP.addItem(current_points)
                k = (k+1)%nIterations
            
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(update)
            self.timer.start(500)
            
        

        
        
        
        
        if isooInArgs(P,Q) == False and P != Q:
            ThreePointsOnMediatrix = Steiner_grids_CP.commonCircles().pointsOnMediatrix(P,Q,3)
            Pt1OnMdx = ThreePointsOnMediatrix[0] 
            Pt2OnMdx = ThreePointsOnMediatrix[1]
            Pt3OnMdx = ThreePointsOnMediatrix[2]
            Orbit1 = MobiusTrans.Mob_trans_iterable(Pt1OnMdx,nIterations)
            Orbit2 = MobiusTrans.Mob_trans_iterable(Pt2OnMdx,nIterations)
            Orbit3 = MobiusTrans.Mob_trans_iterable(Pt3OnMdx,nIterations)
            
            self.PlottingCircleOrLineThrough3Points(Pt1OnMdx,Pt2OnMdx,Pt3OnMdx,'w')
            self.PlottingCircleOrLineThrough3Points(P,Pt2OnMdx,Q,'y')
            point = pg.ScatterPlotItem([Pt2OnMdx.real],[Pt2OnMdx.imag],pen='y')
            self.PlotWidgetIn_pageCP.addItem(point)
            
            k=0
            def update():
                nonlocal k
                previous_Pt1 = Orbit1[k]
                previous_Pt2 = Orbit2[k]
                previous_Pt3 = Orbit3[k]
                self.PlottingCircleOrLineThrough3Points(previous_Pt1,previous_Pt2,previous_Pt3,'r')
                self.PlottingCircleOrLineThrough3Points(P,previous_Pt2,Q,'b')
                previous_point = pg.ScatterPlotItem([previous_Pt2.real],[previous_Pt2.imag],pen='b')
                self.PlotWidgetIn_pageCP.addItem(previous_point)
                current_Pt1 = Orbit1[(k+1)%nIterations]
                current_Pt2 = Orbit2[(k+1)%nIterations]
                current_Pt3 = Orbit3[(k+1)%nIterations]
                self.PlottingCircleOrLineThrough3Points(current_Pt1,current_Pt2,current_Pt3,'w')
                self.PlottingCircleOrLineThrough3Points(P,current_Pt2,Q,'y')
                current_point = pg.ScatterPlotItem([current_Pt2.real],[current_Pt2.imag],pen='y')
                self.PlotWidgetIn_pageCP.addItem(current_point)
                k = (k+1)%nIterations
            #    QtCore.QTimer.singleShot(1000, update)
            #update()
            
    #        timer = QtCore.QTimer(self)
    #        timer.timeout.connect(update)
    #        timer.start(250)
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(update)
            self.timer.start(500)
            
        if isooInArgs(P,Q) == True and P != Q:
            finitePoint = removeooFromArgs(P,Q)[0]
            Orbit1 = MobiusTrans.Mob_trans_iterable(finitePoint+1,nIterations)
            Orbit2 = MobiusTrans.Mob_trans_iterable(finitePoint+1j,nIterations)
            Orbit3 = MobiusTrans.Mob_trans_iterable(finitePoint-1,nIterations)
            
            self.PlottingCircleOrLineThrough3Points(finitePoint+1,finitePoint+1j,finitePoint-1,'w')
            self.PlottingCircleOrLineThrough3Points(P,finitePoint+1j,Q,'y')
            point = pg.ScatterPlotItem([(finitePoint+1j).real],[(finitePoint+1j).imag])
            self.PlotWidgetIn_pageCP.addItem(point)
            
            k=0
            def update():
                nonlocal k
                previous_Pt1 = Orbit1[k]
                previous_Pt2 = Orbit2[k]
                previous_Pt3 = Orbit3[k]
                self.PlottingCircleOrLineThrough3Points(previous_Pt1,previous_Pt2,previous_Pt3,'r')
                self.PlottingCircleOrLineThrough3Points(P,previous_Pt2,Q,'b')
                previous_point = pg.ScatterPlotItem([previous_Pt2.real],[previous_Pt2.imag],pen='b')
                self.PlotWidgetIn_pageCP.addItem(previous_point)
                current_Pt1 = Orbit1[(k+1)%nIterations]
                current_Pt2 = Orbit2[(k+1)%nIterations]
                current_Pt3 = Orbit3[(k+1)%nIterations]
                self.PlottingCircleOrLineThrough3Points(current_Pt1,current_Pt2,current_Pt3,'w')
                self.PlottingCircleOrLineThrough3Points(P,current_Pt2,Q,'y')
                current_point = pg.ScatterPlotItem([current_Pt2.real],[current_Pt2.imag],pen='y')
                self.PlotWidgetIn_pageCP.addItem(current_point)
                k = (k+1)%nIterations
            #    QtCore.QTimer.singleShot(1000, update)
            #update()
            
    #        timer = QtCore.QTimer(self)
    #        timer.timeout.connect(update)
    #        timer.start(250)
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(update)
            self.timer.start(500)
                
            
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
#################################
#################################
#################################
### HYPERBOLIC PLANE
### UPPER HALF PLANE --- UHP


#    
#    def effectOf_UHPsigMouseClicked_Coords(self,ev): ## ev is the clicked point
#        global clicks
#        x = self.PlotWidgetIn_pageUHP.plotItem.vb.mapSceneToView(ev.scenePos()).x()
#        y = self.PlotWidgetIn_pageUHP.plotItem.vb.mapSceneToView(ev.scenePos()).y()
#        while len(clicks) < 3:  
#            clicks.append([x,y])
#        if len(clicks) == 3:  
#            del clicks[0]
#        print(clicks)
#        return clicks
#    
#    
        
    
        
            
    


        
            
        
            

        
    def passCoordsFromPlotWidgetIn_pageUHPto_checkBoxUHPGMShowGeodesicSegments(self,ev):
        if self.checkBoxUHPGMShowGeodesicSegments.isChecked() == True:
            global clicks
            x = self.PlotWidgetIn_pageUHP.plotItem.vb.mapSceneToView(ev.scenePos()).x()
            y = self.PlotWidgetIn_pageUHP.plotItem.vb.mapSceneToView(ev.scenePos()).y()
            while len(clicks) < 3:  
                clicks.append([x,y])
            if len(clicks) == 3:  
                del clicks[0]
            #print(clicks)
            if clicks[0] == clicks[1]:
                initialPoint = pg.ScatterPlotItem([clicks[0][0]],[clicks[0][1]],pen='r',brush='r')
                self.PlotWidgetIn_pageUHP.addItem(initialPoint)
            else:
                #print(clicks)
                finalPoint = pg.ScatterPlotItem([clicks[1][0]],[clicks[1][1]])
                self.PlotWidgetIn_pageUHP.addItem(finalPoint)
                P = clicks[0][0]+clicks[0][1]*(1j)
                Q = clicks[1][0]+clicks[1][1]*(1j)
                #print(P,Q)
                geodesicParametrization = UHP_Maths.UHPBasics().UHPGeodesicSegmentParamByArcLength(P,Q)[0]
                s = UHP_Maths.UHPBasics().UHPGeodesicSegmentParamByArcLength(P,Q)[1]
                numberOfSteps = 150
                t = numpy.linspace(0,s,numberOfSteps+1)
                k=0
                def update():
                    nonlocal k
                    if k < len(t)-1:
                        partialInterval = numpy.linspace(t[k],t[k+1],1000)
                        x_coord = geodesicParametrization(partialInterval).real
                        y_coord = geodesicParametrization(partialInterval).imag
                        self.PlotWidgetIn_pageUHP.plot(x_coord,y_coord,pen='w')   
                    k = (k+1)
                    if k == len(t)-1:
                        finalPointRed = pg.ScatterPlotItem([clicks[1][0]],[clicks[1][1]],pen='r',brush = 'r')
                        self.PlotWidgetIn_pageUHP.addItem(finalPointRed)
                    QtCore.QTimer.singleShot(1000*numpy.ceil(s)/numberOfSteps, update)
                update()
                print(numpy.ceil(s))
                
        #        timer = QtCore.QTimer(self)
        #        timer.timeout.connect(update)
        #        timer.start(250)
#                self.timer = QtCore.QTimer(self)
#                self.timer.timeout.connect(update)
#                self.timer.start(1)
                
        if self.checkBoxUHPGMShowGeodesicSegments.isChecked() == False:
            clicks.clear()
            print("as expected")
                
            #self.PlotWidgetIn_pageUHP.scene().sigMouseClicked.disconnect(onClick) 
        
        
    
#        #p = self.PlotWidgetIn_pageCP
#        print(self.checkBoxUHPGMShowGeodesicSegments.isChecked())
#        def fuck(sl):
#                #print(self.PlotWidgetIn_pageUHP.plotItem.vb.pos())
#                #nonlocal p
#                print('something')
#                #print(sl.scenePos().x())
#                #print(sl.pos().x())
#                P=self.PlotWidgetIn_pageUHP.plotItem.vb.mapSceneToView(sl.scenePos())
#                print(P.x())
#                print(P.y())
#                print(type(P.x()))
#                print(P.y())
#                #print (self.PlotWidgetIn_pageCP.plotItem.vb.mapSceneToView(sl))
#            
#        if self.checkBoxUHPGMShowGeodesicSegments.isChecked():
#            self.PlotWidgetIn_pageUHP.setEnabled(True)
#            
#
#
#    
#            self.PlotWidgetIn_pageUHP.scene().sigMouseClicked.connect(fuck)
#        else:
#            
##            def mouseMoved(evt):
##                pos = evt[0]  ## using signal proxy turns original arguments into a tuple
##                if self.PlotWidgetIn_pageUHP.sceneBoundingRect().contains(pos):
##                    mousePoint = self.PlotWidgetIn_pageUHP.plotItem.vb.mapSceneToView(pos)
##                    #index = int(mousePoint.x())
##                    #if index > 0 and index < self.CP_absolute_lim:
##                        #label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
##                    print(mousePoint.x())
##                    print(mousePoint.y())
##
##            self.proxy = pg.SignalProxy(self.PlotWidgetIn_pageUHP.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
#            
#            #self.PlotWidgetIn_pageUHP.scene().sigMouseMoved.connect(mouseMoved)
#            self.PlotWidgetIn_pageUHP.setEnabled(False)
#            #self.PlotWidgetIn_pageUHP.setEnabled(True)
#            print('yeah')
#            
#            
            
                
            
            
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