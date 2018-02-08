#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:42:40 2018

@author: daniellabardini
"""

import numpy
import sympy


#from exception_handling import Maybe
from exception_handling import myInputError



j = 1j #### PERSONAL NOTE: this is intended to avoid the exception "name 'j' is not defined". Should I find a more elegant way????  
    
class numpyExtendedComplexPlane:
    
    def __init__(self):
        self.oo = 'oo' # This is the point at infinity in the extended complex plane
        self.coords = numpy.vectorize(self.coordsFunction)

    def isooInArgs(self,*args): # This function decides whether the point at infinity is in the arguments passed
        if self.oo in args:
            answer = True
        else:
            answer = False
        return answer
    
    def isooInList(self,List):
        if self.oo in List:
            answer = True
        else:
            answer = False
        return answer
    
    def removeooFromArgs(self,*args):
        return [x for x in args if x != 'oo']
    
    def removeooFromList(self,List):
        return [x for x in List if x != 'oo']
    
    def coordsFunction(self,complexnumber):
        z = numpy.complex(complexnumber)
        return (z.real,z.imag)        
    
    def extendedValue(self,complexOroo): ## PERSONAL NOTE: implement exception handling???
        if complexOroo != self.oo:
            value = numpy.complex(complexOroo)
        else:
            value = self.oo
        return value
    
    def areAllDistinctArgs(self,*args): #### PERSONAL NOTE: Should this function be in my custom exceptions module???? It may look as the definition of an exception....
        length = len(args)
        for t in range(0,length-1): ### PERSONAL NOTE: is there a more efficient way of doing this???
            for s in range(t+1,length):
                if args[t] == args[s]:
                    raise myInputError("Positions "+str(t)+" and "+str(s)+": "+ str(args[t])+","+str(args[s]),
                                     "Arguments are not all pairwise distinct")
        return True
    
    def areAllDistinctList(self,List):
        length = len(List)
        for t in range(0,length-1): ### PERSONAL NOTE: is there a more efficient way of doing this???
            for s in range(t+1,length):
                if List[t] == List[s]:
                    raise myInputError("Positions "+str(t)+" and "+str(s)+": "+ str(List[t])+","+str(List[s]),
                                     "Arguments are not all pairwise distinct")
        return True
        
    
                
    def areCollinear(self,complexP,complexQ,complexR):
        P, Q, R = self.extendedValue(complexP), self.extendedValue(complexQ), self.extendedValue(complexR)
        try:
            self.areAllDistinctArgs(P,Q,R)
        except myInputError:
            raise myInputError(str(P)+","+str(Q)+","+str(R),
                             "To decide collinearity/non-collinearity, the three points must be distinct")
        if self.oo in [P,Q,R]:
            answer = True
        elif ((R-P)/(Q-P)).imag == 0:
            answer = True
        elif ((R-P)/(Q-P)).imag != 0:
            answer = False
        return answer
    
    def typeOfCircleInExtendedPlane(self,complexP,complexQ,complexR):
        #### If the points are not all distinct, an exception is raised
        #### by areCollinear and areAllDistinct
        if self.areCollinear(complexP,complexQ,complexR) == False:
            theType = "circle"
        else:
            theType = "line"
        return theType
    
    def e_circumcenter_and_radius(self,complexP,complexQ,complexR):
        #### If the points are not all distinct, an exception is raised
        #### by areCollinear and areAllDistinct
        if self.typeOfCircleInExtendedPlane(complexP,complexQ,complexR) == "circle":
            P = numpy.complex(complexP) 
            Q = numpy.complex(complexQ)
            R = numpy.complex(complexR) 
            realOfP = numpy.real(P)
            imOfP = numpy.imag(P)
            PointP = sympy.geometry.Point(realOfP,imOfP)
            realOfQ = numpy.real(Q)
            imOfQ = numpy.imag(Q)
            PointQ = sympy.geometry.Point(realOfQ,imOfQ)
            realOfR = numpy.real(R)
            imOfR = numpy.imag(R)
            PointR = sympy.geometry.Point(realOfR,imOfR)
            cent = sympy.geometry.Circle(PointP,PointQ,PointR).center
            rad = sympy.geometry.Circle(PointP,PointQ,PointR).hradius
        else:
            raise myInputError(str(complexP)+","+str(complexQ)+","+str(complexR),"These points are collinear")
        return [[cent.x,cent.y],rad]
    
    