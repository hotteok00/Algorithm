def solution(n, t, m, p):
    answer = ''
    num = 0
    temp = ''
    
    while len(temp) < t * m:
        temp += convert_to_base_n(num, n)
        num += 1
    
    return temp[p-1:t*m:m]

def convert_to_base_n(num, base):
    if num == 0:
        return '0'
    
    digits = '0123456789ABCDEF'
    result = ''
    
    while num:
        result = digits[num % base] + result
        num //= base
        
    return result