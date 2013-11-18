########################################################################
#
# Copyright (C) 2013 Steven Osborne.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
####################################################################### 
#
# A is a list of lists of coefficients
# b is a list of problem constraints
# c is a list of objective coefficients
# integer is a Boolean. If True, performs integer programming,
#    if False, performs linear programming (default False)
# canonical is a Boolean. If True, sets up the LP/IP 
#    min (c^T)x 
#    s.t. Ax >= b
#    x >= 0. 
#    If false, user must supply the following:
#        x_list - a list of integers that dictate the following:
#            x_list[i] =  1      => variable x[i] >= 0
#            x_list[i] =  0      => variable x[i]  = 0
#            x_list[i] = -1      => variable x[i] >= 0
#            x_list[i] != -1,0,1 => variable x[i] free
#        b_list - a list of integers that dictate the following:
#            b_list[i] =  1      => constraint i >= b[i]
#            b_list[i] =  0      => constraint i  = b[i]
#            b_list[i] = -1      => constraint i <= b[i]
#            b_list[i] != -1,0,1 => constraint i free
# dual is a Boolean. If true, returns both the primal LP and the 
#    dual LP. If false, returns only the primal LP

def form_lp(A,b,c,integer=False,max=False,canonical=True,x_list=[],b_list=[], dual=False):
    
    (m,n) = (len(A),len(A[0]))
    if canonical:
        b_list=[1]*m
        x_list=[1]*n
        max = False
    if max == False:
        lp = MixedIntegerLinearProgram(maximization=False)
    else:
        lp = MixedIntegerLinearProgram()
    x = lp.new_variable()
    if integer:
        for i in range(0,n):
            lp.set_integer(x[i])
    else:
        for i in range(0,n):
            lp.set_real(x[i])
    for i in range(0,n):
        if x_list[i] == 1:
            lp.set_min(x[i],0)
        elif x_list[i] == 0:
            lp.set_min(x[i],0)
            lp.set_max(x[i],0)
        elif x_list[i] == -1:
            lp.set_max(x[i],0)
        else:
            lp.set_min(x[i],None)       
    f = c[0]*x[0]
    for i in range(1,n):
        f = f + c[i]*x[i]
    lp.set_objective(f)
    for i in range(0,m):
        g = A[i][0]*x[0]
        for j in range(1,n):
            g = g + A[i][j]*x[j]
        if b_list[i] == 0:    
            lp.add_constraint( g == b[i] )
        elif b_list[i] == 1:
            lp.add_constraint( g >= b[i] )
        elif b_list[i] == -1:
            lp.add_constraint( g <= b[i] )
    if not dual:
        return lp,x
    else:
        import numpy as np 
        AT = np.matrix(A).transpose().tolist()
        if max == False:
            dual_b = [0]*n
            for i in range(0,n):
                if x_list[i] == 1:
                    dual_b[i] = -1
                elif x_list[i] == -1:
                    dual_b[i] = 1
                elif x_list[i] == 0:
                    dual_b[i] = 2      
            dual_x = [0]*m
            for i in range(0,m):
                if b_list[i] == 1:
                    dual_x[i] = 1
                elif b_list[i] == 0:
                    dual_x[i] = 2
                elif b_list[i] == -1:
                    dual_x[i] = -1
                else:
                    dual_x[i] = 2 
            (dual_lp,y) = \
                form_lp(AT,c,b,max=True,integer=integer,canonical=False,x_list=dual_x,b_list=dual_b)
            return lp,x,dual_lp,y
        else:
            dual_b = [0]*n
            for i in range(0,n):
                if x_list[i] == 1:
                    dual_b[i] = 1
                elif x_list[i] == -1:
                    dual_b[i] = -1
                elif x_list[i] == 0:
                    dual_b[i] = 2      
            dual_x = [0]*m
            for i in range(0,m):
                if b_list[i] == 1:
                    dual_x[i] = -1
                elif b_list[i] == 0:
                    dual_x[i] = 2
                elif b_list[i] == -1:
                    dual_x[i] = 1
                else:
                    dual_x[i] = 2
            (dual_lp,y) = \
                form_lp(AT,c,b,integer=integer,canonical=False,x_list=dual_x,b_list=dual_b)
            return lp,x,dual_lp,y