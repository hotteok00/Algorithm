def solution(arr):
    arr_len = len(arr)
    pow_2 = 1
    while arr_len > pow_2: pow_2 *= 2
    
    return arr + [0 for _ in range(0, pow_2 - arr_len)]