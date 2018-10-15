#python3

import sys

def acyclic(adj):

    def explore(v, adj):
        global ct, post_order
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w, adj)
        post_order[v] = ct
        ct += 1
        return

    def DFS(adj):
        for v in range(n):
            if not visited[v]:
                explore(v, adj)
        return


    n = len(adj)
    visited = [False]*n

    DFS(adj)

    for u in range(n):
        for v in adj[u]:
            if post_order[v] > post_order[u]:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    ct = 1
    post_order = [None]*n
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    print(acyclic(adj))
