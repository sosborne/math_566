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

# Problem 1b
key = '1b'
n[key] =  10;
r[key] =  0;
s[key] =  9;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,5),(0,2,1),(0,3,7),(0,4,3),(1,5,10),(2,5,2),(2,7,6),\
              (3,6,2),(3,8,4),(4,8,7),(5,9,6),(6,9,3),(7,9,1),(8,9,2)];

# Problem 2e
key = '2e'
n[key] =  14;
r[key] =  0;
s[key] =  13;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,1),(0,2,1),(0,3,1),(0,4,1),(0,5,1),(0,6,1),(0,7,1),\
              (1,8,infinity),(2,8,infinity),(2,9,infinity),(2,10,infinity),\
              (3,9,infinity),(3,10,infinity),(3,11,infinity),(4,9,infinity),\
              (4,12,infinity),(5,10,infinity),(6,11,infinity),(6,12,infinity),\
              (7,11,infinity),(7,12,infinity),(8,13,1),(9,13,1),(10,13,1),\
              (11,13,1),(12,13,1)]

# Problem 3a
key = '3a'
n[key] =  8;
r[key] =  0;
s[key] =  7;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,2),(0,6,3),(2,1,infinity),(3,1,infinity),(4,3,infinity),\
              (4,5,infinity),(4,6,infinity),(5,2,infinity),(5,7,4),(6,7,3)];

# Problem 3c
key = '3c'
n[key] =  10;
r[key] =  0;
s[key] =  9;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,4),(0,3,4),(0,4,4),(0,7,2),(0,8,4),(1,2,infinity),\
              (2,9,4),(4,3,infinity),(3,2,infinity),(3,5,infinity),\
              (4,3,infinity),(5,6,infinity),(5,9,7),(6,9,6),(7,6,infinity),\
              (8,5,infinity)];

# Problem 4a
key = '4a'
n[key] =  6;
r[key] =  4;
s[key] =  5;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,1),(1,0,1),(1,2,1),(1,3,1),(2,1,1),(2,3,1),(2,4,1),(3,1,1),\
              (3,2,1),(3,5,1),(4,2,1),(4,5,1),(5,3,1),(5,4,1)];

# Problem 4c
key = '4c'
n[key] =  7;
r[key] =  0;
s[key] =  6;
window_sizes[key] = [6,6]
Edges[key] = [(0,1,1),(0,3,1),(0,4,1),(1,0,1),(1,2,1),(1,3,1),(1,5,1),(2,1,1),\
              (2,4,1),(2,5,1),(3,0,1),(3,1,1),(3,4,1),(3,6,1),(4,0,1),(4,2,1),\
              (4,6,1),(5,1,1),(5,2,1),(5,6,1),(6,3,1),(6,4,1),(6,5,1)];

