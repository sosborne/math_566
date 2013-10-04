#Initialize data arrays
n={}
r={}
s={}
Edges={}
window_sizes={}

# For all problems, there are n vertices, 0...n-1.
# Use the values of r and s as the vertices for flow source
#    and sink.
# The list 'Edges' stores triples (i,j,c) where c is the capacity
#    of the directed edge (i,j).

# Problem 1a
key = '1a'
n[key] =  10;
r[key] =  0;
s[key] =  9;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,6),(0,2,4),(0,3,2),(0,4,5),(1,5,3),(1,6,6),(2,5,2),(2,7,3),\
            (3,8,1),(4,7,3),(4,8,4),(5,9,1),(6,9,5),(7,9,3),(8,9,10)];

# Problem 3a
key = '3a'
n[key] =  8;
r[key] =  0;
s[key] =  7;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,2),(0,6,3),(2,1,infinity),(3,1,infinity),(4,3,infinity),\
              (4,5,infinity),(4,6,infinity),(5,2,infinity),(5,7,4),(6,7,3)];

# Problem 4a
key = '4a'
n[key] =  6;
r[key] =  4;
s[key] =  5;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,1),(1,0,1),(1,2,1,),(1,3,1),(2,1,1),(2,3,1),(2,4,1),(3,1,1),\
              (3,2,1),(3,5,1),(4,2,1),(4,5,1),(5,3,1),(5,4,1)];

