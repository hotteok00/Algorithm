from sys import stdin, stdout
input = stdin.readline
output = stdout.write

MAX = 3000001

N, M = map(int, input().split())
S = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    
shorted_distance = [MAX for _ in range(N + 1)]
shorted_distance[S] = 0

visited = [False for _ in range(N + 1)]

from queue import PriorityQueue
queue = PriorityQueue()
queue.put((shorted_distance[S], S))

while queue.qsize() > 0:
    _, u = queue.get()
    
    if visited[u]: continue
    visited[u] = True
    
    for v, w in graph[u]:
        if shorted_distance[v] > w + shorted_distance[u]:
            shorted_distance[v] = w + shorted_distance[u]
            queue.put((shorted_distance[v], v))
    

for i in range(1, N + 1):
    if shorted_distance[i] == MAX: output(str("INF") + "\n")
    else: output(str(shorted_distance[i]) + "\n")