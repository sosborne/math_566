#Initialize data arrays
n={}
r={}
s={}
Edges={}
window_sizes={}
pos={}

# For all instances, there are n vertices, 0...n-1.
# Use the values of r and s as the vertices for flow source
#    and sink.
# The list 'Edges' stores triples (i,j,c) where c is the capacity
#    of the directed edge (i,j).

# Instance I1
key = '1a'
n[key] =  10;
r[key] =  0;
s[key] =  9;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,6),(0,2,4),(0,3,2),(0,4,5),(1,5,3),(1,6,6),(2,5,2),(2,7,3),\
            (3,8,1),(4,7,3),(4,8,4),(5,9,1),(6,9,5),(7,9,3),(8,9,10)];