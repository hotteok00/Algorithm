from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N, M = map(int, input().split())

trust = [[] for _ in range(N + 1)]
# trust = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    B, A = map(int, input().split())
    trust[A].append(B)
    
from collections import deque

result = []

max_cnt = 0
for i in range(1, N + 1):
    queue = deque()
    visited = [False] * (N + 1)
    cnt = 0
    
    visited[i] = True
    queue.append(i)
    cnt += 1

    while queue:
        j = queue.popleft()
        for k in trust[j]:
            if not visited[k]:
                visited[k] = True
                queue.append(k)
                cnt += 1
    
    if max_cnt < cnt:
        max_cnt = cnt
        result = [i]
    elif max_cnt == cnt:
        result.append(i)

# result.sort()
print(*result)
