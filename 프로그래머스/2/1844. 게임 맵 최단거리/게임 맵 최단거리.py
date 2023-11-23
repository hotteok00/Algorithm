from collections import deque

def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    start_x, start_y = 0, 0
    end_x, end_y = n-1, m-1
    
    q = deque()
    q.append((start_x, start_y, 1))
    
    visited = set()
    visited.add((start_x, start_y))
    
    while q:
        x, y, distance = q.popleft()
        
        if (end_x, end_y) == (x, y):
            answer = distance
            break
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                q.append((nx, ny, distance + 1))
                visited.add((nx, ny))
    
    return answer