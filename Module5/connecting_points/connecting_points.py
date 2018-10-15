#Uses python3
import sys
import math
from heapq import heappop, heappush

def minimum_distance(x, y):
    V = len(x)
    added = [0]*V
    node1 = 0
    added[node1] = 1
    curr_node = node1
    total_dist = 0

    PriorityQueue = []

    for i in range(V-1):
        for j in range(V):
            if added[j] == 0:
                dist_j = math.sqrt((x[curr_node]-x[j])**2 + (y[curr_node]-y[j])**2)
                heappush(PriorityQueue, (dist_j, j) )

        (next_dist, next_node) = heappop(PriorityQueue)
        while added[next_node] == 1:
           (next_dist, next_node) = heappop(PriorityQueue) 
        added[next_node] = 1
        total_dist += next_dist
        # print("total_dist", total_dist)
        curr_node = next_node

    result = total_dist
    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
