def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        if flag[i]:
            answer += [arr[i]] * arr[i] * 2
        else:
            answer = answer[:-arr[i]]
    
    return answer