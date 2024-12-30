def solution(n, left, right):
    arr = []
    
    # for i in range(1, n + 1):
    #     arr.append([i for j in range(i - 1)] + [j for j in range(i, n + 1)])
        
    for i in range(left, right + 1):
        j = i // n
        k = i % n
        
        if j >= k:
            arr.append(j + 1)
        else:
            arr.append(k + 1)
    
    return arr