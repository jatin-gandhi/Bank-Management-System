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


'''
import sys

size = int(input("Enter number of nodes: "))
source = int(input("Enter source node: "))
matrix = list()
for i in range(size):
    matrix.append(list(map(int, input("Enter row " + str(i) + ": ").strip(" ").split(" "))))

nodes = [i for i in range(size) if i != source]
path = [[[] for i in range(size)]]
visited = [source]

for _ in range(size - 1):
    source_node, destination_node, min_weight = None, None, sys.maxsize
    
    # Find shortest distance
    for visited_node in visited:
        for j in nodes:
            if matrix[visited_node][j] != 0 and matrix[visited_node][j] < min_weight:
                source_node, destination_node, min_weight = visited_node, j, matrix[visited_node][j]
    
    # Update total distances
    for i in nodes:
        if matrix[destination_node][i] != 0:
            matrix[destination_node][i] += matrix[source_node][destination_node]
    
    matrix[source][destination_node] = matrix[source_node][destination_node]
    visited.append(destination_node)
    nodes.remove(destination_node)
    
    path[source][destination_node].extend(path[source][source_node])
    path[source][destination_node].append(source_node)

for i in range(size):
    print("Source", source, "-", "Destination", str(i) + ":", matrix[source][i]) 
    print("Path:", path[source][i])
    
'''


