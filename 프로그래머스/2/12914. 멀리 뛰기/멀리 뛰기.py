def solution(n):
    answer = 0
    
    a = n
    for k in range(n, -1, -2):
        # print(a, k)
        answer += facto(a) // (facto(a - k) * facto(k))
        a -= 1
    
    return answer % 1234567

def facto(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result