from itertools import combinations
from collections import Counter

def solution(orders, course):
    course = {i : [] for i in course}
    for l in course:
        for order in orders:
            for i in list(combinations(sorted(order), l)):
                course[l].append(i)
    
    answer = []
    for k, v in course.items():
        v_max = max(list(Counter(v).values()) + [2], default=2)
        for k_c, v_c in Counter(v).items():
            if v_c == v_max:
                answer.append(''.join(k_c))
    answer.sort()
    
    return answer