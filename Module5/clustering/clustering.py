#Uses python3
import sys
import math

input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
data = data[1:]
x = data[0:2 * n:2]
y = data[1:2 * n:2]
data = data[2 * n:]
k = data[0]
rank = [1]*n
parent = list(range(0, n))


def clustering(x, y, k):
    #write your code here
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                edges.append((math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2), i, j))
    edges.sort(key=lambda tup: tup[0], reverse=False)
    # print(edges)
    j = 0
    num_edges = 0
    while num_edges < (n-k):
        if getParent(edges[j][1]) != getParent(edges[j][2]):
            merge(edges[j][1], edges[j][2])
            num_edges += 1
        j += 1

   
    while getParent(edges[j][1]) == getParent(edges[j][2]):
        j += 1
    d = edges[j][0]
    # print(parent)

    return d

def getParent(table):
    # find parent and compress path
    if parent[table] != table:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size

    if rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
    else:
        parent[realSource] = realDestination
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] += 1





print("{0:.9f}".format(clustering(x, y, k)))

