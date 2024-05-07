def solution(n):
    c_list = [1, 1]
    
    for i in range(1, n):
        c = 0
        for j in range(i + 1):
            c += c_list[j] * c_list[i - j]
            
        c_list.append(c)
    
    return c_list[n]