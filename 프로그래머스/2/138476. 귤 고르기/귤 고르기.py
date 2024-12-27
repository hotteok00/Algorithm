def solution(k, tangerine):
    arr = {}
    for i in tangerine:
        if i not in arr:
            arr[i] = 0
        arr[i] += 1
        
    arr = sorted(arr.items(), key=lambda item: item[1], reverse=True)
    
    cnt = 0
    tmp = 0
    for i in arr:
        tmp += i[1]
        cnt += 1
        if tmp >= k: break
    
    return cnt