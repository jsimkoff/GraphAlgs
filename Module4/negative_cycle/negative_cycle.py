#Uses python3

# this script detects negative weight cycles in a directed graph
# by running Bellman-Ford on all strongly connected componenets 
# of the graph


import sys
from copy import deepcopy

class Graph(object):

    def __init__(self, adj, cost):
        self.adj = adj
        self.cost = cost
        self.V = len(adj)
        # print("V",self.V)
        self.dist = [float('inf')]*self.V
        self.dist[0] = 0
        self.prev = [None]*self.V
    
    def bellman_ford(self, src):
        for k in range(self.V):
            if self.V == 1: # terminate if only one node
                return ([], [], 0)
            if self.dist[src] < 0:  # catches many cases where the source node of the BF call < 0 --> definitely a nw cycle
                return ([],[],1)    # note: this is probably not necessary and may be confusing... 
            for u in range(self.V):     # note: this could be further optimized by not considering already relaxed nodes
                for idx, v in enumerate(self.adj[u]):   # relax nodes
                    if self.dist[v] > self.dist[u] + self.cost[u][idx]:
                        self.dist[v] =  self.dist[u] + self.cost[u][idx]
                        self.prev[v] = u
            if k == 0:  
                dist_km1 = deepcopy(self.dist)
            if k > 0:
                if self.dist == dist_km1:   # terminate early if no improvement
                    return(dist_km1, deepcopy(self.dist), 0)
                elif k < self.V - 1:
                    dist_km1 = deepcopy(self.dist)
                else:
                    return(dist_km1, deepcopy(self.dist), 0)    # at kth iteration, just return values




    def negative_cycle(self):
        [dist_km1, dist_k, flag] = self.bellman_ford(src=0)
        if flag == 1 or dist_k != dist_km1: # return 1 if nw cycle is found in first run of BF
            return 1
     
        if len(dist_k) > 0:     # skip if there is only a single node
            while max(dist_k) == float('inf'):  # find other connected components in the graph and run BF on them
                idx = dist_k.index(max(dist_k))
                self.dist[idx] = 0
                [dist_km1, dist_k, flag] = self.bellman_ford(src=idx)   # starting at new source node
                if flag == 1 or dist_k != dist_km1: # terminate if nw cycle is found in subsequent runs of BF
                    return 1

        return 0    # if no conditions above are met, there is no nw cycle



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
    # print(adj)
    # print(cost)
    G = Graph(adj, cost)
    print(G.negative_cycle())
