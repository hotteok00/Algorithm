def solution(my_string, queries):
    answer = ''
    
    for s, e in queries:
        tmp = list(my_string[s:e+1])
        tmp.reverse()
        my_string = my_string[:s] + ''.join(tmp) + my_string[e+1:]
        
    
    return my_string