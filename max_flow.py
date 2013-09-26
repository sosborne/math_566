def int_flow(Edges):
    Flow={}
    for edge in Edges:
        Flow[edge[0],edge[1]]=[edge[2],0]
    return Flow

def aux_mat(Flow,n):
    A=Matrix(n)
    for edge in Flow:
        if Flow[edge][0]>Flow[edge][1]:
            A[edge[0],edge[1]]=1
        if Flow[edge][1] > 0:
            A[edge[1],edge[0]]=1
    return list(A)
    
def aug_path(A,r,s):
    R = set([r])
    S = set([])
    n = len(A)
    d={r:0}
    p={r:None}
    for i in range(0,n):
        if i!=r:
            d[i]=infinity
    while s not in R and R != S:
        RmS = R.difference(S)
        dist = min(d[key] for key in RmS)
        for key in RmS:
            if d[key]==dist:
                v=key
                break
        S.update(set([v]))
        N=[]
        for i in range(0,n):
            if A[v][i]!=0:
                N.append(i)
        for u in N:
            if u not in R:
                R.update(set([u]))
                d[u] = d[v]+1
                p[u]=v
    if s in R:
        path=[s]
        v=s
        while v!=r:
            path.append(p[v])
            v = p[v]
        path.reverse()
        return True,path
    else:
        return False,R

def push_flow(Flow,path):
    new_Flow=deepcopy(Flow)
    path_edges=[]
    for i in range(0,len(path)-1):
        path_edges.append((path[i],path[i+1]))
    
    forward,backward=[],[]
    for edge in path_edges:
        if edge in Flow:
            forward.append(edge)
        else:
             backward.append(edge)
    if len(backward)==0:
        epsilon=min(Flow[edge][0]-Flow[edge][1] for edge in forward)
    elif len(forward)==0:
        epsilon = min(Flow[(edge[1],edge[0])][1] for edge in backward)
    else:
        epsilon = min(min(Flow[edge][0]-Flow[edge][1] for edge in forward), \
            min(Flow[(edge[1],edge[0])][1] for edge in backward))
    for edge in forward:
        new_Flow[edge][1]+=epsilon
    for edge in backward:
        new_Flow[(edge[1],edge[0])][1]-=epsilon
        
    return new_Flow

def flow_value(Flow,s):
    flow_sum=0
    for edge in Flow:
        if edge[0]==s:
            flow_sum-=Flow[edge][1]
        elif edge[1]==s:
            flow_sum+=Flow[edge][1]
    return flow_sum
    
def cut_value(Edges,R):
    cut_sum=0
    for r in R:
        for edge in Edges:
            if edge[0]==r and edge[1] not in R:
                cut_sum+=edge[2]
    return cut_sum
    
def max_flow(Edges,n,r,s):
    Flow = int_flow(Edges)
    A = aux_mat(Flow,n)
    cont,path = aug_path(A,r,s)
    while cont:
        Flow=push_flow(Flow,path)
        A = aux_mat(Flow,n)
        cont,path = aug_path(A,r,s)
    return Flow,flow_value(Flow,s),path,cut_value(Edges,path)