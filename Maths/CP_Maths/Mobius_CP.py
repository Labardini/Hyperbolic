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
    
    def Mob_trans_iterable(self,z,n): ### PERSONAL NOTE: treat with nth power of matrix instead?
        SingleIteration = self.EvaluationAtConcretePoint
        CurrentPoint = z
        Orbit = [z]
        for i in range(1,n,1):
            Orbit.append(SingleIteration(CurrentPoint))
            CurrentPoint = SingleIteration(CurrentPoint)
        return Orbit
    
    def fixedPoints(self):
       if self.theDet == 0:# NECESSARY? Perhaps it wouldn't be necessary if a good exception handling were implemented
           fixed_point_set = "This is not an invertible matrix."# NECESSARY?
       elif self.c == 0 and self.a == self.d and self.b == 0:
           fixed_point_set = "This Mobius transformation is the identity. It fixes every point in the extended complex plane."
       elif self.c == 0 and self.a == self.d and self.b != 0:
           fixed_point_set = [self.oo]
       elif self.c == 0 and self.a != self.d:
           z1 =  self.b / (self.d-self.a) 
           fixed_point_set = [z1, self.oo]
       elif self.c != 0:
           coeffOfQuadraticPol = [self.c,self.d-self.a,-self.b]
           fixed_point_set = numpy.roots(coeffOfQuadraticPol)
           #x = sympy.Symbol('x')
           #quadratic_pol = (self.c*(x**2))+((self.d-self.a)*x)-self.b
           #fixed_point_set = sympy.solve(quadratic_pol,x)
       if len(fixed_point_set) == 1:
           fixed_point_set = [fixed_point_set[0],fixed_point_set[0]]
       return fixed_point_set
        
    def MobiusTrace(self):
        if self.theDet == 0: # NECESSARY? Perhaps it wouldn't be necessary if a good exception handling were implemented
            traza = "This is not an invertible matrix."
        else:
            traza0 = (self.a+self.d) / (numpy.sqrt(self.theDet)) 
            traza1 = -(traza0)
            traza = [ traza0 , traza1 ]
        return traza
    
    def isParEllHypLox(self):
        if self.theDet == 0:
            TheTypeIs = "This is not an invertible matrix."
        else:
            S = self.fixedPoints
            T = self.MobiusTrace
            if self.c == 0 and self.a == self.d and self.b == 0:
                TheTypeIs = "This Mobius transformation is the identity. It fixes every point in the Riemann sphere."
            elif S[0] == S[1]:
                TheTypeIs = 'This Mobius transformation is PARABOLIC.'
            elif numpy.imag(T[0]) ==0 and numpy.absolute(numpy.real(T[0]))<2:
                TheTypeIs = 'This Mobius transformation is ELLIPTIC.'
            elif numpy.imag(T[0]) == 0 and numpy.absolute(numpy.real(T[0]))>2:
                TheTypeIs = 'This Mobius transformation is HYPERBOLIC.'
            elif numpy.imag(T[0]) !=0:
                TheTypeIs = 'This Mobius transformation is LOXODROMIC.'
        return TheTypeIs

        
    


    

    
        