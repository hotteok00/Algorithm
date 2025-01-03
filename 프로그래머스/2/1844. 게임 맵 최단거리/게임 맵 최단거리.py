from collections import deque

def solution(maps):
    x, y, distance = 0, 0, 0
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    next_paths = deque()
    
    next_paths.append([x, y])
    visited[x][y] = True
    while next_paths:
        distance += 1
        for _ in range(len(next_paths)):
            nx, ny = next_paths.popleft()

            if isArrived(nx, ny, maps): 
                return distance

            get_next_paths(nx, ny, maps, visited, next_paths)
        
    return -1

def isArrived(nx, ny, maps):
    if nx == len(maps) - 1 and ny == len(maps[0]) - 1:
        return True
    return False

def get_next_paths(x, y, maps, visited, next_paths):
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])):
            if not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                next_paths.append([nx, ny])