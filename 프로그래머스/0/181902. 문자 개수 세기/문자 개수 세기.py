def solution(my_string):
    answer = [0 for _ in range(26 * 2)]
    
    for c in my_string:
        answer[index_of_char(c)] += 1
    
    return answer

def index_of_char(c):
    if 'A' <= c <= 'Z': return ord(c) - 65
    else: return ord(c) - 97 + 26