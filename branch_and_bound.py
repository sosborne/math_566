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

load('https://raw.github.com/sosborne/math_566/master/osborne_lp.py')

def gen_leaves(A,b,b_list,lp_vars):
    a_dict={}
    n=len(lp_vars.keys())
    for i in range(0,n):
        if not lp_vars[i].is_integer():
            val = RR(lp_vars[i])
            l=val.floor();r=val.ceil()
            b1=deepcopy(b);b2=deepcopy(b)
            b1.append(l);b2.append(r)
            b1_list=deepcopy(b_list);b2_list=deepcopy(b_list)
            b1_list.append(-1);b2_list.append(1)
            A1=deepcopy(A);row=[]
            for j in range(0,n):
                if i==j:
                    row.append(1)
                else:
                    row.append(0)
            A1.append(row)
            a_dict[i]=(A1,b1,b1_list,b2,b2_list)
    return a_dict

def check_integral(a_dict):
    inte = True
    for i in a_dict.values():
        if int(i)!=i:
            inte=False
            break
    return inte

# A is a list of lists of coefficients
# b is a list of problem constraints
# c is a list of objective coefficients
# X_list - a list of integers that dictate the following:
#   X_list[i] =  1      => variable x[i] >= 0
#   X_list[i] =  0      => variable x[i]  = 0
#   X_list[i] = -1      => variable x[i] >= 0
#   X_list[i] != -1,0,1 => variable x[i] free
# B_list - a list of integers that dictate the following:
#   B_list[i] =  1      => constraint i >= b[i]
#   B_list[i] =  0      => constraint i  = b[i]
#   B_list[i] = -1      => constraint i <= b[i]
#   B_list[i] != -1,0,1 => constraint i free

def branch_and_bound(A,b,c,X_list,B_list):
    verts=set([0]);searched=set([])
    counter = 0; opt = infinity
    (lp,x)=form_lp(A,b,c,canonical=False,x_list=X_list,b_list=B_list)
    tree = {0:(RR(lp.solve()),False,A,b,B_list,lp.get_values(x))}
    while verts!=searched:
        for v in verts.difference(searched):
            if tree[v][1]:
                opt = min(opt,tree[v][0])
                searched.update(set([v]))
        for v in verts.difference(searched):
            if tree[v][0] > opt:
                searched.update(set([v]))
        
        next_verts=deepcopy(verts)
        for v in verts.difference(searched):
            searched.update(set([v]))
            new_dict = gen_leaves(tree[v][2],tree[v][3],tree[v][4],tree[v][5])
            for i in new_dict.keys():
                a_dict=deepcopy(new_dict)
                (LP,X) = form_lp(a_dict[i][0],a_dict[i][1],c,canonical=False,x_list=X_list,b_list=a_dict[i][2])
                try:
                    nothing=LP.solve()
                    counter+=1;next_verts.update(set([counter]))
                    tree[counter] = (RR(LP.solve()),check_integral(LP.get_values(X)),a_dict[i][0],a_dict[i][1],a_dict[i][2],LP.get_values(X))
                except:
                    nothing=0
                                 
                a_dict=deepcopy(new_dict)
                (LP,X) = form_lp(a_dict[i][0],a_dict[i][3],c,canonical=False,x_list=X_list,b_list=a_dict[i][4])
                try:
                    nothing=LP.solve()
                    counter+=1;next_verts.update(set([counter]))
                    tree[counter] = (RR(LP.solve()),check_integral(LP.get_values(X)),a_dict[i][0],a_dict[i][3],a_dict[i][4],LP.get_values(X))
                except:
                    nothing=0
        verts=deepcopy(next_verts)
    optimal_IP_val = infinity
    optimal_IP_soln = []
    for v in tree:
        if tree[v][1]:
            optimal_IP_val = min(tree[v][0],optimal_IP_val)
    for v in tree:
        if tree[v][1] and tree[v][0]==optimal_IP_val and tree[v][5] not in optimal_IP_soln:
            optimal_IP_soln.append(tree[v][5])
    return optimal_IP_val,optimal_IP_soln