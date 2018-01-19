#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:07:25 2017

@author: daniellabardini
"""

import numpy


class coordsOfComplex:
    
    def __init__(self):
        pass
    
        self.coords = numpy.vectorize(self.coordsFunction)
    
    def coordsFunction(self,complexnumber):
        z = numpy.complex(complexnumber)
        return (numpy.real(z),numpy.imag(z))


class commonCircles:
    
    def __init__(self):
        pass
    
#    def e_circumcenter(self,complexnumberP,complexnumberQ,complexnumberR):
#        P = numpy.complex(complexnumberP) 
#        Q = numpy.complex(complexnumberQ)
#        R = numpy.complex(complexnumberR) 
#        realOfP = numpy.real(P)
#        imOfP = numpy.imag(P)
#        PointP = sympy.geometry.Point(realOfP,imOfP)
#        realOfQ = numpy.real(Q)
#        imOfQ = numpy.imag(Q)
#        PointQ = sympy.geometry.Point(realOfQ,imOfQ)
#        realOfR = numpy.real(R)
#        imOfR = numpy.imag(R)
#        PointR = sympy.geometry.Point(realOfR,imOfR)
#        circ = sympy.geometry.Circle(PointP,PointQ,PointR)
#        cent = circ.center
#        return (cent.x,cent.y)
#    
#
#    def e_circumradius(self,complexnumberP,complexnumberQ,complexnumberR):
#        P = numpy.complex(complexnumberP) 
#        Q = numpy.complex(complexnumberQ)
#        R = numpy.complex(complexnumberR) 
#        realOfP = numpy.real(P)
#        imOfP = numpy.imag(P)
#        PointP = sympy.geometry.Point(realOfP,imOfP)
#        realOfQ = numpy.real(Q)
#        imOfQ = numpy.imag(Q)
#        PointQ = sympy.geometry.Point(realOfQ,imOfQ)
#        realOfR = numpy.real(R)
#        imOfR = numpy.imag(R)
#        PointR = sympy.geometry.Point(realOfR,imOfR)
#        circ = sympy.geometry.Circle(PointP,PointQ,PointR)
#        rad = circ.hradius
#        return rad
    
    
    def pointsOnMediatrix(self,complexnumberP, complexnumberQ, n):
        P = numpy.complex(complexnumberP)
        Q = numpy.complex(complexnumberQ)
        midPoint = (P+Q)/2
        halfDifference = (P-Q)/2
        a = numpy.real(halfDifference)
        b = numpy.imag(halfDifference)
        orthogonal = numpy.complex(b + (-a)*(1j))
        numpyLeftInterval = numpy.arange(-n,0,1)#(-(n-1)/2,0,1)
        numpyRightInterval = numpy.arange(1,1+n,1)#(1,1+(n-1)/2,1)
        numpyInterval = numpy.linspace(-n,n,n)#numpy.union1d(numpyLeftInterval,numpyRightInterval)
        return midPoint + numpyInterval*orthogonal
     
    def commonCirclesFunction(self,complexnumberP,complexnumberQ):
        P = numpy.complex(complexnumberP)
        #Q = numpy.complex(complexnumberQ)
        def theFunction(complexnumberR):
            R = numpy.complex(complexnumberR)
            center = (numpy.real(R),numpy.imag(R))
            radius = numpy.absolute(R-P)
            return [center,radius]
        vectorized = numpy.vectorize(theFunction)
        return vectorized
            
    def common_circles(self,complexnumberP,complexnumberQ,n):
        theFunction = self.commonCirclesFunction(complexnumberP,complexnumberQ)
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
            return [(numpy.real(center),numpy.imag(center)),radius]
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
        
        

        
        

