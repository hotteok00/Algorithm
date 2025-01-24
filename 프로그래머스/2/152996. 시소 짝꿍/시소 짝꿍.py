from collections import Counter

def solution(weights):
    freq = Counter(weights)
    answer = 0
    
    # 같은 무게끼리 조합 (a == b)
    for w in freq:
        n = freq[w]
        if n > 1: answer += n * (n - 1) // 2  # C(n, 2)
    
    # 서로 다른 무게 비율 (2, 3/2, 4/3, ...)
    # 우선 weights의 중복 없이 정렬된 리스트를 구함
    unique_weights = sorted(freq.keys())
    
    # 비율 set: (2/3, 3/4, 4/3, 3/2, 1/2, 2)
    # 편의상 (p, q) 형태로 만들어 사용 가능
    ratios = [(2,3), (3,4), (4,3), (3,2), (1,2), (2,1)]
    
    # 딕셔너리/해시로 저장하면 O(1) 검색 가능
    freq_map = dict(freq)
    
    for i in range(len(unique_weights)):
        w1 = unique_weights[i]
        
        for p, q in ratios:
            # w2 = (q/p)*w1 (or p/q?)
            # => (2,1), (1,2), (3,2), (2,3), (4,3), (3,4)
            # 여기선 1은 위에서 처리
            w2 = (p * w1) / q
            
            # w2가 정수인지 체크
            if w2.is_integer():
                w2 = int(w2)
                if w2 > w1:  # w1 < w2 형태로만 계산해서 중복 방지
                    if w2 in freq_map:
                        answer += freq_map[w1] * freq_map[w2]
    
    return answer


# def solution(weights):
#     weights.sort()
    
#     answer = 0
#     prev = {}
    
#     for i in range(len(weights)-1):
#         if i in prev: 
#             answer += prev[i]
#             continue
#         else:
#             prev[i] = 0
#         for j in range(i+1, len(weights)):
#             if isBuddy(weights[i], weights[j]): 
#                 answer += 1
#                 prev[i] += 1
    
#     return answer

# def isBuddy(a, b):
#     seats_a = [2*a, 3*a, 4*a]
#     seats_b = [2*b, 3*b, 4*b]
    
#     for seat in seats_a:
#         if seat in seats_b: return True
#     return False