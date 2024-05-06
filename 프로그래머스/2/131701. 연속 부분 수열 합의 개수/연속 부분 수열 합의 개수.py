def solution(elements):
    length = len(elements)
    
    total_seqence_partial_sum = {}
    answer = set()
    
    for i in range(length):
        total_seqence_partial_sum[(i, i)] = elements[i]
        answer.add(elements[i])
    
    for i in range(1, length):
        window_size = i
        
        for j in range(length):
            start = j
            end = j + window_size
            
#             partial_sum = 0
#             for k in range(start, end):
#                 partial_sum += elements[k % length]
            
            partial_sum = total_seqence_partial_sum[(start, end - 1)] + elements[end % length]
                
            total_seqence_partial_sum[(start, end)] = partial_sum
            answer.add(partial_sum)
    
    return len(answer)