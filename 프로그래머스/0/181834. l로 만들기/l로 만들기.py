def solution(myString):
    answer = []
    
    for c in myString:
        if c > 'l':
            answer.append(c)
        else:
            answer.append('l')
    
    return ''.join(answer)