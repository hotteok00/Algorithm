from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

# input
# N
# RGB grid (N * N)

N = int(input())
grid = [list(input()[:-1]) for _ in range(N)]

directions = [(0,1),(1,0),(0,-1),(-1,0)]

visited_N = [[False for _ in range(N)] for _ in range(N)]
visited_RG = [[False for _ in range(N)] for _ in range(N)]

queue_N = deque()
queue_RG = deque()

count_sector_N = 0
count_sector_RG = 0

# 적녹 색약 : R == G

for flag in ['R', 'G', 'B']:
    for i in range(N):
        for j in range(N):
            if grid[i][j] == flag and not visited_N[i][j]:
                count_sector_N += 1
                
                queue_N.append((i, j))
                visited_N[i][j] = True
                
                while queue_N:
                    x, y = queue_N.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx <= N-1 and 0 <= ny <= N-1) and grid[nx][ny] == flag and not visited_N[nx][ny]:
                            queue_N.append((nx, ny))
                            visited_N[nx][ny] = True

            if (flag in 'RG' and grid[i][j] in 'RG') and not visited_RG[i][j]:
                count_sector_RG += 1
                
                queue_RG.append((i, j))
                visited_RG[i][j] = True
                
                while queue_RG:
                    x, y = queue_RG.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx <= N-1 and 0 <= ny <= N-1) and (grid[nx][ny] in 'RG') and not visited_RG[nx][ny]:
                            queue_RG.append((nx, ny))
                            visited_RG[nx][ny] = True
            
            if (flag == 'B' and grid[i][j] == 'B') and not visited_RG[i][j]:
                count_sector_RG += 1
                
                queue_RG.append((i, j))
                visited_RG[i][j] = True
                
                while queue_RG:
                    x, y = queue_RG.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx <= N-1 and 0 <= ny <= N-1) and (grid[nx][ny] == 'B') and not visited_RG[nx][ny]:
                            queue_RG.append((nx, ny))
                            visited_RG[nx][ny] = True

# output
# 정상 구역 수
# 적녹색약 구역 수

print(count_sector_N, count_sector_RG)