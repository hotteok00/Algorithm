from sys import stdin, stdout
input = stdin.readline
output = stdout.write

inf = float('inf')
N, A, B, M = map(int, input().split())

graph = []
for i in range(M):
    s, e, v = map(int, input().split())
    graph.append([s, e, v])

distance = [ -inf for _ in range(N) ]
values = list(map(int, input().split()))

distance[A] = values[A]

for i in range(N + 101):
    for s, e, v in graph:
        if distance[s] == -inf: continue
        elif distance[s] == inf: distance[e] = inf
        elif distance[e] < distance[s] - v + values[e]:
            distance[e] = distance[s] - v + values[e]
            if i >= N - 1: distance[e] = inf

if distance[B] == -inf: print("gg")
elif distance[B] == inf: print("Gee")
else: print(distance[B])
