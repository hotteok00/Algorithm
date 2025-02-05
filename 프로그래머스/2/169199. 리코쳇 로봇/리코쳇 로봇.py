from collections import deque

MX = float('inf')

def find_target(board, target):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == target: return (i, j)

def solution(board):
    answer = 0
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    
    q = deque()
    visited = [[MX for _ in range(len(board[0]))] for _ in range(len(board))]
    
    R = find_target(board, 'R')
    # G = find_target(board, 'G')
    
    q.append(R)
    visited[R[0]][R[1]] = 0
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            while (0<=nx<len(board) and 0<=ny<len(board[0])) and board[nx][ny] != 'D':
                nx, ny = nx + dx, ny + dy
            nx, ny = nx-dx, ny-dy
                
            if visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
                if board[nx][ny] == 'G':
                    return visited[nx][ny]
    
    # for i in visited:
    #     for j in i:
    #         print(f'\t{j}', end=', ')
    #     print()
    
    return -1