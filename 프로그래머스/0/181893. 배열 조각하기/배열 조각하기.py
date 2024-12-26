def solution(arr, query):
    for idx in range(len(query)):
        if idx % 2 == 0:
            arr = arr[:query[idx]+1]
        else:
            arr = arr[query[idx]:]
    return arr