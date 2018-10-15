#python3

import sys

class Acyclic(object):
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)
        self.visited = [False]*n
        self.post_order = [None]*n
        self.ct = 1

    def explore(self, v):
        self.visited[v] = True
        for w in self.adj[v]:
            if not self.visited[w]:
                self.explore(w)
        self.post_order[v] = self.ct
        self.ct += 1
        return

    def DFS(self):
        for v in range(n):
            if not self.visited[v]:
                self.explore(v)
        return

    def cycle_check(self):
        self.DFS()
        for u in range(self.n):
            for v in self.adj[u]:
                if self.post_order[v] > self.post_order[u]:
                    return 1
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    acyc = Acyclic(adj)
    print(acyc.cycle_check())
