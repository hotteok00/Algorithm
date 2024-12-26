def solution(code):
    mode = 0
    answer = []
    
    for idx in range(len(code)):
        if code[idx] == '1': mode = 0 if mode else 1
        elif idx % 2 == mode: answer.append(code[idx])
        
    if len(answer) == 0: return "EMPTY"
    return ''.join(answer)