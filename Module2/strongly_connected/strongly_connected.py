# python3

import sys
sys.setrecursionlimit(200000)

class SCCGraph(object):

    def __init__(self, adj_R, adj_G):
        self.adj = adj_R
        self.adj_G = adj_G
        self.n = len(adj_G)
        self.visited = [False]*n
        self.post_order = [None]*n
        self.order = [None]*n
        self.ct = 1
        self.SCC_ct = 0


    def explore(self, v):
        # mark current vertex true
        self.visited[v] = True
        # for all adjacent vertices, if they haven't yet been explored, explore them
        for w in self.adj[v]:
            if not self.visited[w]:
                self.explore(w)
        # each vertex gets a post-order when its explore routine exits
        self.post_order[v] = self.ct
        self.ct += 1
        return

    def DFS(self):
        # explore all vertices
        for v in range(n):
            if not self.visited[v]:
                self.explore(v)
        return

    def toposort(self):
        self.DFS()
        # highest post-order implies it comes first in a linear ordering
        for v, idx in enumerate(self.post_order):
            self.order[self.n-idx] = v
        return self.order

    def number_of_strongly_connected_components(self):
        # get linear ordering of reverse graph - starting with the source here
        # implies starting with the sink of the original graph
        self.toposort()
        # reset self.visited
        self.visited = [False]*n
        # set adjacency matrix to be the original graph instead of reverse
        self.adj = self.adj_G
        # start at sink of the original graph and explore regions, keeping track
        # of SCC count
        for v in self.order:
            if not self.visited[v]:
                self.explore(v)
                self.SCC_ct += 1
        return self.SCC_ct

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj_G = [[] for _ in range(n)]
    adj_R = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_R[b - 1].append(a - 1)
        adj_G[a - 1].append(b - 1)

    g = SCCGraph(adj_R, adj_G)
    print(g.number_of_strongly_connected_components())
