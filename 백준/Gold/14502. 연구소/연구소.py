from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

# 1. 아무 빈 칸 3곳에 벽 세우기
# 2. 바이러스 퍼질 수 있는 만큼 카운트
# 3. 빈 칸 수 기록
# 4. 벽을 세울 수 있는 경우의 수 반복 (조합)
# 5. 가장 큰 빈 칸 수 출력

N, M = map(int, input().split())
max_blankrooms = 0

Lab = []
blankRooms = []
virusRooms = []
combOfWall = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):        
        if tmp[j] == 0:
            blankRooms.append((i, j))
        if tmp[j] == 2:
            virusRooms.append((i, j))
    Lab.append(tmp)

def comb(blankRooms, r, start, current_comb, result):
    if len(current_comb) == r:
        result.append(current_comb[:])
        return
    
    for i in range(start, len(blankRooms)):
        current_comb.append(blankRooms[i])
        comb(blankRooms, r, i + 1, current_comb, result)
        current_comb.pop()

def bfs(x, y, visited):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx <= N-1 and 0 <= ny <= M-1) and Lab[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
                
    return count

comb(blankRooms, 3, 0, [], combOfWall)

for i in combOfWall:    
    # Lab에 벽 세우기
    for x, y in i:
        Lab[x][y] = 1
    
    # visited = [[False for _ in range(M)] for _ in range(N)]
    # for x, y in virusRooms:
    #     bfs(x, y, visited)
        
    # count_blankRooms = 0
    # for x in range(N):
    #     for y in range(M):
    #         if Lab[x][y] == 0 and not visited[x][y]:
    #             count_blankRooms += 1
    
    # if max_blankrooms < count_blankRooms:
    #     max_blankrooms = count_blankRooms
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    for x, y in virusRooms:
        count += bfs(x, y, visited)
        
    count_blankRooms = len(blankRooms) - 3 - count
    if max_blankrooms < count_blankRooms:
        max_blankrooms = count_blankRooms
    
    # Lab에 세운 벽 원복
    for x, y in i:
        Lab[x][y] = 0
        
print(max_blankrooms)