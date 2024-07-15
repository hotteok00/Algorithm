from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

N, M = map(int, input().split())
    
maze = [list(map(int, input()[:-1])) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    queue = deque([(0, 0)])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            return visited[x][y]
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

print(bfs())