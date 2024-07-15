from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

# input 
# 정사각형 한 변의 길이 N
# 지도 N * N

N = int(input())
map = [list(map(int, input()[:-1])) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
queue = deque()   # bfs
count_group = 0     # 단지 수
count_house = []    # 단지 내 집 수
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            count_group += 1
            
            queue.append((i, j))
            visited[i][j] = True
            tmp = 1
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx <= N-1 and 0 <= ny <= N-1) and map[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        tmp += 1
            
            count_house.append(tmp)
            
# output
# 총 단지 수
# 각 단지 내 집 수 / 오름차순으로 / 출력

print(count_group)
for i in sorted(count_house):
    output(str(i) + '\n')