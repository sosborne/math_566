def dist(u,v):
    return real(((u[0]-v[0])^2 + (u[1]-v[1])^2)^(1/2)).n()

def len_tour(H):
    tsp_length = 0
    if type(H) == type([]):
        for i in range(0,len(H)):
            tsp_length += dist(H[i-1],H[i])
    else:
        for edge in H.edges():
            tsp_length+=edge[2]
    return real(tsp_length)

def add_dem_verts(u,v,w):
    u0=u[0]; u1=u[1]; v0=v[0]; v1=v[1];
    if u[0]<v[0]:
        return (u,v,w)
    elif v[0]<u[0]:
        return (v,u,w)
    else:
        if u[1]<v[1]:
            return (u,v,w)
        elif u[1]>v[1]:
            return (v,u,w)
        else:
            return 'Same vertex retard!'

def form_tour(cycle):
    G = Graph()
    G.add_vertices(cycle)
    for i in range(0,len(cycle)):
        G.add_edge(add_dem_verts(cycle[i-1],cycle[i],dist(cycle[i-1],cycle[i])))
    return G

def two_opt(cycle,j,k):
    new_cycle = []
    for i in range(0,j):
        new_cycle.append(cycle[i])
    for i in range(j,k+1):
        new_cycle.append(cycle[k+j-i])
    for i in range(k+1,len(cycle)):
        new_cycle.append(cycle[i])
    return new_cycle

def all_two_opt(cycle):
    count = 0
    while True:
        best_dist = len_tour(cycle)
        for j in range(0,len(cycle)-1):
            break_out = False
            for k in range(j+1,len(cycle)):
                new_cycle = two_opt(cycle,j,k)
                new_dist = len_tour(new_cycle)
                if new_dist < best_dist:
                    cycle = deepcopy(new_cycle)
                    break_out = True
                    break
            if break_out:
                break
        if new_dist < best_dist:
            count +=1
        else:
            return cycle,count

def farthest_insertion(grid):
    G = Graph({})
    G.add_vertices(grid)
    pos_dict = {}
    for vert in G.vertices():
        pos_dict[vert]=[vert[1]*10,vert[0]*10]
    
    max_dist = 0
    pair = None
    for i in range(0,len(grid)):
        for j in range(i+1,len(grid)):
            u,v = grid[i],grid[j]
            this_dist = dist(u,v)
            if this_dist>=max_dist:
                pair = (u,v)
                max_dist = this_dist
    G.add_edge(add_dem_verts(pair[1],pair[0],dist(pair[0],pair[1])))
    remaining_verts = deepcopy(grid)
    remaining_verts.remove(pair[0])
    remaining_verts.remove(pair[1])
    
    count = 0
    while len(remaining_verts)!=0:
        worst_pair = None
        worst_val = 0
        for v in remaining_verts:
            best_add=Infinity
            pair_place=None
            for edge in G.edges():
                add_dist=dist(edge[0],v)+dist(edge[1],v)
                if add_dist.n() < best_add.n():
                    pair_place = ((edge[0],v),(edge[1],v))
                    best_add=add_dist
            if best_add>worst_val:
                worst_val=best_add
                worst_pair = pair_place
        
        a = worst_pair[0]
        b = worst_pair[1]
        G.add_edge(add_dem_verts(a[0],a[1],dist(a[0],a[1])))
        G.add_edge(add_dem_verts(b[0],b[1],dist(b[0],b[1])))
        if count > 0:
            G.delete_edge(add_dem_verts(a[0],b[0],dist(a[0],b[0])))
        count+=1
        remaining_verts.remove(a[1])
    return G,pos_dict