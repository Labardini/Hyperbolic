#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:07:25 2017

@author: daniellabardini
"""

import numpy
import sympy
from sympy import I




class commonCircles:
    
    def __init__(self):
        pass
    
    def e_circumcenter(self,complexnumberP,complexnumberQ,complexnumberR):
        P = numpy.complex(complexnumberP) 
        Q = numpy.complex(complexnumberQ)
        R = numpy.complex(complexnumberR) 
        realOfP = numpy.real(P)
        imOfP = numpy.imag(P)
        PointP = sympy.geometry.Point(realOfP,imOfP)
        realOfQ = numpy.real(Q)
        imOfQ = numpy.imag(Q)
        PointQ = sympy.geometry.Point(realOfQ,imOfQ)
        realOfR = numpy.real(R)
        imOfR = numpy.imag(R)
        PointR = sympy.geometry.Point(realOfR,imOfR)
        circ = sympy.geometry.Circle(PointP,PointQ,PointR)
        cent = circ.center
        return (cent.x,cent.y)
    

    def e_circumradius(self,complexnumberP,complexnumberQ,complexnumberR):
        P = numpy.complex(complexnumberP) 
        Q = numpy.complex(complexnumberQ)
        R = numpy.complex(complexnumberR) 
        realOfP = numpy.real(P)
        imOfP = numpy.imag(P)
        PointP = sympy.geometry.Point(realOfP,imOfP)
        realOfQ = numpy.real(Q)
        imOfQ = numpy.imag(Q)
        PointQ = sympy.geometry.Point(realOfQ,imOfQ)
        realOfR = numpy.real(R)
        imOfR = numpy.imag(R)
        PointR = sympy.geometry.Point(realOfR,imOfR)
        circ = sympy.geometry.Circle(PointP,PointQ,PointR)
        rad = circ.hradius
        return rad
    
    
    def pointsOnMediatrix(self,complexnumberP, complexnumberQ, n):
        P = numpy.complex(complexnumberP)
        Q = numpy.complex(complexnumberQ)
        midPoint = (P+Q)/2
        halfDifference = (P-Q)/2
        a = numpy.real(halfDifference)
        b = numpy.imag(halfDifference)
        orthogonal = numpy.complex(b + (-a)*(1j))
        numpyLeftInterval = numpy.arange(-(n-1)/2,0,1)
        numpyRightInterval = numpy.arange(1,1+(n-1)/2,1)
        numpyInterval = numpy.union1d(numpyLeftInterval,numpyRightInterval)
        return midPoint + numpyInterval*orthogonal
     
    def commonCirclesFunction(self,complexnumberP,complexnumberQ):
        def theFunction(complexnumberR):
            return [self.e_circumcenter(complexnumberP,complexnumberQ,complexnumberR),self.e_circumradius(complexnumberP,complexnumberQ,complexnumberR)]
        vectorized = numpy.vectorize(theFunction)
        return vectorized
            
    def common_circles(self,complexnumberP,complexnumberQ,n):
        theFunction = self.commonCirclesFunction(complexnumberP,complexnumberQ)
        points_on_mediatrix = self.pointsOnMediatrix(complexnumberP, complexnumberQ, n)
        print(points_on_mediatrix)
        return theFunction(points_on_mediatrix)
#        mylist =[]
#        for R in points_on_mediatrix:
#            mylist.append(theFunction(R))  
#        return mylist
    

        
        
    
    
    

