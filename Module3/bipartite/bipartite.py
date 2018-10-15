#Uses python3

import sys
from collections import deque

def bipartite(adj):
    V = len(adj)
    if V <= 2:  # graphs with 0-2 vertices are always bipartite
        return 1
    class_list = [V+1]*(V)   # V+1 will be at least 4, so no issue with 0/1 comparison later
    classes = [1, 0]
    Queue = deque()
    s = 0
    curr_class = 0
    class_list[s]  = curr_class              # start with node 1
    Queue.append(s)
    while len(Queue) > 0:
        u = Queue.popleft()
        curr_class = class_list[u]
        next_class = classes[curr_class]
        for v in adj[u]:
            if class_list[v] <= 1:      # if discovered, check the class
                if class_list[v] == curr_class:
                    return 0
            else:
                Queue.append(v)
                class_list[v] = next_class

    return 1


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
    print(bipartite(adj))
