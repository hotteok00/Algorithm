from collections import deque
def solution(maps):
    answer = []
    
    m, n = len(maps), len(maps[0])
    
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = deque()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != 'X':
                q.append([i, j])
                visited[i][j] = True
                tmp = int(maps[i][j])
                
                while q:
                    x, y = q.popleft()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        
                        if (0<=nx<m and 0<=ny<n) and not visited[nx][ny] and maps[nx][ny] != 'X':
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            tmp += int(maps[nx][ny])
                
                answer.append(tmp)
    
    return sorted(answer) if len(answer) > 0 else [-1]