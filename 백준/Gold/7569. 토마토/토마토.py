from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

# input 
# N, M, H
# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 빈 칸

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
directions = [(0,0,1),(0,1,0),(1,0,0),(0,0,-1),(0,-1,0),(-1,0,0)]
current_queue = deque()
next_queue = deque()

count_day = -1
count_zero = 0

def check_coordinates(x, y, z):
    if 0 <= x <= H-1 and 0 <= y <= N-1 and 0 <= z <= M-1:
        return True
    return False

# (순차 탐색 중, 1 찾으면 1 주변 queue에 삽입) 반복 = 너무 많은 순차 탐색 -> 1의 좌표 기억?

for x in range(H):
    for y in range(N):
        for z in range(M):            
            if box[x][y][z] == 1: 
                current_queue.append((x, y, z))
                continue
            if box[x][y][z] == 0:
                count_zero += 1

while current_queue:
    while current_queue:
        x, y, z = current_queue.popleft()
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if check_coordinates(nx, ny, nz) and box[nx][ny][nz] == 0:
                next_queue.append((nx, ny, nz))
                box[nx][ny][nz] = 1
                count_zero -= 1
    
    count_day += 1
    
    while next_queue:
        current_queue.append(next_queue.popleft())
    
# output 
# 모든 토마토가 익는데 걸리는 최소 시간
# 다 못 익으면 -1

if count_zero > 0: print(-1)
else: print(count_day)