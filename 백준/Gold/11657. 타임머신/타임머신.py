from sys import stdin, stdout
input = stdin.readline
output = stdout.write

import sys

N, M = map(int, input().split())
distance = [sys.maxsize for _ in range(N + 1)]
graph = []
for _ in range(M):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])

distance[1] = 0
for _ in range(N - 1):
    for u, v, w in graph:
        if distance[u] != sys.maxsize and distance[v] > distance[u] + w:
            distance[v] = distance[u] + w
            
cycle = False
for u, v, w in graph:
    if distance[u] != sys.maxsize and distance[v] > distance[u] + w:
        cycle = True
        
if not cycle:
    for i in range(2, N + 1):
        if distance[i] == sys.maxsize: output(str(-1) + "\n")
        else: output(str(distance[i]) + "\n")
else:
    print(-1)