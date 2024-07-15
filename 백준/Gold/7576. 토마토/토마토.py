from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

# input
# N * M 격자 상자
# 0, 1, -1 : 안 익은 토마토, 익은 토마토, 빈 칸

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(M)]
queue = deque()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
day_count = -1
zero_count = 0

# 익은 토마토와 인접한 안 익은 토마토는 하루 뒤에 익는다.
# 최대 일 수는 (N - 1) + (M - 1)
# 이중 반복문을 한번 돌고 나서 queue에 저장한 좌표 1, count += 1  
    
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            queue.append((x, y))
        elif box[x][y] == 0:
            zero_count += 1
        
while queue:
    len_Q = len(queue)
    for _ in range(len_Q):
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx <= N-1 and 0 <= ny <= M-1) and box[nx][ny] == 0:
                queue.append((nx, ny))
                box[nx][ny] = 1
                zero_count -= 1
    
    day_count += 1

# output
# 토마토가 다 익는데 걸리는 시간 = 완전 탐색까지 걸리는 탐색 횟수
# 토마토가 모두 익지 못하면 -1

if zero_count == 0:
    print(day_count)
else:
    print(-1)