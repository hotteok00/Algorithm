def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        if len(str(i).replace('5', '').replace('0', '')) == 0:
            answer.append(i)
    
    if answer == []: return [-1]
    return sorted(answer)