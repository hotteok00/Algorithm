import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_candidates(arrayA, arrayB):
    # 1. arrayA의 전체 GCD 구하기
    from functools import reduce
    gcdA = reduce(gcd, arrayA)
    
    # 2. gcdA의 모든 약수 구하기
    divisors = set()
    limit = int(math.isqrt(gcdA))
    for d in range(1, limit+1):
        if gcdA % d == 0:
            divisors.add(d)
            divisors.add(gcdA // d)
    
    # 3. arrayB 원소들의 약수가 되지 않는 것만 필터링
    candidates = []
    for divisor in divisors:
        if all(b % divisor != 0 for b in arrayB):
            candidates.append(divisor)
            
    return candidates

def solution(arrayA, arrayB):
    # arrayA 원소들의 공약수이면서, arrayB 원소들의 약수는 아닌 최댓값
    candidatesA = get_candidates(arrayA, arrayB)
    
    # arrayB 원소들의 공약수이면서, arrayA 원소들의 약수는 아닌 최댓값
    candidatesB = get_candidates(arrayB, arrayA)
    
    # 필터링된 것 중 최댓값 찾기
    candidates = candidatesA + candidatesB
    if candidates:
        return max(candidates)
    else:
        return 0
    
    return answer