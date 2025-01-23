from collections import deque

START, LEVER, EXIT, X, O = 'S', 'L', 'E', 'X', 'O'
directions = [[0,1],[1,0],[0,-1],[-1,0]]

def reshape(maps):
    s, l = [], []
    n, m = len(maps), len(maps[0])
    outer = [['X' for _ in range(m+2)]]
    new_maps = []
    for i in range(n):
        new_maps.append(['X'])
        for j in range(m):
            if maps[i][j] == START: s = [i+1, j+1]
            if maps[i][j] == LEVER: l = [i+1, j+1]
            new_maps[i].append(maps[i][j])
        new_maps[i].append('X')
    return outer + new_maps + outer, s, l

def find(maps, s, goal):
    n, m = len(maps), len(maps[0])
    
    q = deque()
    distance = [[False for _ in range(m)] for _ in range(n)]
    
    q.append(s)
    distance[s[0]][s[1]] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not distance[nx][ny] and maps[nx][ny] != X:
                q.append([nx, ny])
                distance[nx][ny] = distance[x][y] + 1
                if maps[nx][ny] == goal:
                    return distance[nx][ny]
    return -1

def solution(maps):
    answer = 0
    
    maps, s, l = reshape(maps)
    
    tmp = find(maps, s, LEVER)
    if tmp > 0: answer += tmp
    else: return -1
    
    tmp = find(maps, l, EXIT)
    if tmp > 0: return answer + tmp
    else: return -1