from collections import deque

def solution(x, y, n):
    q = deque()
    q.append([y, 0])
    
    while q:
        y, cnt = q.popleft()
        
        if y < x: continue
        
        if y == x: return cnt
        
        if y % 3 == 0: q.append([y // 3, cnt + 1])
        if y % 2 == 0: q.append([y // 2, cnt + 1])
        q.append([y - n, cnt + 1])
    
    return -1