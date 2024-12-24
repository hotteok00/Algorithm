def solution(arr):
    l, r = -1, -1
    
    for i in range(len(arr)):
        if arr[i] == 2:
            l = i
            break
            
    for i in range(len(arr)):
        if arr[len(arr) - 1 - i] == 2:
            r = len(arr) - i
            break
    
    if l == -1 and r == -1:
        return [-1]
    
    return arr[l:r]