def solution(data, col, row_begin, row_end):
    answer = []
    
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    for i in range(len(data)):
        if row_begin <= i+1 <= row_end:
            answer.append(sum([c % (i+1) for c in data[i]]))
            
    for i in range(1, len(answer)):
        answer[0] ^= answer[i]
    
    return answer[0]