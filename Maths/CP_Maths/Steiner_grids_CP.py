#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:07:25 2017

@author: daniellabardini
"""

import numpy
import sympy

from exception_handling import myInputError

from Maths.CP_Maths import extended_complex_plane_CP

#### SOME FUNCTIONS IMPORTED FROM extended_complex_plane_CP
oo = extended_complex_plane_CP.numpyExtendedComplexPlane().oo
coords=extended_complex_plane_CP.numpyExtendedComplexPlane().coords
isooInArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().isooInArgs
isooInList = extended_complex_plane_CP.numpyExtendedComplexPlane().isooInList
extendedValue = extended_complex_plane_CP.numpyExtendedComplexPlane().extendedValue
areAllDistinctArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().areAllDistinctArgs
areAllDistinctList = extended_complex_plane_CP.numpyExtendedComplexPlane().areAllDistinctList
removeooFromArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().removeooFromArgs
removeooFromList = extended_complex_plane_CP.numpyExtendedComplexPlane().removeooFromList
####



class commonCircles:
    
    def __init__(self):
        pass
        
    
    
    def pointsOnMediatrix(self,complexnumberP, complexnumberQ, n):
        P = extendedValue(complexnumberP)
        Q = extendedValue(complexnumberQ)
        try:
            areAllDistinctArgs(P,Q)
        except myInputError:
            raise myInputError(str(P)+","+str(Q),"The points must be distinct")
        if isooInArgs(P,Q) == True:
            raise myInputError(str(P)+","+str(Q),"Both points must be finite")
        else:
            midPoint = (P+Q)/2
            halfDifference = (P-Q)/2
            a = numpy.real(halfDifference)
            b = numpy.imag(halfDifference)
            orthogonal = numpy.complex(b + (-a)*(1j))
            numpyLeftInterval = numpy.arange(-n,0,1)#(-(n-1)/2,0,1)
            numpyRightInterval = numpy.arange(1,1+n,1)#(1,1+(n-1)/2,1)
            numpyInterval = numpy.linspace(-n,n,n)#numpy.union1d(numpyLeftInterval,numpyRightInterval)
            return midPoint + numpyInterval*orthogonal
         
     
    def circlesThroughPFunction(self,complexnumberP):
        P = extendedValue(complexnumberP)
        if P == oo:
            raise myInputError(str(P),"The point must be finite")
        else:
            def theFunction(complexnumberR): ## Makes R the center of circle passing through P.
                R = numpy.complex(complexnumberR)
                center = [numpy.real(R),numpy.imag(R)]
                radius = numpy.absolute(R-P)
                return [center,radius]
            vectorized = numpy.vectorize(theFunction)
            return vectorized

    def pointsAroundP(self,complexnumberP,n):
        P = extendedValue(complexnumberP)
        if P == oo:
            raise myInputError(str(P),"The point must be finite")
        else:
            theta = numpy.linspace(0,2*numpy.pi,n)
            return P + numpy.cos(theta) + ((numpy.sin(theta))*(1j))
        
    def linesThroughPFunction(self,complexnumberP): ##PERSONAL NOTE: Should I try to curry the functions that have functions as outputs?
        P = extendedValue(complexnumberP)
        if P == oo:
            raise myInputError(str(P),"The point must be finite")
        else:
            def theFunction(complexR):
                R = numpy.complex(complexR)
                return [[R.real,R.imag],P]
            vectorized = numpy.vectorize(theFunction)
            return vectorized
        
        
            
            
    def common_circlesFunction(self,complexnumberP,complexnumberQ,n):
        P = extendedValue(complexnumberP)
        Q = extendedValue(complexnumberQ)
        try:
            areAllDistinctArgs(P,Q)
        except myInputError:
            raise myInputError(str(P)+","+str(Q),"The points must be distinct")
        if isooInArgs(P,Q) == True:
            finitePoint = (removeooFromList([P,Q]))[0]
            theFunction = self.linesThroughPFunction(finitePoint)
            pointsAroundFinitePoint = self.pointsAroundP(finitePoint,n)
            return theFunction(pointsAroundFinitePoint)
        else:
            theFunction = self.circlesThroughPFunction(complexnumberP)
            points_on_mediatrix = self.pointsOnMediatrix(complexnumberP, complexnumberQ, n)
            return theFunction(points_on_mediatrix)
        
    
    
class Apollonius:
    
    def __init__(self):
        pass
    
    def centerAndRadiusApolloniusCircle(self,complexnumberP,complexnumberQ):
        P = numpy.complex(complexnumberP)
        Q = numpy.complex(complexnumberQ)
        distance = numpy.absolute(P-Q)
        def theFunction(k): # k is supposed to be an integer greater than 0 and smaller than an n to be given as an input below
            x = (k*distance) / (1+k)
            y = (k*distance) / (k-1)
            X = P + (x/distance)*(Q-P)
            Y = P + (y/distance)*(Q-P)
            center = (X+Y)/2
            radius = (k*distance) / (  numpy.absolute(1-k**2)  )
            return [[numpy.real(center),numpy.imag(center)],radius]
        vectorized = numpy.vectorize(theFunction)
        return vectorized

    
    def Apollonius_e_circles1(self,complexnumberP,complexnumberQ,n):#(beta1,beta2,number):
        theFunction = self.centerAndRadiusApolloniusCircle(complexnumberP,complexnumberQ)
        numpyInterval = numpy.arange(1,n,1)
        numpyFirstInterval = numpyInterval / n
        return theFunction(numpyFirstInterval)
    
    def Apollonius_e_circles2(self,complexnumberP,complexnumberQ,n):#(beta1,beta2,number):
        theFunction = self.centerAndRadiusApolloniusCircle(complexnumberP,complexnumberQ)
        numpyInterval = numpy.arange(1,n,1)
        numpySecondInterval = n / (n-numpyInterval)
        return theFunction(numpySecondInterval)
        
        

        
        

