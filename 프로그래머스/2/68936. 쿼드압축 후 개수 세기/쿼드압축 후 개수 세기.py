def solution(arr):
    cnt_0, cnt_1 = count(arr, 0), count(arr, 1)
    
    std_len = len(arr)
    while std_len > 1:
        for x in range(0, len(arr), std_len):
            for y in range(0, len(arr), std_len):
                
                if arr[x][y] == -1: continue
                
                tmp = quadTree(arr, x, y, std_len)
                if tmp == 0:
                    cnt_0 = cnt_0 - std_len * std_len + 1
                elif tmp == 1:
                    cnt_1 = cnt_1 - std_len * std_len + 1
        
        std_len //= 2
    
    return [cnt_0, cnt_1]

def count(arr, n):
    cnt = 0
    for i in arr:
        for j in i:
            if j == n: cnt += 1
    return cnt

def quadTree(arr, x, y, std_len):
    for i in range(x, x + std_len):
        for j in range(y, y + std_len):
            if arr[x][y] != arr[i][j]: return
    
    result = arr[x][y]
    for i in range(x, x + std_len):
        for j in range(y, y + std_len):
            arr[i][j] = -1

    return result