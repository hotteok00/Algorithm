from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

N, M, V = map(int, input().split())
edge = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)

def dfs(v, visited): 
    output(str(v) + ' ')
    visited[v] = True
    
    for i in sorted(edge[v]):
        if not visited[i]:
            dfs(i, visited)
    
def bfs(v, visited): 
    bfs_queue = deque([v])
    visited[v] = True
    
    while bfs_queue:
        v = bfs_queue.popleft()
        
        output(str(v) + ' ')
        
        for i in sorted(edge[v]):
            if not visited[i]:
                bfs_queue.append(i)
                visited[i] = True
    
visited_dfs = [False for _ in range(N + 1)]    
dfs(V, visited_dfs)

print()

visited_bfs = [False for _ in range(N + 1)]
bfs(V, visited_bfs)