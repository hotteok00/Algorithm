from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

N, M, K, X = map(int, input().split())

SourceAndDestination = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, input().split())
    SourceAndDestination[A].append(B)
    
queue = deque()
visited = [False] * (N + 1)

queue.append(X)
visited[X] = 1

result = []
while queue:
    source = queue.popleft()
    
    tmp = []
    for destination in SourceAndDestination[source]:
        if visited[destination] == False:
            queue.append(destination)
            tmp.append(destination)
            visited[destination] = visited[source] + 1
    
    if visited[source] < K: continue
    if visited[source] == K: result += tmp
    if visited[source] > K: break
    
    
if len(result) == 0: print(-1)
else:
    result.sort()
    for i in result: output(str(i) + "\n")