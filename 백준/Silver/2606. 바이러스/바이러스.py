from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

node = int(input())
edge = int(input())
network = {i + 1 : [] for i in range(node)}
visited = [False for _ in range(node + 1)]

for _ in range(edge):
    s, e = map(int, input().split())
    network[s].append(e)
    network[e].append(s)

def bfs():
    queue = deque([1])
    visited[1] = True
    count = -1
    
    while queue:
        v = queue.popleft()
        count += 1
        
        for i in network[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return count

print(bfs())