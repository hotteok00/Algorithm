def solution(n):
    answer = []
    
    x, y, cnt = 0, 0, 1
    snail = [[0 for _ in range(i + 1)] for i in range(n)]
    
    max_cnt = n * (n + 1) // 2
    
    while cnt <= max_cnt:
        for row in range(n):
            if snail[x][y] != 0: break
            snail[x][y] = cnt
            x += 1
            cnt += 1
        
        n -= 1
        x -= 1
        y += 1
        
        for col in range(n):
            if snail[x][y] != 0: break
            snail[x][y] = cnt
            y += 1
            cnt += 1
        
        n -= 1
        x -= 1
        y -= 2
        
        for row in range(n):
            if snail[x][y] != 0: break
            snail[x][y] = cnt
            x -= 1
            y -= 1
            cnt += 1
        
        n -= 1
        x += 2
        y += 1
    
    for s in snail: answer += s
    return answer