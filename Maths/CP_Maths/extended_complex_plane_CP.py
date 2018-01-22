#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:42:40 2018

@author: daniellabardini
"""

import numpy


class coordsOfComplex:
    
    def __init__(self):
        
        self.coords = numpy.vectorize(self.coordsFunction)
    
    def coordsFunction(self,complexnumber):
        z = numpy.complex(complexnumber)
        return (z.real,z.imag)
    
    
class numpyExtendedComplexPlane:
    
    def __init__(self):
        self.oo = 'oo' # This is the point at infinity in the extended complex plane 
    
    def extendedValue(self,complexOroo): ## PERSONAL NOTE: implement exception handling???
        if complexOroo == self.oo:
            value = complexOroo
        else:
            value = numpy.complex(complexOroo)
        return value