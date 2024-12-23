def solution(str1, str2):
    answer = []
    
    for c1, c2 in zip(str1, str2):
        answer.append(c1)
        answer.append(c2)
    
    return ''.join(answer)