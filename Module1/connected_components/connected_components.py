#Uses python3

import sys

def number_of_components(adj):
    n = len(adj)
    result = 0

    visited = [False]*n

    def explore(v, adj):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w, adj)
        return

    def DFS(adj):
        num_regions = 0
        for v in range(n):
            if not visited[v]:
                explore(v, adj)
                num_regions += 1
        return num_regions

    result = DFS(adj)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
