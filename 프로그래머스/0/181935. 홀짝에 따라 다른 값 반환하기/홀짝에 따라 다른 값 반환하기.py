def solution(n):
    if n % 2 == 0:
        return sum (i * i for i in range(n + 1) if i % 2 == 0)
    else:
        return sum(i for i in range(n + 1) if i % 2 == 1)