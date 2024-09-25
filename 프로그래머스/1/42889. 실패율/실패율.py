def solution(N, stages):
    answer = []
    
    failureRate = [[0, 0, idx] for idx in range(N + 2)]    # not clear yet, arrived
    for s in stages:
        failureRate[s][0] += 1
        for i in range(1, s + 1): failureRate[i][1] += 1
    
    for idx in range(N + 2): 
        b = failureRate[idx][1]
        if b == 0: failureRate[idx][1] = 1
    
    failureRate = failureRate[1:-1]
    failureRate.sort(key = lambda x: -x[0]/x[1])
    
    for a, b, idx in failureRate: answer.append(idx)
    
    return answer