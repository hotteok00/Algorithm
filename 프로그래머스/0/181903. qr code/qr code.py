def solution(q, r, code):
    answer = []
    
    for idx in range(len(code)):
        if idx % q == r:
            answer.append(code[idx])
            
    return ''.join(answer)