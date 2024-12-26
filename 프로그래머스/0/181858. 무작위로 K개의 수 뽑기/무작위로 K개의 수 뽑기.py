def solution(arr, k):
    arrSet = []
    for i in arr:
        if i not in arrSet:
            arrSet.append(i)
        if len(arrSet) >= k: 
            break
    
    return list(arrSet)[:k] + [-1 for _ in range(len(arrSet), k)]