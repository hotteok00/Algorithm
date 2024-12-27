def solution(arr):
    for i in range(len(arr) - 1):
        arr[i + 1] = lcm(arr[i], arr[i + 1])
    
    return arr[-1]

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a