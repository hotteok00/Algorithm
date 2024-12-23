def solution(a, d, included):
    answer = 0
    
    for i in included:
        if i: answer += a
        a += d
    
    return answer