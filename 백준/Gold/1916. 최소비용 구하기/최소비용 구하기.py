from sys import stdin, stdout
input = stdin.readline
output = stdout.write

MAX = 10000000001

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    
S, E = map(int, input().split())
    
shorted_distance = [MAX for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

from queue import PriorityQueue
q = PriorityQueue()

shorted_distance[S] = 0
q.put((shorted_distance[S], S))
while q.qsize() > 0:
    _, u = q.get()
    
    if visited[u]: continue
    visited[u] = True
    
    for v, w in graph[u]:
        if shorted_distance[v] > shorted_distance[u] + w:
            shorted_distance[v] = shorted_distance[u] + w
            q.put((shorted_distance[v], v))
    
print(shorted_distance[E])