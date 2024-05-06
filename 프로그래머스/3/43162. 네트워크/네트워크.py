def solution(n, computers):
    answer = 0
    
    # 방문할 노드 저장 queue
    # 방문한 노드 기록 = set
    # 네트워크 리스트
    
    visited = set()
    
    for i in range(n):
        if i in visited: continue
        visited.add(i)
        
        dest = [x for x in range(n) if computers[i][x] == 1 and i != x]
        while len(dest):
            i = dest.pop()
            
            if i in visited: continue
            visited.add(i)
            
            dest = dest + [x for x in range(n) if computers[i][x] == 1 and i != x]
        
        answer += 1
    
    return answer