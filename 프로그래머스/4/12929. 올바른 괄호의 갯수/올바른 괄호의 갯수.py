def solution(n):
    if n == 1: return 1  
    
    cnt_list = [0, 1]
    
    for i in range(1, n):
        tmp = 0
        
        l = len(cnt_list)
        for j in range(l):
            tmp += (l - j) * cnt_list[j]
        
        tmp += 1
        
        cnt_list.append(tmp)
    
    return cnt_list[n]