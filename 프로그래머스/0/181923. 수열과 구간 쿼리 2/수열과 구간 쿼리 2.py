def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        tmp = 1000000
        for i in arr[s:e+1]:
            if k < i < tmp:
                tmp = i
        if tmp == 1000000: answer.append(-1)
        else: answer.append(tmp)
    
    return answer