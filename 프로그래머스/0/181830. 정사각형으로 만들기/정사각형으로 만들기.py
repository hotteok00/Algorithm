def solution(arr):
    rowLen = len(arr)
    colLen = len(arr[0])
    
    if rowLen > colLen:
        for a in arr:
            for _ in range(colLen, rowLen):
                a.append(0)
    elif rowLen < colLen:
        for _ in range(rowLen, colLen):
            arr.append([0] * colLen)
    
    return arr