#Uses python3

import sys

def reach(adj, x, y):
    global n
    visited = [False]*n

    def explore(v, adj):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w, adj)
        return

    explore(x, adj)

    if visited[y]:
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()    # read all data
    data = list(map(int, input.split()))    # make a list of all data
    n, m = data[0:2]    # params in the problem, n vertices, m edges
    data = data[2:]     # the rest of the data
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2])) # start:end:increment
    x, y = data[2 * m:] # the last line is the pair of vertices we want to check
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(adj, x, y))
