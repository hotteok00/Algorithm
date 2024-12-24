def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    
    # x방향, y방향
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    idx_drt = 0
    x, y = 0, 0
        
    while cnt <= n ** 2:
        answer[x][y] = cnt
        if (x + direction[idx_drt][0] < n and answer[x + direction[idx_drt][0]][y] == 0) or (y + direction[idx_drt][1] < n and answer[x][y + direction[idx_drt][1]] == 0):
            x += direction[idx_drt][0]
            y += direction[idx_drt][1]
        else:
            idx_drt = (idx_drt + 1) % 4
            x += direction[idx_drt][0]
            y += direction[idx_drt][1]
        cnt += 1
    
    return answer