#python3


import sys
from collections import deque



def shortest_paths(adj, cost, s, distance, reachable, shortest):
    V = len(adj)
    prev = [None]*V
    distance[s] = 0

    for k in range(V):  # run Bellman-Ford V times
        if V == 1: # terminate if only one node
            return (reachable, shortest, distance)
        num_changes = 0
        Queue = deque()
        for u in range(V):    # iterate over all edges in each iteration of Bellman-Ford
            if k == 0 or distance[u] < float('inf'):
                for idx, v in enumerate(adj[u]):   # relax nodes
                    if distance[v] > distance[u] + cost[u][idx]:
                        distance[v] =  distance[u] + cost[u][idx]
                        prev[v] = u
                        num_changes += 1
                        if k == V-1:
                            Queue.append(v)
        if k > 0:
            if num_changes == 0:   # trminate early if no improvement
                return(reachable, shortest, distance)

    visited = [0]*V
    while len(Queue) > 0:
        u = Queue.popleft()
        shortest[u] = 0
        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 0:
                Queue.append(v)
                visited[v] = 1
                shortest[u] = 0

    return(reachable, shortest, distance)
    


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [1] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if distance[x] == float('inf'):
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

