def aug_paths(A,M):
    (n,m)=A.dimensions()
    G = BipartiteGraph(A.transpose())
    matched = []
    for (u,v,discard) in M:
        matched.extend([u,v])
    S=set(range(0,n))
    X=set(range(0,n))
    Y=set(range(n,n+m))
    S.difference_update(set(matched))
    T=set([])
    p={}
    for x in X:
        p[x]=None
    for y in Y:
        p[y]=None
    
    marked=[]
    while S.difference(set(marked))!= set([]):
        x = list(S.difference(set(marked)))[0]
        marked.append(x)
        for y in G.neighbors(x):
            if (x,y,None) not in M and (y,x,None) not in M:
                if y not in T:
                    T.update(set([y]))
                    p[y]=x
                    if y not in matched:
                        path=[y]
                        next=y
                        while p[next]!=None:
                            next=p[next]
                            path.append(next)
                        path.reverse()
                        return path
                    else:
                        for edge in M:
                            if y in edge:
                                (small,large,discard)=edge
                                if y==small:
                                    p[large]=y
                                    S.update(set([large]))
                                else:
                                    p[small]=y
                                    S.update(set([small]))
    X.difference_update(S)
    X.update(T)
    return X

def max_matching(A):
    G = BipartiteGraph(A.transpose())
    M = [G.edges()[0]]
    P = aug_paths(A,M)
    while type(P)!=type(set([])):
        add=[]
        sub=[]
        while len(P)!=0:
            add.append((min([P[0],P[1]]),max([P[0],P[1]]),None))
            if len(P)>2:
                sub.append((min([P[1],P[2]]),max([P[1],P[2]]),None))
            P.pop(0);P.pop(0)
        M=set(M)
        M.update(set(add))
        M.difference_update(set(sub))
        M=list(M)
        P = aug_paths(A,M)
    return M,P

def excess(W,u,v):
    (n,m)=W.dimensions();E=Matrix(n,n)
    for i in range(0,n):
        for j in range(0,n):
            E[i,j]=(u[i]+v[j]-W[i,j])
    return E

def equal_subgraph(W,u,v):
    (n,m)=W.dimensions();A=Matrix(n,n);E=excess(W,u,v)
    for i in range(0,n):
        for j in range(0,n):
            if E[i,j]==0:
                A[i,j]=1
    return A

def hung_alg(W):
    (n,m)=W.dimensions();u=[];v=[]
    X=set(range(0,n))
    Y=set(range(n,n+m))
    for i in range(0,n):
        u.append(max(W[i]))
        v.append(0)
    A=equal_subgraph(W,u,v)
    while True:
        M,Q=max_matching(A)
        if len(M)==n:
            matching_weight=0
            for (x,y,discard) in M:
                matching_weight+=W[x,y-n]
            return M,u,v,matching_weight,sum(u)+sum(v)
        else:
            R = Q.intersection(X)
            T = Q.intersection(Y)
            ep_list=[]
            for x in X.difference(R):
                for y in Y.difference(T):
                    ep_list.append(u[x]+v[y-n]-W[x,y-n])
            ep=min(ep_list)
            for x in X.difference(R):
                u[x]=u[x]-ep
            for y in T:
                v[y-n]=v[y-n]+ep
            A=equal_subgraph(W,u,v)