def solution(n, k):
    answer = 0
    
    converted = converter(n, k)
    for i in converted.split('0'):
        if isPrime(i): answer += 1
    
    return answer

def converter(n, k):
    digits = '0123456789ABCDEF'
    result = ''
    
    while n:
        result = digits[n % k] + result
        n //= k
        
    return result

def isPrime(n):
    if not n.isdigit():
        return False
    
    n = int(n)
    
    if n < 2:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    
    return True