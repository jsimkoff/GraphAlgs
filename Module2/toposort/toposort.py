#Uses python3

import sys


class DAG(object):
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)
        self.visited = [False]*n
        self.post_order = [None]*n
        self.order = [None]*n
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

    def toposort(self):
        self.DFS()
        for v, idx in enumerate(self.post_order):
            self.order[self.n-idx] = v
        return self.order


    # def dfs(adj, used, order, x):
    #     #write your code here
    #     pass
    #
    #
    # def toposort(adj):
    #     used = [0] * len(adj)
    #     order = []
    #     #write your code here
    #     return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    dag = DAG(adj)
    order = dag.toposort()
    for x in order:
        print(x + 1, end=' ')
