def solution(n, l, r):
    if n == 1: return count_1('11011'[l-1:r])
    
    l_where = find_where(n, l)
    r_where = find_where(n, r)
    
    case = case_distinction(l_where, r_where)
    
    count = r_where - l_where
    l_adjust = l_where * (5 ** (n-1))
    r_adjust = r_where * (5 ** (n-1))
    
    if case == 0:
        return 0
    elif case == 1:
        return (count-1) * (4 ** (n-1)) + position_right(n-1, r-r_adjust)
    elif case == 2:
        return position_left(n-1, l-l_adjust) + (count-1) * (4 ** (n-1))
    elif case == 3:
        return solution(n-1, l-l_adjust, r-r_adjust)
    elif case == 4:
        return position_left(n-1, l-l_adjust) + position_right(n-1, r-r_adjust)
    else:
        return position_left(n-1, l-l_adjust) + (count-2) * (4 ** (n-1)) + position_right(n-1, r-r_adjust)

def position_left(n, l):
    if n == 1: return count_1('11011'[l-1:])
    
    l_where = find_where(n, l)
    
    case = case_distinction(l_where, 5)
    
    count = 5 - l_where
    l_adjust = l_where * (5 ** (n-1))
    
    if case == 1:
        return 2 * (4 ** (n-1))
    elif case == 4:
        return position_left(n-1, l-l_adjust) + (count-1) * (4 ** (n-1))
    else:
        return position_left(n-1, l-l_adjust) + (count-2) * (4 ** (n-1))

def position_right(n, r):
    if n == 1: return count_1('11011'[:r])
    
    r_where = find_where(n, r)
    
    case = case_distinction(-1, r_where)
    
    count = r_where - (-1)
    r_adjust = r_where * (5 ** (n-1))
    
    if case == 2:
        return 2 * (4 ** (n-1))
    elif case == 4:
        return (count-1) * (4 ** (n-1)) + position_right(n-1, r-r_adjust)
    else:
        return (count-2) * (4 ** (n-1)) + position_right(n-1, r-r_adjust)

def find_where(n, target):
    for i in range(5):
        if i * (5 ** (n-1)) < target <= (i + 1) * (5 ** (n-1)):
            return i
        
def case_distinction(l, r):
    if l == 2 or r == 2:
        if l == 2 and r == 2:
            return 0
        else:
            if l == 2 and r != 2:
                return 1
            else:
                return 2
    else:
        if l == r:
            return 3
        else:
            if (l < 2 and r < 2) or (l > 2 and r > 2):
                return 4
            else:
                return 5

def count_1(arr):
    return arr.count('1')
    # ans = 0
    # for i in arr:
    #     if i == '1': ans += 1
    # return ans
    
# def solution(n, l, r):
#     answer = 0
    
#     cantor = get_cantor(n)
#     for i in cantor[l-1:r]:
#         if i == '1': answer += 1
    
#     return answer

# def get_cantor(n):
#     cantor = '1'
#     for _ in range(n):
#         tmp = ''
#         for i in range(len(cantor)):
#             if cantor[i] == '1':
#                 tmp += '11011'
#             else:
#                 tmp += '00000'
#         cantor = tmp
#     return cantor