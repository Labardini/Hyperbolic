#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 07:54:19 2018

@author: daniellabardini
"""

import numpy



from exception_handling import myInputError
from Maths.CP_Maths import extended_complex_plane_CP


#### SOME FUNCTIONS IMPORTED FROM Maths.CP_Maths.extended_complex_plane_CP
oo = extended_complex_plane_CP.numpyExtendedComplexPlane().oo
isooInArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().isooInArgs
isooInList = extended_complex_plane_CP.numpyExtendedComplexPlane().isooInList
extendedValue = extended_complex_plane_CP.numpyExtendedComplexPlane().extendedValue
areAllDistinctArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().areAllDistinctArgs
areAllDistinctList = extended_complex_plane_CP.numpyExtendedComplexPlane().areAllDistinctList
removeooFromArgs = extended_complex_plane_CP.numpyExtendedComplexPlane().removeooFromArgs
removeooFromList = extended_complex_plane_CP.numpyExtendedComplexPlane().removeooFromList
e_circumcenter_and_radius = extended_complex_plane_CP.numpyExtendedComplexPlane().e_circumcenter_and_radius
areCollinear = extended_complex_plane_CP.numpyExtendedComplexPlane().areCollinear
myNumpyCosecant = extended_complex_plane_CP.numpyExtendedComplexPlane().myNumpyCosecant
myNumpyCotangent = extended_complex_plane_CP.numpyExtendedComplexPlane().myNumpyCotangent
####



        
class UHPBasics:
    
    def __init__(self):
        pass
    
    def isInUHP(self,complexP):
        P = extendedValue(complexP)
        if P != oo and P.imag > 0:
            answer = True
        else:
            answer = False
        return answer
    
    def isIdealPoint(self,complexP):
        P = extendedValue(complexP)
        if P == oo or P.imag == 0:
            answer = True
        else:
            answer = False
        return answer
    
    def isInUHPBar(self,complexP):
        if self.isInUHP(complexP) == True or self.isIdealPoint(complexP) == True:
            answer = True
        else:
            answer = False
        return answer
        
    def areVertAlignedInUHP(self,hPointP,hPointQ):
        P, Q = extendedValue(hPointP), extendedValue(hPointQ)
        if self.isInUHP(P) == True and self.isInUHP(Q) == True and P != Q:
            if P.real == Q.real:
                answer = True
            else:
                answer = False
            return answer
        else:
            raise myInputError(print(P)+','+print(Q),"Both points must belong to the UHP and they must be distinct")

    def UHPNorm(self,point,vector): # IN THE UPPER HALF PLANE
        P = numpy.complex(point)
        V = numpy.complex(vector)
        result =   numpy.sqrt( (numpy.real(V))**2 + (numpy.imag(V))**2 )  / numpy.imag(P)
        return result

    def UHPDist(self,pointP,pointQ): # UPPER HALF PLANE
        P = numpy.complex(pointP)
        Q = numpy.complex(pointQ)
        P1 = numpy.real(P)
        P2 = numpy.imag(P)
        Q1 = numpy.real(Q)
        Q2 = numpy.imag(Q)
        dist_expression = numpy.arccosh(  1 + ( ( (Q1-P1)**2 + (Q2-P2)**2 ) / (2*P2*Q2) )  )
        return dist_expression
    
            
    def eCenterAndRadiusNonVertGeodesicThroughPAndQ(self,hpointP,hpointQ):
        P, Q = extendedValue(hpointP), extendedValue(hpointQ)
        if self.areVertAlignedInUHP(P,Q) == False:
            normal = (Q-P).imag + (P-Q).real*(1j)
            midpoint = (P+Q)/2
            eCenter = midpoint + (-(midpoint.imag)/(normal.imag))*(normal)
            eRadius = numpy.absolute(P-eCenter)
            return [eCenter,eRadius]
        else:
            raise myInputError(str(P)+','+str(Q),"The points must be distinct, belong to the UHP, and not be vertically alligned")
            
    def eCenterAndRadiusH_Circle(self,hcenter,hradius): # IN THE UPPER HALF PLANE
        Hcenter = numpy.complex(hcenter)
        Hradius = numpy.real(hradius)            
        x0 = numpy.real(Hcenter)
        x1 = numpy.imag(Hcenter)
        euclidean_center_x = x0
        euclidean_center_y = x1*(numpy.cosh(Hradius))
        #euclidean_center = Point(euclidean_center_x, euclidean_center_y)
        euclidean_radius = x1*(numpy.sinh(Hradius))
        return [ numpy.complex(euclidean_center_x + euclidean_center_y*(1j)), numpy.real(euclidean_radius)]













#### PERSONAL NOTE: Check the next functions carefully

    def UHPGeodesicSegment_rcostrsint(self,startpoint,endpoint):
        A = extendedValue(startpoint)
        B = extendedValue(endpoint)
        if self.areVertAlignedInUHP(A,B) == False:
            X = self.eCenterAndRadiusNonVertGeodesicThroughPAndQ(A,B)
            translated_startpoint = A - (X[0])
            translated_endpoint = B - (X[0])
            interval_for_t = [ numpy.angle(translated_startpoint), numpy.angle(translated_endpoint) ]
        else:
            interval_for_t = [ numpy.imag(A), numpy.imag(B) ]
        left_to_right_interval_for_t = [0, numpy.abs(interval_for_t[1]-interval_for_t[0])]
        def parametrized_curve(time_t):
            Time_t = numpy.real(time_t)
            if self.areVertAlignedInUHP(A,B) == False:
                parametrization = X[0] + (X[1]*(numpy.cos(Time_t) + (numpy.sin(Time_t))*(1j)))
            else:
                parametrization = numpy.real(A) + (Time_t*(1j))
            return parametrization
        def reoriented_parametrization(increasing_t):
            if interval_for_t[1] - interval_for_t[0] >= 0:
                result = parametrized_curve(increasing_t + interval_for_t[0])
            if interval_for_t[1] - interval_for_t[0] < 0:
                result = parametrized_curve(-increasing_t + interval_for_t[0])
            return result
        return [reoriented_parametrization, left_to_right_interval_for_t]
    
#    self.numeric_upper_geodesic_rcosrsin = Numeric_Upper_Geodesic_Segment_rcosrsin_Parametrization
                

    def UHPGeodesicSegmentParamByArcLength(self,startpoint,endpoint): # ASSUMES THE FORMULAS FOR s IN Symb_Upper_Arc_Length_for_Geodesic_Segment
    #ARE CORRECT
    # I APOLOGIZE FOR SUCH A LONG NAME...
        A = extendedValue(startpoint)
        B = extendedValue(endpoint)
        if self.areVertAlignedInUHP(A,B) == False:
            X = self.eCenterAndRadiusNonVertGeodesicThroughPAndQ(A,B)
            translated_startpoint = A - (X[0])
            translated_endpoint = B - (X[0])
            arg_trans_startpoint = numpy.angle(translated_startpoint)
            arg_trans_endpoint = numpy.angle(translated_endpoint)
            interval_for_s = numpy.log( ( myNumpyCosecant(arg_trans_endpoint) - myNumpyCotangent(arg_trans_endpoint) ) / ( myNumpyCosecant(arg_trans_startpoint) - myNumpyCotangent(arg_trans_startpoint) ) )#self.UHPDist(A,B)
        else:
            interval_for_s = numpy.log(numpy.imag(B) / numpy.imag(A))
        left_to_right_interval_for_s = numpy.abs(interval_for_s)
        def parametrized_curve(time_s):
            ARC_LENGTH_PARAMETER = numpy.real(time_s)
            if self.areVertAlignedInUHP(A,B) == False:
                e_center_of_geodesic = X[0]
                e_radius_of_geodesic = X[1]
                t  = 2 * ( numpy.arctan( (numpy.tan( arg_trans_startpoint / 2 )) * numpy.exp(ARC_LENGTH_PARAMETER) ) )
                parametrization = e_center_of_geodesic + e_radius_of_geodesic*( numpy.cos(t) + numpy.sin(t)*(1j) )
            else:
                t = numpy.imag(A)*( numpy.exp(ARC_LENGTH_PARAMETER) )
                parametrization = numpy.real(A) + t*(1j)
            return parametrization
        def reoriented_parametrization(increasing_s):
            if interval_for_s >= 0:
                result = parametrized_curve(increasing_s)
            if interval_for_s < 0:
                result = parametrized_curve(-increasing_s)
            return result
        return [reoriented_parametrization, left_to_right_interval_for_s]

        
#    self.numeric_upper_geodesic_param_by_arc_length = Numeric_Upper_Geodesic_Segment_Parameterized_by_Arc_Length


#
#        def Symb_Upper_Arc_Length_for_Geodesic_Segment(startpoint,endpoint): # GEODESIC IS IMPLICITLY SUPPOSED TO BE ORIGINALLY PARAMETERIZED AS r*(cos(t)+sin(t)*I) OR x + t*I
#            def Expression_when_Geodesic_is_E_Circle_Centered_at_Origin(specialstartpoint):
#                rotation_angle = (sympy.pi/2) - sympy.arg(specialstartpoint) # ANGLE NEEDED TO ROTATE THE specialstarpoint TO pi/2
#                time = sympy.Symbol("t") + rotation_angle
#                s = ( sympy.ln( sympy.tan(time/2) ) )
#                return s
#            if sympy.re(startpoint) != sympy.re(endpoint):
#                import_E_Data = E_Data()
#                X = import_E_Data.e_center_radius_non_vert_geodesic(startpoint,endpoint)[0]
#                translated_startpoint = startpoint -X
#                translated_endpoint = endpoint - X
#                s = Expression_when_Geodesic_is_E_Circle_Centered_at_Origin(translated_startpoint)
#                interval_for_t = [sympy.arg(translated_startpoint),sympy.arg(translated_endpoint)] ### CHECK THIS, I DEFINED THIS INTERVAL TOO QUICKLY, WITHOUT THINKING TOO MUCH
#            else:
#                time = sympy.sign(sympy.im(endpoint-startpoint)) * sympy.Symbol("t")
#                s = sympy.ln( time/sympy.im(startpoint) )
#                interval_for_t = [sympy.im(startpoint),sympy.im(endpoint)]
#            return [s,interval_for_t] # GIVES s == zoo IF endpoint == startpoint. SHOULD I SET IT TO 0 IN THIS CASE????
#







    
class UHPGeodesicMotion:
    
    def __init__(self):
        pass
    
class UHPCircularMotion:
    
    def __init__(self):
        pass
    
class UHPIsometries:
    
    def __init__(self):
        pass

    
    
    