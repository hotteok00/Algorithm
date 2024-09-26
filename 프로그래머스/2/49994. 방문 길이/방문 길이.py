def solution(dirs):
    answer = 0
    
    x, y = 0, 0
    path = set()
    
    for d in dirs:
        srt = str(x) + str(y)
        
        if d == 'U':
            if y == 5: continue
            
            y += 1
            end = str(x) + str(y)
            
            if srt + "-" + end in path: continue
            if end + "-" + srt in path: continue
            
            path.add(srt + "-" + end)
            path.add(end + "-" + srt)
            answer += 1
            
        elif d == 'D':
            if y == -5: continue
            
            y -= 1
            end = str(x) + str(y)
            
            if srt + "-" + end in path: continue
            if end + "-" + srt in path: continue
            
            path.add(srt + "-" + end)
            path.add(end + "-" + srt)
            answer += 1
            
        elif d == 'R':
            if x == 5: continue
            
            x += 1
            end = str(x) + str(y)
            
            if srt + "-" + end in path: continue
            if end + "-" + srt in path: continue
            
            path.add(srt + "-" + end)
            path.add(end + "-" + srt)
            answer += 1
            
        elif d == 'L':
            if x == -5: continue
            
            x -= 1
            end = str(x) + str(y)
            
            if srt + "-" + end in path: continue
            if end + "-" + srt in path: continue
            
            path.add(srt + "-" + end)
            path.add(end + "-" + srt)
            answer += 1
    
    return answer