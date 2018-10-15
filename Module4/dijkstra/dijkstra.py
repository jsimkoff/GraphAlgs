#python35

import sys
from heapq import *
import math
# python implementation of heapq has parent <= its children: already in the right
# form for ExtractMin



def distance(adj, cost, s, t):
    V = len(adj)
    dist = [float('inf')]*V
    dist[s] = 0
    prev = [None]*V
    PriorityQueue = []

    for v in range(len(adj)):
        heappush(PriorityQueue, (dist[v], v))
    
    # print(PriorityQueue)


    while len(PriorityQueue) > 0:
        # print("heappop():")
        u = heappop(PriorityQueue)[1]
        # print("u", u)
        if u == t and dist[u] != float('inf'):
            return dist[u]

        for idx, v in enumerate(adj[u]):
            # print("v", v)
            # print("idx", idx)
            # print("dist[u]", dist[u])
            # print("dist[v]", dist[v])
            # print("cost[u][v]",cost[u][idx])
            if dist[v] > dist[u] + cost[u][idx]:
                dist[v] = dist[u] + cost[u][idx]
                prev[v] = u
                # print("prev", prev)
                # print("dist", dist)
                heappush(PriorityQueue, (dist[v], v))
                # print("PQ", PriorityQueue)


    return -1

    


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    # print("adj", adj)
    # print("cost", cost)
    print(distance(adj, cost, s, t))
