from sys import stdin, stdout
input = stdin.readline
output = stdout.write

MAX = 250000001

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

from queue import PriorityQueue
q = PriorityQueue()
distance = [PriorityQueue() for _ in range(N + 1)]

distance[1].put((0, 0))
q.put((0, 1))
while q.qsize() > 0:
    prev_w, u = q.get()
    
    for v, w in graph[u]:
        # print(f"{u} to {v} with {w}")
        if distance[v].qsize() < K:
            distance[v].put((-(prev_w + w), prev_w + w))
            q.put((prev_w + w, v))
        elif distance[v].queue[0][1] > prev_w + w:
            # print("pop", distance[v].queue[0][1], prev_w + w)
            distance[v].get()
            distance[v].put((-(prev_w + w), prev_w + w))
            q.put((prev_w + w, v))
    
    # for Q in distance:    
    #     output(str(Q.queue) + " ")
    # print()

for i in range(1, N + 1):
    Q = distance[i]
    if Q.qsize() < K: output(str(-1) + "\n")
    else: output(str(Q.queue[-K][1]) + "\n")