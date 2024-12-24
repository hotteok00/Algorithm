def solution(a, b, c, d):    
    p, q, r, N = check(a, b, c, d)
    
    if N == 5: return min(a, b, c, d)
    elif N == 4: return q * r
    elif N == 3: return (p + q) * abs(p - q)
    elif N == 2: return (10 * p + q) ** 2
    else: return 1111 * p

def check(a, b, c, d):
    set_abcd = set([a, b, c, d])
    
    # same 4            p, q, 0, 1
    if len(set_abcd) == 1: return a, a, 0, 1
    
    if len(set_abcd) == 2:
        tmp = [0 for _ in range(7)]
        for i in [a, b, c, d]:
            tmp[i] += 1
        
        if 3 in tmp:
            # same 3, 1         p, q, 0, 2
            return tmp.index(3), tmp.index(1), 0, 2
        else:
            # same 2, same 2    p, q, 0, 3
            set_abcd = list(set_abcd)
            return set_abcd[0], set_abcd[1], 0, 3
    
    # same 2, 1, 1      0, q, r, 4
    if len(set_abcd) == 3:
        if a == b: return 0, c, d, 4
        if a == c: return 0, b, d, 4
        if a == d: return 0, b, c, 4
        if b == c: return 0, a, d, 4
        if b == d: return 0, a, c, 4
        if c == d: return 0, a, b, 4
    
    # 1, 1, 1, 1        0, 0, 0, 5
    return 0, 0, 0, 5