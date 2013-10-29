def aug_paths(A,M):
    (n,m)=A.dimensions()
    matched = []
    for (u,v) in M:
        matched.extend([u,v])
    S=set(range(0,n))
    X=set(range(0,n))
    Y=set(range(n,n+m))
    S.difference_update(set(matched))
    T=set([]);p={}
    for x in X:
        p[x]=None
    for y in Y:
        p[y]=None
    marked=[]
    while S.difference(set(marked))!= set([]):
        x = list(S.difference(set(marked)))[0]
        marked.append(x)
        for j in A[x].nonzero_positions():
            y = j+n
            if (x,y) not in M:
                if y not in T:
                    T.update(set([y]))
                    p[y]=x
                    if y not in matched:
                        path=[y];next=y
                        while p[next]!=None:
                            next=p[next]
                            path.append(next)
                        path.reverse()
                        return path
                    else:
                        for edge in M:
                            if y in edge:
                                xp = edge[0]
                                p[xp]=y
                                S.update(set([xp]))
                                break
    X.difference_update(S);X.update(T)
    return X

def check_PM(W):
    (n,m)=W.dimensions()
    if n!=m:
        return False
    else:
        A = Matrix(n,m)
        for x in range(0,n):
            for y in range(0,m):
                if W[x,y]!=0:
                    A[x,y]=1
        if len(max_matching(A)[0]) != n:
            return False
        else:
            return True

def max_matching(A):
    (n,m) = A.dimensions()
    matched = [];M = []
    break_out=False
    for x in range(0,n):
        for y in range(0,m):
            if A[x,y]==1 and y not in matched:
                M.append((x,y+n))
                matched.append(y)
                break_out=True
                break
        if break_out:
            break
    P = aug_paths(A,M)
    while type(P)!=type(set([])):
        add=[];sub=[]
        while len(P)!=0:
            add.append((P[0],P[1]))
            if len(P)>2:
                sub.append((P[2],P[1]))
            P.pop(0);P.pop(0)
        M=set(M);M.update(set(add))
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

def hung_alg(W,min_match=False,error_catching=True):
    if min_match:
        W = -W
    (n,m)=W.dimensions();u=[];v=[]
    if error_catching:
        if n!=m or not check_PM(W):
            return 'No perfect matching!'
    X=set(range(0,n))
    Y=set(range(n,n+m))
    for x in range(0,n):
        u.append(max(W[x]))
    for y in range(0,m):
        v.append(0)
    A=equal_subgraph(W,u,v)
    while True:
        M,Q=max_matching(A)
        if len(M)==n:
            if min_match:
                W = -W
                u = list(-vector(u))
                v = list(-vector(v))
            matching_weight=0
            matching = []
            for (x,y) in M:
                matching.append((x,y-n))
                matching_weight+=W[x,y-n]
            return matching,u,v,matching_weight,sum(u)+sum(v)
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