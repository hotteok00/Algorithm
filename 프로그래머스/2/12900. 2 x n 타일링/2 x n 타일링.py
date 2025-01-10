def solution(n):
    if n < 3: return n
    prev_1, prev_2 = 1, 2
    for i in range(3, n + 1):
        curr = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = curr
    return prev_2 % 1000000007