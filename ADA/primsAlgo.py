import sys
def findMinKey(key,mst,n):
    minimum = sys.maxsize
    minIndex=None
    for i in range(n):
        if (mst[i] == False) and key[i]<minimum:
            minimum = key[i]
            minIndex = i
    return minIndex

def prim(graph,n):
    mst=[False]*n
    parent=[-1]*n
    inf = sys.maxsize
    key =[inf]*n
    key[0] =0
    print(key)
    for i in range(n-1):
        u = findMinKey(key,mst,n)
        print(u)
        mst[u]=True
        for v in range(n):
            if graph[u][v] and mst[v] ==False and graph[u][v] <key[v]:
                parent[v] = u
                key[v] = min(graph[u][v],key[v])
    for i in range(1,n):
        print(parent[i],"-",i," = ",graph[i][parent[i]])

matrix = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

prim(matrix,5)

    


    