def solution(arr, queries):
    for i, j in queries:
        swap(arr, i, j)
    
    return arr

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp