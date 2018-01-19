#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:07:25 2017

@author: daniellabardini
"""

import numpy






class numpyExtendedComplexPlane:
    
    def __init__(self):
        self.oo = 'oo' # This is the point at infinity in the extended complex plane 
    
    def extendedValue(self,complexOroo): ## PERSONAL NOTE: implement exception handling???
        if complexOroo == self.oo:
            value = complexOroo
        else:
            value = numpy.complex(complexOroo)
        return value


#############################

class MobiusAssocToMatrix:
    
    def __init__(self,complexa,complexb,complexc,complexd):
        self.a = numpy.complex(complexa)
        self.b = numpy.complex(complexb)
        self.c = numpy.complex(complexc)
        self.d = numpy.complex(complexd)
        self.theMatrix = numpy.matrix([[self.a,self.b],[self.c,self.d]])
        self.theDet = self.a*self.d - self.b*self.c
        if self.theDet == 0: ##### PERSONAL NOTE: implement a good exception handling
            raise ValueError
            
        self.oo = numpyExtendedComplexPlane().oo
        
        self.evaluation = numpy.vectorize(self.EvaluationAtConcretePoint)
    

    

        
    def EvaluationAtConcretePoint(self,z):
        z = numpyExtendedComplexPlane().extendedValue(z)
        if self.theDet == 0:# NECESSARY? PERSONAL NOTE: implement a good exception handling (somewhere, maybe here it wouldn't be necessary if it is well implemented)
            result = "This is not an invertible matrix."# NECESSARY? PERSONAL NOTE: implement a good exception handling (somewhere, maybe here wouldn't be necessary)
        elif z != self.oo and self.c*z + self.d != 0:
            result = (self.a*z + self.b)/(self.c*z + self.d)
        elif z != self.oo and self.c*z + self.d == 0:
            result = self.oo
        elif z == self.oo and self.c != 0:
            result = self.a / self.c
        elif z == self.oo and self.c == 0:
            result = self.oo
        return result
    
    def Mob_trans_iterable(self,z,n): 
        SingleIteration = self.EvaluationAtConcretePoint
        CurrentPoint = z
        Orbit = [z]
        for i in range(1,n,1):
            Orbit.append(SingleIteration(CurrentPoint))
            CurrentPoint = SingleIteration(CurrentPoint)
        return Orbit
    
    
            
        
    

    

    
        