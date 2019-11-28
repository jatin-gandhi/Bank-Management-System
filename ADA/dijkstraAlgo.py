import sys
def findMin(dist,spt,V):
    minimum = sys.maxsize
    minIndex = None
    for v in range(V):
        if spt[v]==False and (dist[v] <= minimum):
            minimum = dist[v]
            minIndex = v
    return minIndex

def dijkstra(graph,V):
    inf = sys.maxsize
    spt = [False]*V
    dist=[inf ]*V
    dist[0] = 0
    parent=[-1]*V
    combined=[]
    for i in range(V-1):
        u = findMin(dist,spt,V)
        spt[u]=True
        path =[]
        for v in range(V):
            if graph[u][v] and spt[v] ==False and (dist[v] >dist[u] + graph[u][v]) and dist[u] !=inf :
                dist[v] = dist[u]+graph[u][v]
                parent[v] =u
        print(parent)

        #combined.append(path)

    for i in range(V):
        print(i,"-",dist[i])
        #print(parent)
    #print(combined)

matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]

dijkstra(matrix,9)


